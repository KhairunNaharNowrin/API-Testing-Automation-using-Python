import requests as requests


def test_get_user_list():
    url = "https://reqres.in/api/users"

    response = requests.get(url)

    print(response.text)

    # check response code
    code = response.status_code
    assert code == 200, "Code doesn't match"