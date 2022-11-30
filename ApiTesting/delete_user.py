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


class TestDeleteUser:

    @pytest.mark.positive
    def test_delete_user(self):
        user_id = create_user()
        url = f'{BASE_URI}/api/users/{user_id}'

        res = requests.delete(url)
        print(url)
        assert res.status_code == 204, "Check status code"


