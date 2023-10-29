import json
from unittest.mock import Mock, mock_open, patch
from uuid import uuid4

from add_workflow_metric import AddWorkflowMetric

workspace_id = uuid4()
workflow_id = uuid4()


def test_run_valid_workflow_metric():
    # Mocks
    mock_workflow_api = Mock()
    mock_workflow_api.add_workflow_metrics = Mock()

    metric_data = {"key": "value"}
    metric_str = json.dumps(metric_data)

    with patch("builtins.open", mock_open(read_data=metric_str)):
        update_workflow = AddWorkflowMetric(mock_workflow_api)
        update_workflow.run(workspace_id, workflow_id, "/mlspace-worker", "developer-option-dir/metric.json")

    # Asserts
    mock_workflow_api.add_workflow_metrics.assert_called_once_with(workspace_id, workflow_id, metric_data)
