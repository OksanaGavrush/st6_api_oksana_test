import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.put_object import PuttObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def post_id():
    create_publication = CreateObject()
    create_publication.create_new_object()
    post_id = create_publication.response.json()['id']
    yield post_id
    obj = DeleteObject()
    obj.delete_object(post_id=post_id)



