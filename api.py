# This class is to build up testing APIs for either production or dev sites
class Api:
    # slugs for testing
    payload1 = {"planet": "Saturn", "target": "Pluto", "limit": 2}
    payload2 = {"planet": "Earth", "target": "Moon", "mission": "Hubble", "limit": 2}
    payload3 = {"planet": "Earth", "target": "Moon", "limit": 2}
    payload4 = {"planet": "Earth", "target": "Moon", "mission": "Hubble", "limit": 2}
    payload5 = {"planet": "Mars", "target": "Mars", "instrument": "Hubble WFC3", "limit": 2} # Hubble+WFC3
    payload6 = {"cats": "PDS Constraints"}
    payload7 = {"planet": "Jupiter", "limit": 2}

    def __init__(self, target="production"):
        self.target = target
        self.build_all_testing_api()

    def build_all_testing_api(self):
        self.api_base = self.build_api_base()
        self.api_data_base = self.build_api_data_base()
        self.api_metadata_base = self.build_api_metadata_base()
        self.api_metadata_v2_base = self.build_api_metadata_v2_base()
        self.api_images_size_base = self.build_api_images_size_base()
        self.api_images_base = self.build_api_images_base()
        self.api_images_with_opus_id_base = self.build_api_images_with_opus_id_base()
        self.api_files_with_opus_id_base = self.build_api_files_with_opus_id_base()
        self.api_all_files_base = self.build_api_all_files_base()
        self.api_count_base = self.build_api_count_base()
        self.api_mults_base = self.build_api_mults_base()
        self.api_endpoints_base = self.build_api_endpoints_base()
        self.api_categories_with_opus_id_base = self.build_api_categories_with_opus_id_base()
        self.api_all_categories_base = self.build_api_all_categories_base()
        self.api_fields_base = self.build_api_fields_base()
        self.api_all_fields_base = self.build_api_all_fields_base()
        self.api_dict = self.build_api_dict()

    def build_api_base(self):
        if self.target == "production":
            return "https://tools.pds-rings.seti.org/opus/api/"
        elif self.target == "dev":
            return "http://dev.pds-rings.seti.org/opus/api/"

    # Getting Data
    # api/data.[fmt]
    def build_api_data_base(self):
        return self.api_base + "data."

    # api/metadata/[opus_id].[fmt]
    def build_api_metadata_base(self):
        if self.target == "production":
            return self.api_base + "metadata/VGISS_7204-C26548XX-C2654853."
        elif self.target == "dev":
            return self.api_base + "metadata/vg-iss-1-j-c1466833."

    # api/metadata_v2/[opus_id].[fmt]
    def build_api_metadata_v2_base(self):
        if self.target == "production":
            return self.api_base + "metadata_v2/VGISS_7204-C26548XX-C2654853."
        elif self.target == "dev":
            return self.api_base + "metadata_v2/hst-07717-wfpc2-u4ym0302."

    # api/images/[size].[fmt]
    def build_api_images_size_base(self):
        return self.api_base + "images/thumb."

    # api/images.[fmt]
    def build_api_images_base(self):
        return self.api_base + "images."

    # api/image/[size]/[opus_id].[fmt]
    def build_api_images_with_opus_id_base(self):
        if self.target == "production":
            return self.api_base + "image/full/HSTU0_7717-V03-U4YM0303R."
        elif self.target == "dev":
            return self.api_base + "image/full/nh-lorri-lor_0235006328."

    # api/files/[opus_id].[fmt]
    def build_api_files_with_opus_id_base(self):
        if self.target == "production":
            return self.api_base + "files/NHJULO_x001-20070115_003120-lor_0031203239_0x630."
        elif self.target == "dev":
            return self.api_base + "files/hst-05836-wfpc2-u2tf0107."

    # api/files.[fmt]
    def build_api_all_files_base(self):
        return self.api_base + "files."

    # Getting Information about Data
    # api/meta/result_count.[fmt]
    def build_api_count_base(self):
        return self.api_base + "meta/result_count."

    # api/meta/mults/[param].[fmt]
    def build_api_mults_base(self):
        return self.api_base + "meta/mults/mission." # use mission

    # api/meta/range/endpoints/[param].[fmt]
    def build_api_endpoints_base(self):
        return self.api_base + "meta/range/endpoints/wavelength1." # use wavelength1

    # api/categories/[opus_id].json
    def build_api_categories_with_opus_id_base(self):
        if self.target == "production":
            return self.api_base + "categories/HSTU0_7717-V03-U4YM0303R."
        elif self.target == "dev":
            return self.api_base + "categories/hst-07717-wfpc2-u4ym0302."

    # api/categories.json
    def build_api_all_categories_base(self):
        return self.api_base + "categories."

    # api/fields/[field].[fmt]
    def build_api_fields_base(self):
        return self.api_base + "fields/mission." # use mission

    # api/fields.[fmt]
    def build_api_all_fields_base(self):
        return self.api_base + "fields."

    def build_api_dict(self):
        return {
            self.api_data_base: {
                "api": "api/data.[fmt]",
                "payload": Api.payload5,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_metadata_base: {
                "api": "api/metadata/[opus_id].[fmt]",
                "payload": Api.payload6,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_metadata_v2_base: {
                "api": "api/metadata_v2/[opus_id].[fmt]",
                "payload": Api.payload6,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_images_size_base: {
                "api": "api/images/[size].[fmt]",
                "payload": Api.payload7,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_images_base: {
                "api": "api/images.[fmt]",
                "payload": Api.payload7,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_images_with_opus_id_base: {
                "api": "api/image/[size]/[opus_id].[fmt]",
                "payload": None,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_files_with_opus_id_base: {
                "api": "api/files/[opus_id].[fmt]",
                "payload": None,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_all_files_base: {
                "api": "api/files.[fmt]",
                "payload": Api.payload7,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_count_base: {
                "api": "api/meta/result_count.[fmt]",
                "payload": Api.payload1,
                "support": ["json", "html", "zip"]
            },
            self.api_mults_base: {
                "api": "api/meta/mults/[param].[fmt]",
                "payload": Api.payload2,
                "support": ["json", "html", "zip"]
            },
            self.api_endpoints_base: {
                "api": "api/meta/range/endpoints/[param].[fmt]",
                "payload": Api.payload3,
                "support": ["json", "html", "zip", "csv"]
            },
            self.api_categories_with_opus_id_base: {
                "api": "api/categories/[opus_id].json",
                "payload": None,
                "support": ["json"]
            },
            self.api_all_categories_base: {
                "api": "api/categories.json",
                "payload": Api.payload4,
                "support": ["json"]
            },
            self.api_fields_base: {
                "api": "api/fields/[field].[fmt]",
                "payload": None,
                "support": ["json", "html", "zip"]
            },
            self.api_all_fields_base: {
                "api": "api/fields.[fmt]",
                "payload": None,
                "support": ["json", "html", "zip"]
            },
        }
