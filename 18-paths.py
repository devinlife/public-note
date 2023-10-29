from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

@dataclass
class MeasurementPaths:
    dataset: Path
    outputs: Path
    log: Path

@dataclass
class EvaluationPaths:
    dataset: Path
    outputs: Path
    metric: Path

def load_paths_from_dict(config_data: Dict[str, Dict[str, str]]) -> Tuple[MeasurementPaths, EvaluationPaths]:
    # dict 데이터를 데이터 클래스로 변환
    # Path 객체로 변환
    measurement_paths = MeasurementPaths(**{key: Path(value) for key, value in config_data['measurement'].items()})
    evaluation_paths = EvaluationPaths(**{key: Path(value) for key, value in config_data['evaluation'].items()})
    
    return measurement_paths, evaluation_paths

# 예제 사용
config_dict = {
    "measurement": {
        "dataset": "measurement/dataset",
        "outputs": "measurement/outputs",
        "log": "outputs/log.txt"
    },
    "evaluation": {
        "dataset": "evaluation/dataset",
        "outputs": "evaluation/outputs",
        "metric": "outputs/metric.json"
    }
}

measurement, evaluation = load_paths_from_dict(config_dict)

print(measurement.dataset)  # 출력: measurement/dataset (이것은 Path 객체입니다.)
print(evaluation.metric)    # 출력: outputs/metric.json (이것도 Path 객체입니다.)
