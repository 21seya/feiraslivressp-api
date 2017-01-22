## API usando Python 3.5 e Django Rest Framework para CRUD básico de Feiras Livres de São Paulo

Antes de começar, é necessário a criação e ativação de uma VirtualEnv com Python 3.5, para isso recomendo pyenv.
Após isso, vá para a pasta raiz desse projeto (feiraslivressp-api) e siga as instruções abaixo.

1) Instale os requisitos do projeto

    ```
    $ pip install -r requirements.txt
    ```

2) Faça a migração e suba a aplicação (para que possa importar os dados via API REST no próximo passo)

    ```
    $ python feiraslivresapi/manage.py migrate
    $ python feiraslivresapi/manage.py runserver &
    ```

3) Para importar os dados do CSV, execute o seguinte comando e este irá fazer uso da API para inserir os dados no SQLite3

    ```
    $ python import_data.py DEINFO_AB_FEIRASLIVRES_2014.csv
    ```

    NOTA: O Log de importação está em ```import_data.log```


# Testando com curl:

(NOTA: Uma alternativa ao curl é a UI Web para interagir com a API via browser, que é habilitada automaticamente pelo django-rest-framework. É possível fazer todas as requisições - GET, POST, PUT, PATCH e DELETE, acessando a seguinte URL: ``` http://localhost:8000/ ``` . Basta ir navegando pelos links dos recursos.)


- Retorna todas as Feiras, também é possível realizar paginação com limit e offset

    ```
    $ curl -iX GET http://localhost:8000/feiras/
    $ curl -X GET http://localhost:8000/feiras/ | python -m json.tool # pretty view
    $ curl -X GET http://localhost:8000/feiras/?limit=10&offset=10
    ```

    ```
    [
        {
            "id": 1,
            "longi": "-46550164",
            "lat": "-23558733",
            "setcens": "355030885000091",
            "areap": "3550308005040",
            "coddist": 87,
            "distrito": "VILA FORMOSA",
            "codsubpref": 26,
            "subprefe": "ARICANDUVA-FORMOSA-CARRAO",
            "regiao5": "Leste",
            "regiao8": "Leste 1",
            "nome_feira": "VILA FORMOSA",
            "registro": "4041-0",
            "logradouro": "RUA MARAGOJIPE",
            "numero": 0,
            "bairro": "VL FORMOSA",
            "referencia": "TV RUA PRETORIA"
        }
    ]
    ```

- Cadastra uma nova Feira

    ```
    $ curl -iX POST -H "Content-Type: application/json" -d '{"longi":"-46580164", "lat":"-23574733", "setcens":"355030885000000", "areap":"3550308004040", "coddist":"87", "distrito":"VILA FATIMA", "codsubpref":"26", "subprefe":"ARICANDUVA-FATIMA-CARRAO", "regiao5":"Leste", "regiao8":"Leste 1", "nome_feira":"VILA FATIMA", "registro":"4042-0", "logradouro":"RUA URUSSUI", "numero":"20", "bairro":"VL FATIMA", "referencia":"TV RUA PRETORIA"}' http://localhost:8000/feiras/
    ```

    ```
    HTTP/1.0 201 Created
    Date: Thu, 19 Jan 2017 13:22:55 GMT
    Server: WSGIServer/0.2 CPython/3.6.0
    Content-Type: application/json
    Allow: GET, OPTIONS, POST
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {"id":3,"longi":"-46580164","lat":"-23574733","setcens":"355030885000000","areap":"3550308004040","coddist":87,"distrito":"VILA FATIMA","codsubpref":26,"subprefe":"ARICANDUVA-FATIMA-CARRAO","regiao5":"Leste","regiao8":"Leste 1","nome_feira":"VILA FATIMA","registro":"4042-0","logradouro":"RUA URUSSUI","numero":20,"bairro":"VL FATIMA","referencia":"TV RUA PRETORIA"}
    ```

- Deleta uma Feira usando sua Primary Key

    ```
    $ curl -iX DELETE http://localhost:8000/feiras/3/
    ```

    ```
    HTTP/1.0 204 No Content
    Date: Thu, 19 Jan 2017 13:24:18 GMT
    Server: WSGIServer/0.2 CPython/3.6.0
    Allow: OPTIONS, GET, POST, PUT, DELETE
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN
    ```

- Altera os campos de uma feira já cadastrada, exceto a Primary Key

    ```
    $ curl -iX PUT -H "Content-Type: application/json" -d '{"nome_feira":"VILA CHAVES"}' http://localhost:8000/feiras/1/
    ```

    ```
    HTTP/1.0 200 OK
    Date: Thu, 19 Jan 2017 22:18:35 GMT
    Server: WSGIServer/0.2 CPython/3.6.0
    Content-Type: application/json
    Allow: OPTIONS, DELETE, PUT, POST, GET
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    {"id":1,"longi":"-46580163","lat":"-23574722","setcens":"355030885000000","areap":"3550308004040","coddist":87,"distrito":"VILA FATIMA","codsubpref":26,"subprefe":"ARICANDUVA-FATIMA-CARRAO","regiao5":"Leste","regiao8":"Leste 1","nome_feira":"VILA CHAVES","registro":"4042-0","logradouro":"RUA URUSSUI","numero":20,"bairro":"VL FATIMA","referencia":"TV RUA PRETORIA"}
    ```

- Procura por feiras usando qualquer um dos seguintes parâmetros (distrito, regiao5, nome_feira, bairro)

    ```
    $ curl -X GET http://localhost:8000/feiras/?distrito=otto | python -m json.tool
    ```

    ```
    [
        {
            "id": 3,
            "longi": "-46580164",
            "lat": "-23574733",
            "setcens": "355030885000000",
            "areap": "3550308004040",
            "coddist": 87,
            "distrito": "VILA OTTO",
            "codsubpref": 26,
            "subprefe": "ARICANDUVA-FATIMA-CARRAO",
            "regiao5": "Leste",
            "regiao8": "Leste 1",
            "nome_feira": "VILA FATIMA",
            "registro": "4042-0",
            "logradouro": "RUA PIZZA",
            "numero": 20,
            "bairro": "VL FATIMA",
            "referencia": "TV RUA PRETORIA"
        }
    ]
    ```

NOTA: A aplicação loga no arquivo feiraslivresapi/feiraslivresapi.log toda vez que um registro é CRIADO, ALTERADO ou EXCLUÍDO.


- A aplicação suporta os seguintes content types, e não é necessário enviar "Content-Type" no header da requisição:

    ```
    application/json (DEFAULT)
    application/x-www-form-urlencoded
    multipart/form-data
    ```


# Para observar a cobertura dos testes, rode os seguintes comandos

    ```
    $ python feiraslivresapi/manage.py test -v 2 feiraslivres --with-coverage --cover-html
    ```

NOTA: A cobertura do relatório de testes pode ser acessada no arquivo ```feiraslivressp-api/fairslivresapi/cover/index.html```. Ao clicar em um arquivo do relatório, você pode visualizar a cobertura linha por linha.
