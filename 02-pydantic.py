from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

# 딕셔너리로부터 pydantic 모델 객체 생성
data = {
    'name': 'Alice',
    'age': 28,
    'email': 'alice@example.com',
    'address': 'alice@example.com'
}

user = User(**data)
print(user)  # 출력: User(name='Alice', age=28, email='alice@example.com')
