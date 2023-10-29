import httpx
from utils.download_file import download_file, download_files
from utils.file_descriptor_from_dto import create_file_descriptor_from_dto

INPUT_MODEL_DIR_RELATIVE_PATH = "input_models"
DATASET_DIR_RELATIVE_PATH = "dataset"


class PrepareEvaluationInputStep:
    def __init__(self, workflow_api, bucket_api):
        self._workflow_api = workflow_api
        self._bucket_api = bucket_api

    def run(
        self, workspace_id, workflow_id, job_id, base_dir_name, input_models, previous_output_models, dataset, script
    ):
        try:
            print(f"workspace_id: {workspace_id}, workflow_id: {workflow_id}, job_id: {job_id}")
            input_model_files = create_file_descriptor_from_dto(
                input_models, base_dir_name, INPUT_MODEL_DIR_RELATIVE_PATH
            )
            previous_output_model_files = create_file_descriptor_from_dto(
                previous_output_models, base_dir_name, INPUT_MODEL_DIR_RELATIVE_PATH
            )
            dataset_file = create_file_descriptor_from_dto(dataset, base_dir_name, DATASET_DIR_RELATIVE_PATH)

            # FIXME: get this path form entrypoint
            script_relative_path = "script"
            script_file = create_file_descriptor_from_dto(dataset, base_dir_name, script_relative_path)

            with httpx.Client() as client:
                download_files(client, input_model_files)
                download_files(client, previous_output_model_files)
                download_file(client, dataset_file, extract=True)
                download_file(client, script_file, extract=True)
        except Exception as e:
            print(e)
            raise e
