class JobConfig:
    name: str
    description: str

class Sdk:
    def __init__(self, name, job_configs: set[JobConfig] | None = None):
        self._name = name
        self._job_configs = job_configs or set()

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        return self._name == other.name