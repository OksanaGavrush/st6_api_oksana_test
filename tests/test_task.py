import pytest
import allure
from tests.base_tests import BaseTest


class TestMethod(BaseTest):

    @allure.feature("Create Object")
    @allure.story("Post Request to Create an Object")
    @allure.title("Test Create Object with POST Request")
    def test_create_object(self):
        payload = {
            "name": "Apple MacBook 22",
            "data": {
                "year": 2022,
                "price": 1883,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
            }
        }
        self.create_endpoint.create_new_object(payload)
        self.create_endpoint.check_response_is_200()
        self.create_endpoint.check_name_is(name=payload['name'])

    @allure.feature("Get Object")
    @allure.story("Get Request to Retrieve Object by ID")
    @allure.title("Test Update Object by ID with PUT Request")
    @pytest.mark.critical
    def test_get_object_by_id(self, post_id):
        self.get_endpoint.get_by_id(post_id)
        self.get_endpoint.check_response_is_200()
        self.get_endpoint.check_id_is_correct(post_id)

    @allure.feature("Update Object")
    @allure.story("Put Request to Update an Object by ID")
    @pytest.mark.parametrize('name', ['Apple MacBook Pro 16', 88], ids=['string', 'int'])
    def test_put_object_by_id(self, name, post_id):
        payload = {
            "name": name,
            "data": {
                "year": 2024,
                "price": 1923,
                "CPU model": "Intel Core i11",
                "Hard disk size": "1.1 TB",
            }
        }
        self.put_endpoint.put_obj_by_id(post_id=post_id, payload=payload)
        self.put_endpoint.check_name_is(name=payload['name'])
        self.put_endpoint.check_response_is_200()

    @allure.feature("Modify Object")
    @allure.story("Patch Request to Modify an Object by ID")
    @pytest.mark.medium
    def test_patch_object_by_id(self, post_id):
        payload = {
            "name": "Samsung"
        }

        self.patch_endpoint.patch_obj_by_id(post_id=post_id, payload=payload)
        self.patch_endpoint.validate_patch_response(expected_name=payload['name'])
        self.patch_endpoint.check_response_is_200()

    @allure.feature("Delete Object")
    @allure.story("Delete Request to Remove an Object by ID")
    @allure.title("Test Delete Object by ID with DELETE Request")
    def test_delete_post(self, post_id):
        self.delete_endpoint.delete_object(post_id)
        self.delete_endpoint.check_response_is_200()
        self.get_endpoint.get_by_id(post_id)
        self.get_endpoint.check_response_is_404()


