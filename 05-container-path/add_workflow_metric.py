import json

from utils.file_descriptor import FileDescriptor


class AddWorkflowMetric:
    def __init__(self, workflow_api):
        self._workflow_api = workflow_api

    def run(self, workspace_id, workflow_id, base_dir_name, metric_filepath: str):
        try:
            metric_file = FileDescriptor(
                filepath=metric_filepath,
                base_path_local=base_dir_name,
            )
            with open(metric_file.local_filepath, "r") as f:
                metrics = json.load(f)

            self._workflow_api.add_workflow_metrics(workspace_id, workflow_id, metrics)
        except Exception as e:
            print(e)
            raise e
