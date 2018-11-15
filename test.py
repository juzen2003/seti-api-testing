import json
import requests
import re

class Api_test:
    file_format = ["json", "html","zip", "csv"]

    def __init__(self):
        pass

    # unit test: test return of single api call for ONE format (need to pass in format)
    # check see if the response is ok
    def test_api_single_return_format(self, api_url_base, api_dict, format):
        api = api_url_base + format
        payload = api_dict[api_url_base]["payload"]
        res = requests.get(api, params=payload);
        test_url = res.url
        http_status_code = res.status_code

        if http_status_code == 200:
            return (format, test_url)
        else:
            raise Exception("%s: Error, http status code: %s" %(format, http_status_code))

    # functional test: test return of one api call for all return formats (pass in api url: api_url_base)
    # flag error if any of documented formats is not supported
    def test_api_all_return_format(self, api_url_base, api_dict):
        testing_file_format = api_dict[api_url_base]["support"]
        actual_supported_format = []
        actual_test_url = None
        error_msg = []

        for format in testing_file_format:
            try:
                valid_return_format = self.test_api_single_return_format(api_url_base, api_dict, format)
                actual_supported_format.append(valid_return_format[0])
                if not actual_test_url:
                    actual_test_url = valid_return_format[1]
            except Exception as error:
                error_msg.append(error)

        if error_msg:
            print("---------------------------------------------------")
            print("Return format error on: %s" %(api_dict[api_url_base]["api"]))
            print("Testing case: %s" %(actual_test_url))
            print("Supported format in doc: %s" %(api_dict[api_url_base]["support"]))
            print("Actual Supported format: %s" %(actual_supported_format))

    # unit test: collect all image counts for ONE primary filespec
    def test_api_collect_vims_image_numbers_for_single_primary_filespec(self, primary_filespec, api_dict):
        format = "json"
        primary_filespec_object = api_dict[primary_filespec]
        api = primary_filespec_object["url"] + format
        payload = primary_filespec_object["payload"]
        res = requests.get(api, params=payload);
        test_url = res.url
        http_status_code = res.status_code
        image_count = {}

        if http_status_code == 200:
            data_object = res.json()["data"]
            for id in primary_filespec_object["opus_id"]:
                image_count[id] = {
                    "browse-thumb": len(data_object[id]["browse-thumb"]),
                    "browse-small": len(data_object[id]["browse-small"]),
                    "browse-medium": len(data_object[id]["browse-medium"]),
                    "browse-full": len(data_object[id]["browse-full"]),
                    "covims-thumb": len(data_object[id]["covims-thumb"]),
                    "covims-medium": len(data_object[id]["covims-medium"]),
                    "covims-full": len(data_object[id]["covims-full"]),
                }
            return image_count
        else:
            raise Exception("%s: Error, http status code: %s" %(format, http_status_code))

    # functional test: check if 001 image numbers are larger than 002 image numbers
    # flag error if any image numbers from 001 is equal or less than ones in 002
    def test_api_compare_vims_downlinks_for_v1_and_v2(self, primary_filespec, api_dict):
        primary_filespec_object = api_dict[primary_filespec]
        image_count = {}
        error_msg = []

        try:
            image_count = self.test_api_collect_vims_image_numbers_for_single_primary_filespec(primary_filespec, api_dict)
        except Exception as error:
            error_msg.append(error)

        v1_ir = primary_filespec_object["opus_id"][0]
        v1_vis = primary_filespec_object["opus_id"][1]
        v2_ir = primary_filespec_object["opus_id"][2]
        v2_vis = primary_filespec_object["opus_id"][3]
        image_info = []
        if not error_msg:
            for image, count in image_count[v1_ir].items():
                if image_count[v2_ir][image] >= count:
                    error_msg.append("%s is missing downlinks for ir image: %s" %(v1_ir, image))
            for image, count in image_count[v1_vis].items():
                if image_count[v2_vis][image] >= count:
                    error_msg.append("%s is missing downlinks for vis image: %s" %(v1_vis, image))
        else:
            print(error_msg)

        if not error_msg:
            print("Check passed. Multiple VIMS downlinks for %s & %s are available." %(v1_ir, v1_vis))
        else:
            print(error_msg)



    # print out all response code, for debugging purpose
    # def debug_api_return_format(self, api_url_base, api_dict):
    #     print("---------------------------------------------------")
    #     print("Testing API: %s" %(api_dict[api_url_base]["api"]))
    #     actual_supported_format = []
    #
    #     for format in Api_test.file_format:
    #         api = api_url_base + format
    #         payload = api_dict[api_url_base]["payload"]
    #         res = requests.get(api, params=payload);
    #         http_status_code = res.status_code
    #         # print(res.url)
    #         if(format == "json"):
    #             print("Testing case: %s" %(res.url.replace("json", "[fmt]")))
    #
    #         if http_status_code == 200:
    #             print("%s: Response ok, http status code: %s" %(format, http_status_code))
    #             actual_supported_format.append(format)
    #         elif http_status_code == 404:
    #             print("%s: Page not found, http status code: %s" %(format, http_status_code))
    #         elif http_status_code >= 400 and http_status_code < 500:
    #             print("%s: Bad request, http status code: %s" %(format, http_status_code))
    #         elif http_status_code >= 500:
    #             print("%s: Server error, http status code: %s" %(format, http_status_code))
    #         else:
    #             print("%s: Error, http status code: %s" %(format, http_status_code))
    #
    #     print("Supported format in doc: %s" %(api_dict[api_url_base]["support"]))
    #     print("Actual Supported format: %s" %(actual_supported_format))
