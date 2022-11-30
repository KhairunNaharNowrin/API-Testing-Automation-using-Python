import json

import pytest as pytest
import requests as requests

from config import BASE_URI


def create_user():
    url = f'{BASE_URI}/api/people'

    headers = {'Content-Type': 'application/json'}

    payload = {
        "name": "morpheus",
        "job": "zion resident",
        "updatedAt": "2022-11-30T09:39:23.737Z"
    }

    res = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    json_response = res.json()
    user_id = json_response['id']
    return user_id


class TestUpdateUser:

    @pytest.mark.positive
    def test_update_user(self):
        user_id = create_user()
        url = f'{BASE_URI}/api/users/{user_id}'

        headers = {'Content-Type': 'application/json'}

        payload = {
                "name": "morpheus",
                "job": "zion resident",
                "updatedAt": "2022-11-30T09:39:23.737Z"
        }

        res = requests.put(url, headers=headers, data=json.dumps(payload, indent=4))
        assert res.status_code == 200, "Check status code"
        print(res.json())



