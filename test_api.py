import json
import requests

file_format = ["json", "html","zip", "csv"]
# slugs
payload1 = {"planet": "Saturn", "target": "Pluto"}
payload2 = {"planet": "Earth", "target": "Pluto", "mission": "Hubble"}
payload3 = {"planet": "Earth", "target": "Moon"}

# Getting Information about Data
# api/meta/result_count.[fmt]
api_count_base = "https://tools.pds-rings.seti.org/opus/api/meta/result_count."
# api/meta/mults/[param].[fmt]
api_mults_base = "https://tools.pds-rings.seti.org/opus/api/meta/mults/mission." #for now we use mission
# api/meta/range/endpoints/[param].[fmt]
api_endpoints_base = "https://tools.pds-rings.seti.org/opus/api/meta/range/endpoints/wavelength1." #for now we use wavelength1


def test_api_return_format(api_url_base, payload):
    print("Testing API: %s" %(api_url_base) + "[fmt]")
    for format in file_format:
        api = api_url_base + format
        res = requests.get(api, params=payload);
        http_status_code = res.status_code

        if http_status_code == 200:
            print("%s: Response ok, http status code: %s" %(format, http_status_code))
        elif http_status_code >= 400 and http_status_code < 500:
            print("%s: Bad request, http status code: %s" %(format, http_status_code))
        elif http_status_code >= 500:
            print("%s: Server error, http status code: %s" %(format, http_status_code))
        else:
            print("%s: Error, http status code: %s" %(format, http_status_code))



# main function
if __name__ == '__main__':
    test_api_return_format(api_count_base, payload1)
    test_api_return_format(api_mults_base, payload2)
    test_api_return_format(api_endpoints_base, payload3)

    # try:
    #     res.raise_for_status()
    # except:
    #     raise Exception("Error, http status code %s" %(res.status_code))



# print(res.url)
# print(res.status_code)
# print(res.raise_for_status())
# print(res.text)
# print(res)
# print(res.json())

# print(res.json()["data"])
# print(res.json()["data"][0]["result_count"] == 1525767)
# print(res)
