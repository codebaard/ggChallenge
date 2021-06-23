import requests
from app.model.Army import Army
import unittest

class apiHandlerTest(unittest.TestCase):

    def test_checkCorrectReturn(self):
        response = requests.get('https://gg.juliusneudecker.com/troops?size=3')
        testArmy = Army(3)
        testArmy.populate()

        assert response.status_code == 200
        assert response.headers['content-type'] == 'application/json'

        json = response.json()

        assert len(json) == 2
        assert json.get('total') == 3
        assert len(json.get('troops')) == 3
        assert json.get('troops')[0].get('count') == 1

    def test_checkBadRequst(self):
        response = requests.get('https://gg.juliusneudecker.com/troops?size=2')
        assert response.status_code == 400
        assert response.headers['content-type'] == 'application/json'

    def test_checkNotFound(self):
        response = requests.get('https://gg.juliusneudecker.com/test')
        assert response.status_code == 404
        assert response.headers['content-type'] == 'application/json'

if __name__ == '__main__':
    unittest.main()
