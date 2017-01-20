import requests
import json

# Para rodar os testes (pasta "freefairs"): pytest -s -vv feiraslivresapi/tests

def test_get_feira_from_api():
    response = requests.get('http://localhost:8000/feiras/3/')
    data = response.json()
    assert data['id'] == 3 and data['nome_feira'] == 'CONCORDIA' and data['registro'] == '4003-7'


numb = 0
def test_post_feira_on_api():
    headers = {'Content-Type': 'application/json'}
    feira = {'id': 0, 'longi': '', 'lat': '', 'setcens': '', 'areap': '',
             'coddist': 0, 'distrito': '', 'codsubpref': 0, 'subprefe': '',
             'regiao5': '', 'regiao8': '', 'nome_feira': '', 'registro': '',
             'logradouro': '', 'numero': 0, 'bairro': '', 'referencia': ''}
    response = requests.post('http://localhost:8000/feiras/',
                             data=json.dumps(feira), headers=headers)
    assert response.status_code == 201


def test_put_feira_on_api():
    headers = {'Content-Type': 'application/json'}
    feira = {'nome_feira': 'VILA CHAVES'}
    response = requests.put('http://localhost:8000/feiras/880/',
                            data=json.dumps(feira), headers=headers)
    assert response.status_code == 200


def test_patch_feira_on_api():
    headers = {'Content-Type': 'application/json'}
    feira = {'distrito': '99'}
    response = requests.patch('http://localhost:8000/feiras/880/',
                              data=json.dumps(feira), headers=headers)
    assert response.status_code == 200


def test_delete_feira_on_api():
    response = requests.delete('http://localhost:8000/feiras/891/')
    assert response.status_code == 204
