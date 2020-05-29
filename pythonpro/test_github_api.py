from unittest.mock import Mock

from pythonpro import github_api


# Teste unitário
def test_buscar_avatar_unitario():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'marvinsilva',
        'id': 45732834,
        'node_id': 'MDQ6VXNlcjQ1NzMyODM0',
        'avatar_ur': 'https://avatars1.githubusercontent.com/u/45732834?v=4',
        'url': 'https://api.github.com/users/marvinsilva',
        'html_url': 'https://github.com/marvinsilva',
        'followers_url': 'https://api.github.com/users/marvinsilva/followers',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('marvinsilva')
    assert 'https://avatars1.githubusercontent.com/u/45732834?v=4' == url


# Teste de integração dependente da rede e github server
def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('marvinsilva')
    assert 'https://avatars1.githubusercontent.com/u/45732834?v=4' == url
