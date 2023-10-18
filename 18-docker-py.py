import threading
import time

import docker
from requests.exceptions import ConnectionError

def run_container_and_wait(timeout):
    client = docker.from_env()
    container = client.containers.run("alpine", ["sleep", "300"], name="test11", detach=True, remove=False)
    try:
        container.wait(timeout=timeout)
    except ConnectionError as e:
        print(f"11Timeout reached. Stopping the container. {type(e).__name__}: {e}")
        container.stop()
    except Exception as e:
        print(f"Timeout reached. Stopping the container. {type(e).__name__}: {e}")
        container.stop()


def poll_container_status():
    client = docker.from_env()

    # 최근 실행된 컨테이너를 얻습니다. 실제 환경에서는 컨테이너의 ID나 이름을 사용해서 특정 컨테이너를 찾을 수 있습니다.
    time.sleep(1)
    container = client.containers.list()[0]

    while True:
        time.sleep(2)
        container.reload()
        status = container.status
        name = container.name
        print(f"Container status: {name}/{status}")

        if status not in ["running", "paused"]:
            break


if __name__ == "__main__":
    # 컨테이너 실행 및 wait 메소드를 별도의 스레드에서 실행
    threading.Thread(target=run_container_and_wait, args=(10,)).start()

    # 메인 스레드에서 컨테이너 상태를 폴링
    poll_container_status()
