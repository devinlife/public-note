from unittest.mock import ANY, MagicMock, patch

import pytest
from prepare_evaluation_input import PrepareEvaluationInputStep

input_models = [{"key": "model1.zip", "download_url": "http://example.com/model1.zip"}]
previous_output_models = [{"key": "model2.zip", "download_url": "http://example.com/model2.zip"}]
dataset = {"key": "dataset1.zip", "download_url": "http://example.com/dataset1.zip"}
script = {"key": "script1.zip", "download_url": "http://example.com/script1.zip"}


@pytest.fixture
def mock_prepare_evaluation_input_step():
    workflow_api = MagicMock()
    bucket_api = MagicMock()
    return PrepareEvaluationInputStep(workflow_api, bucket_api)


def test_prepare_evaluation_input_step_run(mock_prepare_evaluation_input_step):
    with patch("prepare_evaluation_input.create_file_descriptor_from_dto") as mock_create_file_descriptor, patch(
        "prepare_evaluation_input.download_files"
    ) as mock_download_files, patch("prepare_evaluation_input.download_file") as mock_download_file:
        mock_create_file_descriptor.return_value = MagicMock()

        mock_prepare_evaluation_input_step.run(
            workspace_id="workspace1",
            workflow_id="workflow1",
            job_id="job1",
            base_dir_name="/base",
            input_models=input_models,
            previous_output_models=previous_output_models,
            dataset=dataset,
            script=script,
        )

        assert mock_create_file_descriptor.call_count == 4
        mock_download_files.assert_called_with(ANY, mock_create_file_descriptor.return_value)
        mock_download_file.assert_called_with(ANY, mock_create_file_descriptor.return_value, extract=True)
