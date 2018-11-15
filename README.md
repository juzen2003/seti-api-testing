## API testing notes

* Make sure all supported return formats are valid (Issue #377)
  * json
  * html
  * zip
  * csv
* Test of VIMS products returned for observations with multiple downlink numbers (Issue #482)

### Setup
* virtualenv venv
* source venv/bin/activate
* pip3 install requests

### Reference
* usage of request: http://docs.python-requests.org/en/master/user/quickstart/
* response object: http://docs.python-requests.org/en/v1.0.0/api/
