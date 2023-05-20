import json
import allure

from utilities.api import Google_maps_api
from utilities.checking import Checking

"""Creation, update and deletion of new location"""
@allure.epic("Test create place")
class Test_create_place:

    @allure.description("Test creation, update and deletion of new location")
    def test_create_new_place(self):

        print("Method POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        print(f"Current status code: {result_post.status_code}")
        Checking.check_status_code(result_post, 200)
        token = json.loads(result_post.text)
        print(f"Mandatory fields: {list(token)}")
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')


        print("Method GET POST")
        result_get = Google_maps_api.get_new_place(place_id)
        print(f"Current status code: {result_get.status_code}")
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(f"Mandatory fields: {list(token)}")
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Method PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        print(f"Current status code: {result_put.status_code}")
        Checking.check_status_code(result_put, 200)
        token = json.loads(result_put.text)
        print(f"Mandatory field: {list(token)}")
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Method GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        print(f"Current status code: {result_get.status_code}")
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(f"Mandatory fields: {list(token)}")
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Method DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        print(f"Current status code: {result_delete.status_code}")
        Checking.check_status_code(result_delete, 200)
        token = json.loads(result_delete.text)
        print(f"Mandatory field: {list(token)}")
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Method GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        print(f"Current status code: {result_get.status_code}")
        Checking.check_status_code(result_get, 404)
        token = json.loads(result_get.text)
        print(f"Mandatory field: {list(token)}")
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("Creation, update and deletion of new location has been successfully tested")