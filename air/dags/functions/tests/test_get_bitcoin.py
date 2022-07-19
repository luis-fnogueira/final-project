import pytest
from unittest.mock import patch
from unittest import TestCase
import sys
import requests


# Appending our folder with functions
sys.path.append('air/dags/functions')
from get_bitcoin import GetResponse


@pytest.fixture()
# @patch("air.dags.functions.get_bitcoin.GetResponse.getDeserialize", set())
def fixture_get_deserialize():
    response = GetResponse()
    return response.getDeserialize("valid_endpoint")


def mocked_requests_get(*args, **kwargs):
    class MockResponse(requests.Response):
        def __init__(self, json_data, status_code):
            super().__init__()
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

        def raise_for_status(self) -> None:
            if self.status_code != 200:
                raise Exception

    if args[0] == "valid_endpoint":
        return MockResponse(json_data={"foo": "bar"}, status_code=200)
    else:
        return MockResponse(json_data=None, status_code=404)


class TestGetResponse(TestCase):

    @patch("get_bitcoin.GetResponse.getDeserialize", side_effect=mocked_requests_get)
    def testGetDeserialize(self, mock_getDeserialize):

        get_response = GetResponse()
        response = get_response.getDeserialize("valid_endpoint")
        
        response_json = response.json()
        
        assert response_json == {'foo':'bar'}