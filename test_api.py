import json
import requests

file_format = ["json", "html","zip", "csv"]
# api_url_base = "https://tools.pds-rings.seti.org/opus/api/meta/result_count.%s" %(file_format)
api_url_base = "https://tools.pds-rings.seti.org/opus/api/meta/result_count."
payload = {'planet': 'Saturn', 'target': 'Pluto'} # slugs
# print(api_url_base)

for format in file_format:
    api = api_url_base + format
    res = requests.get(api, params=payload);
    http_status_code = res.status_code
    # print(http_status_code)
    print(res.url)

    if http_status_code == 200:
        print("Response ok, http status code: %s" %(http_status_code))
    elif http_status_code >= 400 and http_status_code < 500:
        print("Bad request, http status code: %s" %(http_status_code))
    elif http_status_code >= 500:
        print("Server error, http status code: %s" %(http_status_code))
    else:
        print("Error, http status code: %s" %(http_status_code))

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
