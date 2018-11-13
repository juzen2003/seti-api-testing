from api import Api
from test import Test
import json
import requests


# main function
if __name__ == '__main__':
    api = Api(target="dev")
    test = Test()
    for api_url in api.api_dict:
        test.test_api_return_format(api_url, api.api_dict)



# print(res.url)
# print(res.status_code)
# print(res.raise_for_status())
# print(res.text)
# print(res)
# print(res.json())

# print(res.json()["data"])
# print(res.json()["data"][0]["result_count"] == 1525767)
# print(res)
