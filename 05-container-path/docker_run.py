import threading
import time

from utils.file_descriptor import FileDescriptor


class DockerRunStep:
    def __init__(self, client, timeout):
        self._client = client
        self._timeout = timeout
        self._strem_docker_log_thread = None
        self._container_run_thread = None

    def run(
        self,
        job_id,
        image: str,
        command: str,
        base_dir_name: str = None,
        is_aborted: callable[[], bool] = None,
        requirements_file: FileDescriptor = None,
    ):
        container = None

        try:
            name = f"job-{job_id}"
            self._client.images.pull(image)
            volumes = self._get_volumes(base_dir_name)

            # FIXME: proxy 상태인지 확인 추가 해야함
            if requirements_file.container_filepath:
                command = f"pip install -r {requirements_file.container_filepath} && {command}"

            container = self._client.containers.run(
                image=image,
                name=name,
                entrypoint="",
                command=command,
                environment={},
                volumes=volumes,
            )
            self._wait_container_thread = threading.Thread(target=self._wait_container, args=[container], daemon=True)
            self._wait_container_thread.start()

            time.sleep(0.5)

            while container.status != "exited":
                container.reload()
                if is_aborted():
                    container.stop()
                    raise Exception("Job aborted")
                time.sleep(5)

            container.reload()
            stauts_code = container.attrs["State"]["ExitCode"]
            if stauts_code > 0:
                raise Exception("Job failed")
        except Exception as e:
            print(e)
            raise e
        finally:
            if container:
                container.remove(force=True)

    def _get_volumes(self, base_dir_name: str):
        volumes = {}
        if base_dir_name:
            volumes[base_dir_name] = {"bind": base_dir_name, "mode": "rw"}
        return volumes

    def _wait_container(self, container):
        try:
            container.wait(timeout=self._timeout)
        except Exception as e:
            print(e)
            raise e
