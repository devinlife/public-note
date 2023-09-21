from dataclasses import dataclass


def update_orm_to_domain(orm_class, domain_class):
    domain_class.name = orm_class.name
    domain_class.age = orm_class.age


@dataclass
class User:
    name: str
    age: int


class OrmUser:
    id: int
    name: str
    age: int

    def __init__(self) -> None:
        self.id = generate_id()


tom = User("tom", 23)
tom_orm = OrmUser()

update_orm_to_domain(tom_orm, tom)
