파이썬 3.10의 새로운 기능 중 하나는 Structural Pattern Matching이라는 기능입니다. 하지만 여기서는 DDD를 위한 기본 클래스 구조를 제공하겠습니다.

먼저, `Sdk`와 `Job` 클래스를 정의합니다:

```python
from datetime import datetime
from typing import List, Any

class ValueObject:
    """A base class for value objects."""
    
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and vars(self) == vars(other)
    
    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)


class Job(ValueObject):
    def __init__(self, name: str, options: List[Any], created_at: datetime = datetime.now()):
        self.name = name
        self.options = options
        self.created_at = created_at


class Sdk:
    def __init__(self, name: str, jobs: List[Job], created_at: datetime = datetime.now()):
        self.name = name
        self.jobs = jobs
        self.created_at = created_at


# 예제:
job1 = Job(name="Job1", options=["option1", "option2"])
job2 = Job(name="Job2", options=["option3", "option4"])
sdk = Sdk(name="SDK1", jobs=[job1, job2])
```

이 코드에서:

- `ValueObject`는 값 객체를 위한 기본 클래스입니다. 이 클래스를 통해 값 객체들 간의 동일성을 검사할 수 있습니다.
  
- `Job` 클래스는 `ValueObject`를 상속받습니다. 이 클래스는 `name`, `options`, `created_at` 세 가지 속성을 가지고 있습니다.
  
- `Sdk` 클래스는 `name`, `jobs`, `created_at` 세 가지 속성을 가지고 있습니다. `jobs` 속성은 `Job` 객체의 목록입니다.

이렇게 정의한 클래스를 바탕으로 DDD 방법론을 따라 도메인 로직을 추가하실 수 있습니다.