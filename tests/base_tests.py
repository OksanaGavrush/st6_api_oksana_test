from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.put_object import PuttObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject


class BaseTest:
    create_endpoint = None
    get_endpoint = None
    put_endpoint = None
    patch_endpoint = None
    delete_endpoint = None

    def setup_method(self):
        self.create_endpoint = CreateObject()
        self.get_endpoint = GetObject()
        self.put_endpoint = PuttObject()
        self.patch_endpoint = PatchObject()
        self.delete_endpoint = DeleteObject()
