import json
import requests

api_base = "https://tools.pds-rings.seti.org/opus/api/"
file_format = ["json", "html","zip", "csv"]

# Getting Data
# api/data.[fmt]
api_data_base = api_base + "data."
# api/metadata/[opus_id].[fmt]
api_metadata_base = api_base + "metadata/VGISS_7204-C26548XX-C2654853." # use VGISS_7204-C26548XX-C2654853"
# api/metadata_v2/[opus_id].[fmt]
api_metadata_v2_base = api_base + "metadata_v2/VGISS_7204-C26548XX-C2654853."
# api/images/[size].[fmt]
api_images_size_base = api_base + "images/thumb."
# api/images.[fmt]
api_images_base = api_base + "images."
# api/image/[size]/[opus_id].[fmt]
api_images_with_opus_id_base = api_base + "image/full/HSTU0_7717-V03-U4YM0303R." # use HSTU0_7717-V03-U4YM0303R
# api/files/[opus_id].[fmt]
api_files_with_opus_id_base = api_base + "files/NHJULO_x001-20070115_003120-lor_0031203239_0x630."
# api/files.[fmt]
api_all_files_base = api_base + "files."

# Getting Information about Data
# api/meta/result_count.[fmt]
api_count_base = api_base + "meta/result_count."
# api/meta/mults/[param].[fmt]
api_mults_base = api_base + "meta/mults/mission." # use mission
# api/meta/range/endpoints/[param].[fmt]
api_endpoints_base = api_base + "meta/range/endpoints/wavelength1." # use wavelength1
# api/categories/[opus_id].json
api_categories_with_opus_id_base = api_base + "categories/HSTU0_7717-V03-U4YM0303R." # use HSTU0_7717-V03-U4YM0303R
# api/categories.json
api_all_categories_base = api_base + "categories."
# api/fields/[field].[fmt]
api_fields_base = api_base + "fields/mission." # use mission
# api/fields.[fmt]
api_all_fields_base = api_base + "fields."

# slugs for testing
payload1 = {"planet": "Saturn", "target": "Pluto", "limit": 5}
payload2 = {"planet": "Earth", "target": "Pluto", "mission": "Hubble", "limit": 5}
payload3 = {"planet": "Earth", "target": "Moon", "limit": 5}
payload4 = {"planet": "Earth", "target": "Moon", "mission": "Cassini", "limit": 5}
payload5 = {"planet": "Mars", "target": "Mars", "instrument": "Hubble WFC3", "limit": 5} # Hubble+WFC3
payload6 = {"cats": "PDS Constraints"}
payload7 = {"planet": "Jupiter", "limit": 5}

# dictionary to store testing api & payload for each testing case
api_dict = {
    api_data_base: {
        "api": "api/data.[fmt]",
        "payload": payload5,
        "support": ["json", "html", "zip", "csv"]
    },
    api_metadata_base: {
        "api": "api/metadata/[opus_id].[fmt]",
        "payload": payload6,
        "support": ["json", "html", "zip", "csv"]
    },
    api_metadata_v2_base: {
        "api": "api/metadata_v2/[opus_id].[fmt]",
        "payload": payload6,
        "support": ["json", "html", "zip", "csv"]
    },
    api_images_size_base: {
        "api": "api/images/[size].[fmt]",
        "payload": payload7,
        "support": ["json", "html", "zip", "csv"]
    },
    api_images_base: {
        "api": "api/images.[fmt]",
        "payload": payload7,
        "support": ["json", "html", "zip", "csv"]
    },
    api_images_with_opus_id_base: {
        "api": "api/image/[size]/[opus_id].[fmt]",
        "payload": None,
        "support": ["json", "html", "zip", "csv"]
    },
    api_files_with_opus_id_base: {
        "api": "api/files/[opus_id].[fmt]",
        "payload": None,
        "support": ["json", "html", "zip", "csv"]
    },
    api_all_files_base: {
        "api": " api/files.[fmt]",
        "payload": payload7,
        "support": ["json", "html", "zip", "csv"]
    },
    api_count_base: {
        "api": "api/meta/result_count.[fmt]",
        "payload": payload1,
        "support": ["json", "html", "zip"]
    },
    api_mults_base: {
        "api": "api/meta/mults/[param].[fmt]",
        "payload": payload2,
        "support": ["json", "html", "zip"]
    },
    api_endpoints_base: {
        "api": "api/meta/range/endpoints/[param].[fmt]",
        "payload": payload3,
        "support": ["json", "html", "zip", "csv"]
    },
    api_categories_with_opus_id_base: {
        "api": "api/categories/[opus_id].json",
        "payload": None,
        "support": ["json"]
    },
    api_all_categories_base: {
        "api": "api/categories.json",
        "payload": payload4,
        "support": ["json"]
    },
    api_fields_base: {
        "api": "api/fields/[field].[fmt]",
        "payload": None,
        "support": ["json", "html", "zip"]
    },
    api_all_fields_base: {
        "api": "api/fields.[fmt]",
        "payload": None,
        "support": ["json", "html", "zip"]
    },
}

def test_api_return_format(api_url_base):
    print("---------------------------------------------------")
    print("Testing API: %s" %(api_dict[api_url_base]["api"]))
    actual_supported_format = []

    for format in file_format:
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


# main function
if __name__ == '__main__':
    for api in api_dict:
        test_api_return_format(api)
    # test_api_return_format(api_data_base)
    # test_api_return_format(api_metadata_base)
    # test_api_return_format(api_metadata_v2_base)
    # test_api_return_format(api_images_size_base)
    # test_api_return_format(api_images_base)
    # test_api_return_format(api_images_with_opus_id_base)
    # test_api_return_format(api_files_with_opus_id_base)
    # test_api_return_format(api_all_files_base)
    # test_api_return_format(api_count_base)
    # test_api_return_format(api_mults_base)
    # test_api_return_format(api_endpoints_base)
    # test_api_return_format(api_categories_with_opus_id_base)
    # test_api_return_format(api_all_categories_base)
    # test_api_return_format(api_fields_base)
    # test_api_return_format(api_all_fields_base)

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
