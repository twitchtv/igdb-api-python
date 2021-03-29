from pytest import raises
from src.igdb.wrapper import IGDBWrapper

def test_stores_authentication():
    wrapper = IGDBWrapper('client', 'token')
    assert hasattr(wrapper, 'client_id')
    assert wrapper.client_id == 'client'
    assert hasattr(wrapper, 'auth_token')
    assert wrapper.auth_token == 'token'

def test_composes_query():
    wrapper = IGDBWrapper('client', 'token')
    assert IGDBWrapper._build_url('dummy') == 'https://api.igdb.com/v4/dummy'
    assert wrapper._compose_request('fields test,test2,test3; offset 2') == {
        'data': 'fields test,test2,test3; offset 2',
        'headers': {
            'Client-ID': 'client',
            'Authorization': 'Bearer token'
        }
    }

def test_raises_when_query_bad():
    wrapper = IGDBWrapper('', '')
    with raises(Exception) as exc:
        wrapper._compose_request()
        assert exc.type is Exception
        assert exc.value.args[0] == 'No query provided!\nEither provide an inline query following Apicalypse\'s syntax or an Apicalypse object'

    with raises(TypeError) as exc:
        wrapper._compose_request(11)
        assert exc.type is TypeError
        assert exc.value.args[0] == 'Incorrect type of argument \'query\', only Apicalypse-like strings or Apicalypse objects are allowed'
