import requests
import allure
from endpoints.base_endopoint import BaseEndpoint
from endpoints.json_shemas import PayloadModel

PAYLOAD = {
    "name": "name",
    "data": {
        "year": 2022,
        "price": 1883,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
    }
}


class CreateObject(BaseEndpoint):
    response_data = None

    @allure.step("Send POST request and validate response")
    def create_new_object(self, payload=None):
        payload = payload if payload else PAYLOAD
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.status_code = self.response.status_code
        self.response_js = self.response.json()
        self.response_data = PayloadModel(**self.response.json())

    @allure.step("Check name is correct")
    def check_name_is(self, name):
        assert self.response_data.name == name

