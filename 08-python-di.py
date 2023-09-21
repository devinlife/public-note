from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


class Service:
    def __init__(self, database_url: str):
        print(f"Service is created: {database_url}")
        self.database_url = database_url
        # ... 다른 초기화 코드 ...


class Container(containers.DeclarativeContainer):
    # database_url을 상수로 지정하지 않고 단순히 Service 클래스의 생성을 위한 팩토리로만 둡니다.
    service = providers.Factory(Service)


@inject
def main(container: Container = Provide[Container]):
    # main 함수 내에서 database_url을 직접 지정합니다.
    database_url = "your-database-url-here"

    service = container.service(database_url=database_url)
    # ... 나머지 코드 ...

    print(f"type container.service : {type(container.service)}")
    print(f"type service : {type(service)}")

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    main()
