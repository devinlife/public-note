from bravado.client import SwaggerClient

client = SwaggerClient.from_url(
    "https://petstore.swagger.io/v2/swagger.json",
    config={"validate_responses": False, "validate_requests": False, "validate_swagger_spec": False},
)
print(f"client = {client}")
print(f"dir client = {dir(client)}")

print(f"client = {client.pet.getPetById.operation}")
print(f"client = {client.pet.getPetById.operation.swagger_spec}")

swagger_spec = client.pet.getPetById.operation.swagger_spec
schema = swagger_spec.spec_dict['paths'][.split('.')[0]]




schema = client.pet["getPetById".split('.')[0]]['post']['requestBody']['content']['application/json']['schema']
print(f"schema = {schema}")


print(f"client swagger_spec = {client.swagger_spec}")
print(f"type client.pet.getPetById= {client.pet.getPetById}")
pet = client.pet.getPetById(petId=24364310).response().result
print(f"pet = {pet}")

# Pet = client.get_model("Pet")
# Category = client.get_model("Category")
# pet = Pet(id=42, name="tommy", photoUrls=["www.google.com"], category=Category(id=24))
# ret = client.pet.addPet(body=pet)
# print(ret.result())
