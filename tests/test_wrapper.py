from pytest import raises
from src.igdb.wrapper import IGDBWrapper

def test_stores_user_key():
    wrapper = IGDBWrapper('test')
    assert hasattr(wrapper, 'user_key')
    assert wrapper.user_key == 'test'

def test_composes_query():
    wrapper = IGDBWrapper('test')
    assert IGDBWrapper._build_url('dummy') == 'https://api-v3.igdb.com/dummy'
    assert wrapper._compose_request('fields test,test2,test3; offset 2') == {
        'data': 'fields test,test2,test3; offset 2',
        'headers': {
            'user-key': 'test'
        }
    }

def test_raises_when_query_bad():
    wrapper = IGDBWrapper('')
    with raises(Exception) as exc:
        wrapper._compose_request()
        assert exc.type is Exception
        assert exc.value.args[0] == 'No query provided!\nEither provide an inline query following Apicalypse\'s syntax or an Apicalypse object'

    with raises(TypeError) as exc:
        wrapper._compose_request(11)
        assert exc.type is TypeError
        assert exc.value.args[0] == 'Incorrect type of argument \'query\', only Apicalypse-like strings or Apicalypse objects are allowed'
