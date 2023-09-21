def camel_to_snake(s: str) -> str:
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

string = "UserJobRun"
converted = camel_to_snake(string)
print(converted)  # 출력: job_run
