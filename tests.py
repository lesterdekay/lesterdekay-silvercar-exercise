from api.endpoints import Users
from nose.tools import assert_true, assert_false
from json import loads

# Mock testing using the stub implementation is enabled by default using this global.
# Any test can be switched to using the live endpoint by changing the parameter to mock=False
MOCK = True


def test_existing_user_get_status_code():
    status_code = Users().get_status_code('lesterdekay', mock=MOCK)
    assert_true(status_code == 200)


def test_nonexisting_user_get_status_code():
    status_code = Users().get_status_code('lester_dekay', mock=MOCK)
    assert_true(status_code == 404)


def test_existing_users_get_text():
    text = Users().get_response_text('lesterdekay', mock=MOCK)
    resp = loads(text)
    # There are many fields in the response, but for the sake of this exercise I am only going to
    # validate a handful
    following = resp.get('following')
    login = resp.get('login')
    type = resp.get('type')
    bio = resp.get('bio')
    organizations_url = resp.get('organizations_url')
    assert_true(following == 0)
    assert_true(login == 'lesterdekay')
    assert_true(type == 'User')
    assert_false(bio)
    assert_true(organizations_url == 'https://api.github.com/users/lesterdekay/orgs')


def test_nonexisting_users_get_text():
    text = Users().get_response_text('lester_dekay', mock=MOCK)
    resp = loads(text)
    message = resp.get('message')
    documentation_url = resp.get('documentation_url')
    assert_true(message == 'Not Found')
    assert_true(documentation_url == 'https://developer.github.com/v3/users/#get-a-single-user')


