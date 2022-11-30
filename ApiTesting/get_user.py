import pytest as pytest
import requests as requests

from config import BASE_URI


class TestGetUserList:

    @pytest.mark.positive
    def test_get_user_list(self):
        url =f'{BASE_URI}/api/people'

        res = requests.get(url)
        print(res.json())

        assert res.status_code == 200, "Check status code"
        print(res.json())



