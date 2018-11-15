from api_general import Api_general
from api_vims import Api_vims
from test import Api_test
import json
import requests

# main function
if __name__ == '__main__':
    api = Api_general(target="dev")
    api_vims = Api_vims(target="dev")
    test = Api_test()
    # print("---------------------------------------------------")
    # print("API return format testing:")
    # for api_url in api.api_dict:
    #     test.test_api_all_return_format(api_url, api.api_dict)
    print("---------------------------------------------------")
    print("VIMS downlink testing:")

    for primary_filespec in api_vims.api_dict:
        test.test_api_compare_vims_downlinks_for_v1_and_v2(primary_filespec, api_vims.api_dict)




# print(res.url)
# print(res.status_code)
# print(res.raise_for_status())
# print(res.text)
# print(res)
# print(res.json())
# print(res.json()["data"])
# print(res.json()["data"][0]["result_count"] == 1525767)
# print(res)
