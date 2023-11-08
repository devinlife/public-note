from typing import Any, List

class Command:
    def execute(self, *args, **kwargs) -> Any:
        raise NotImplementedError("You should implement this method")


class ConcreteCommand1(Command):
    def execute(self, *args, **kwargs) -> Any:
        print("Command 1 is being executed")
        # ... 여기에 로직을 구현합니다 ...
        result = "result_from_command1"  # 예제 결과
        return result


class ConcreteCommand2(Command):
    def execute(self, *args, **kwargs) -> Any:
        print("Command 2 is being executed with arguments:", args, kwargs)
        # ... 여기에 로직을 구현합니다 ...
        result = "result_from_command2"  # 예제 결과
        return result


class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def run(self) -> Any:
        result = None
        for command in self._commands:
            if result is not None:
                result = command.execute(result)
            else:
                result = command.execute()

        return result


# 클라이언트 코드 예시
if __name__ == "__main__":
    # 명령 객체 생성
    command1 = ConcreteCommand1()
    command2 = ConcreteCommand2()

    # 실행자(Invoker) 객체 생성 및 명령 추가
    invoker = Invoker()
    invoker.add_command(command1)
    invoker.add_command(command2)

    # 명령 실행
    invoker.run()


-------------


class Step:
    def execute(self, previous_result=None):
        """
        Execute the step logic and return the result if any.
        If there is a result from the previous step, it should be accepted as an argument.
        """
        raise NotImplementedError("Execute method must be implemented by the concrete step classes.")

class Step1(Step):
    def __init__(self, initial_data):
        self.initial_data = initial_data

    def execute(self, previous_result=None):
        print(f"Executing Step 1 with initial data: {self.initial_data} and previous result: {previous_result}")
        # Step logic here...
        result = "result from step 1"
        return result

class Step2(Step):
    def __init__(self, additional_data):
        self.additional_data = additional_data

    def execute(self, previous_result=None):
        print(f"Executing Step 2 with additional data: {self.additional_data} and previous result: {previous_result}")
        # Step logic here...
        result = "result from step 2"
        return result

class Step3(Step):
    def execute(self, previous_result=None):
        print(f"Executing Step 3 with previous result: {previous_result}")
        # Step logic here...
        # This step does not return anything
        pass

class WorkflowEngine:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run(self):
        result = None
        for step in self.steps:
            result = step.execute(previous_result=result)  # Pass the previous result to the next step
            # If a step does not return a result, the previous result is carried forward unchanged
            if result is None and step is not self.steps[-1]:  # Prevent carrying forward None if it's a meaningful result of a step
                raise Exception("Step did not return a result when one was expected.")
        return result  # The final result can be used if needed

# Example usage
if __name__ == "__main__":
    step1 = Step1(initial_data="Data for step 1")
    step2 = Step2(additional_data="Data for step 2")
    step3 = Step3()

    workflow = WorkflowEngine()
    workflow.add_step(step1)
    workflow.add_step(step2)
    workflow.add_step(step3)

    workflow.run()
