from api import Api
import json
import requests

class Test:
    file_format = ["json", "html","zip", "csv"]

    def __init__(self):
        pass

    # test all return format for one api call (api url: api_url_base)
    def test_api_return_format(self, api_url_base, api_dict):
        print("---------------------------------------------------")
        print("Testing API: %s" %(api_dict[api_url_base]["api"]))
        actual_supported_format = []

        for format in Test.file_format:
            api = api_url_base + format
            payload = api_dict[api_url_base]["payload"]
            res = requests.get(api, params=payload);
            http_status_code = res.status_code
            # print(res.url)
            if(format == "json"):
                print("Testing case: %s" %(res.url.replace("json", "[fmt]")))

            if http_status_code == 200:
                print("%s: Response ok, http status code: %s" %(format, http_status_code))
                actual_supported_format.append(format)
            elif http_status_code == 404:
                print("%s: Page not found, http status code: %s" %(format, http_status_code))
            elif http_status_code >= 400 and http_status_code < 500:
                print("%s: Bad request, http status code: %s" %(format, http_status_code))
            elif http_status_code >= 500:
                print("%s: Server error, http status code: %s" %(format, http_status_code))
            else:
                print("%s: Error, http status code: %s" %(format, http_status_code))

        print("Supported format in doc: %s" %(api_dict[api_url_base]["support"]))
        print("Actual Supported format: %s" %(actual_supported_format))
