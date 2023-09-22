from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient
from faker import Faker

fake = Faker()

def generate_dummy_data(schema):
    data = {}
    for prop, details in schema['properties'].items():
        data_type = details.get('type', '')
        if data_type == 'string':
            data[prop] = fake.name()
        elif data_type == 'integer':
            data[prop] = fake.random_int(min=0, max=9999)
        elif data_type == 'boolean':
            data[prop] = fake.boolean()
        # 여기에 더 많은 데이터 타입을 추가할 수 있습니다.
    return data

def post_data_using_bravado(api_spec_url, operation_id):
    http_client = RequestsClient()
    swagger_client = SwaggerClient.from_url(
        api_spec_url,
        http_client=http_client,
        config={'validate_responses': False, 'validate_requests': False, 'validate_swagger_spec': False}
    )

    service = swagger_client.get_service(operation_id)
    schema = swagger_client.spec_dict['paths'][operation_id.split('.')[0]]['post']['requestBody']['content']['application/json']['schema']

    dummy_data = generate_dummy_data(schema)
    print(f"Generated Dummy Data: {dummy_data}")

    request_future = service(body=dummy_data)
    
    try:
        response = request_future.result()
        print(f'Successfully posted data: {response}')
    except Exception as e:
        print(f'Failed to post data: {e}')

if __name__ == "__main__":
    api_spec_url = "https://petstore.swagger.io/v2/swagger.json"
    operation_id = 'addPet'  # OpenAPI 스펙에서 해당 엔드포인트의 operationId 값을 확인하세요.

    post_data_using_bravado(api_spec_url, operation_id)
