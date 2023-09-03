from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Option:
    name: str
    order: int
    type: str
    help_message: str

@dataclass(frozen=True)
class SubJob:
    name: str
    order: int
    options: List[Option]

class SDK:
    def __init__(self, name: str, order: int, subjobs: List[SubJob]):
        self.name = name
        self.order = order
        self.subjobs = subjobs

# 예시 데이터 생성
example_sdk = SDK(
    name="ExampleSDK",
    order=1,
    subjobs=[
        SubJob(
            name="SubJob1",
            order=1,
            options=[
                Option(
                    name="option1",
                    order=1,
                    type="string",
                    help_message="This is the first option for SubJob1, and it expects a string value."
                ),
                Option(
                    name="option2",
                    order=2,
                    type="int",
                    help_message="This is the second option for SubJob1, and it expects an integer value."
                )
            ]
        ),
        SubJob(
            name="SubJob2",
            order=2,
            options=[
                Option(
                    name="optionA",
                    order=1,
                    type="boolean",
                    help_message="This is the first option for SubJob2, and it expects a boolean value."
                ),
                Option(
                    name="optionB",
                    order=2,
                    type="float",
                    help_message="This is the second option for SubJob2, and it expects a float value."
                )
            ]
        )
    ]
)

print(type(example_sdk))
print(example_sdk)