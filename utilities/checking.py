"""Methods for checking responses"""
import json


class Checking:

    """Method for checking status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print(f"Status code {result.status_code} is correct.")


    """Method for checking response mandatory fields"""
    @staticmethod
    def check_json_token(result, expected_field):
        token = json.loads(result.text)
        assert list(token) == expected_field
        print("All mandatory fields are present")


    """Method for checking response mandatory fields value"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        value = result.json()
        value_info = value.get(field_name)
        assert value_info == expected_value
        print(f"Field name '{field_name}' is correct")
        print(f"Expected value '{expected_value}' is correct too")
