import json

import pytest as pytest
import requests as requests

from config import BASE_URI


class TestCreateUser:

    @pytest.mark.positive
    def test_create_user(self):
        url =f'{BASE_URI}/api/people'

        headers = {'Content-Type': 'application/json'}

        payload = {
                "name": "morpheus",
                "job": "zion resident",
                "updatedAt": "2022-11-30T09:39:23.737Z"
        }

        res = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
        assert res.status_code == 201, "Check status code"
        print(res.json())



