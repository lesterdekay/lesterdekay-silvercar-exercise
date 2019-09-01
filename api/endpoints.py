import requests
from api.constants import BASE_URL

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


class Users:
    endpoint = 'users/'

    def __init__(self):
        self.users_url = urljoin(BASE_URL, self.endpoint)

    def get(self, user):
        url = urljoin(self.users_url, user)
        return requests.get(url)

    def get_status_code(self, user, mock):
        if mock:
            return self.mock_get_status_code(user)
        else:
            return self.get(user).status_code

    def mock_get_status_code(self, user):
        if user == 'lesterdekay':
            return 200
        elif user == 'lester_dekay':
            return 404

    def get_response_text(self, user, mock):
        if mock:
            return self.mock_get_response_text(user)
        else:
            return self.get(user).text

    def mock_get_response_text(self, user):
        if user == 'lesterdekay':
            return '{"login":"lesterdekay","id":1817065,"node_id":"MDQ6VXNlcjE4MTcwNjU=","avatar_url":"https://avatars0.githubusercontent.com/u/1817065?v=4","gravatar_id":"","url":"https://api.github.com/users/lesterdekay","html_url":"https://github.com/lesterdekay","followers_url":"https://api.github.com/users/lesterdekay/followers","following_url":"https://api.github.com/users/lesterdekay/following{/other_user}","gists_url":"https://api.github.com/users/lesterdekay/gists{/gist_id}","starred_url":"https://api.github.com/users/lesterdekay/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lesterdekay/subscriptions","organizations_url":"https://api.github.com/users/lesterdekay/orgs","repos_url":"https://api.github.com/users/lesterdekay/repos","events_url":"https://api.github.com/users/lesterdekay/events{/privacy}","received_events_url":"https://api.github.com/users/lesterdekay/received_events","type":"User","site_admin":false,"name":null,"company":null,"blog":"","location":null,"email":null,"hireable":null,"bio":null,"public_repos":1,"public_gists":3,"followers":0,"following":0,"created_at":"2012-06-04T21:48:55Z","updated_at":"2016-02-27T02:23:58Z"}'
        elif user == 'lester_dekay':
            return '{"message":"Not Found","documentation_url":"https://developer.github.com/v3/users/#get-a-single-user"}'
