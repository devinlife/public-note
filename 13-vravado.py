from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient


def post_data_using_bravado(api_url, api_spec_url, operation_id, payload):
    http_client = RequestsClient()


api_spec_url = "https://petstore.swagger.io/v2/swagger.json"

http_client = RequestsClient()
swagger_client = SwaggerClient.from_url(
    f"{api_spec_url}",
    http_client=http_client,
    config={"validate_responses": False, "validate_requests": False, "validate_swagger_spec": False},
)


# print(dir(swagger_client.pet))

operation_id = "updatePet"
payload = {"id": 42, "name": "tommy", "category": "Category(id=24)"}


# Operation ID는 Swagger/OpenAPI 스펙에서 해당 API 엔드포인트의 'operationId'에 해당합니다.


service = swagger_client.get("pet")

request_future = service(body=payload)


client = SwaggerClient.from_url("https://petstore.swagger.io/v2/swagger.json")
pet = client.pet.getPetById(petId=24364310).response().result
print(pet)


Pet = client.get_model("Pet")
Category = client.get_model("Category")
pet = Pet(id=42, name="tommy", category=Category(id=24))
client.pet.addPet(body=pet).response().result
