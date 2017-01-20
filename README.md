## API utilizando Python 3.5 e Django rest framework para CRUD básico de Feiras Livres de São Paulo

1) Instale os requirements que contém django e djangorestframework à partir do diretório inicial do projeto

    ```
    $ pip install -r requirements.txt
    ```

2) Crie um novo projeto em Django e em seguida uma nova aplicação

    ```
    $ django-admin.py startproject feiraslivresapi
    $ cd feiraslivresapi
    $ python manage.py startapp feiraslivres
    ```

2) Edite o arquivo feiraslivresapi/settings.py , adicionando a aplicação (feiraslivres.apps.FeiraslivresConfig) e o rest_framework

    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'feiraslivres.apps.FeiraslivresConfig',
    ]
    ```

3) Crie o models da sua aplicação (```/feiraslivresapi/feiraslivres/models.py```).

4) Crie e execute as migrações

    ```
    $ python manage.py makemigrations feiraslivres
    $ python manage.py migrate
    ```

NOTA: Enquanto não apontarmos para outro banco de dados relacional, ele usará sqlite3 por padrão. Assim, você pode usar o "sqlite3 CLI" para confirmar as tabelas criadas pós execução das migrações:

    ```
    $ sqlite3 db.sqlite3 '.tables'
    $ sqlite3 db.sqlite3 '.schema feiraslivres_feira'
    $ sqlite3 db.sqlite3 'SELECT * FROM feiraslivres_feira;'
    ```

5) Crie os serializers (```/feiraslivresapi/feiraslivres/serializers.py```)

6) Crie as views da API (```feiraslivres/views.py```).

7) Crie as rotas de url (```feiraslivres/urls.py``` e ```feiraslivresapi/urls.py```)

8) Teste a aplicação:

    ```
    $ python manage.py runserver
    ```

- Para importar os dados do CSV, basta na raíz do projeto executar o seguinte comando e este fará uso da API para inserir os dados no SQLite3

    ```
    $ python import_data.py DEINFO_AB_FEIRASLIVRES_2014.csv
    ```

- O log dessa importação está em import_data.log


# Apêndice

Testando com curl:

- Retorna todas as feiras

    ```
    $ curl -iX GET http://localhost:8000/feiras/
    $ curl -X GET http://localhost:8000/feiras/ | python -m json.tool # Mais apresentável
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

- Cadastra uma nova feira

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

- Deleta uma feira à partir de sua Primary Key

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

- Altera os campos cadastrados de uma feira, exceto a Primary Key

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

- Busca de feiras podendo utilizar qualquer um dos parâmetros (distrito,regiao5, nome_feira, bairro)

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

# Execute os testes com o seguinte comando na raiz do projeto

    ```
    $  pytest -s -vv feiraslivresapi/tests/
    ```

    ```
    ================================================================= test session starts ==============================================================
    platform linux -- Python 3.5.1, pytest-3.0.5, py-1.4.32, pluggy-0.4.0 -- /home/rshimithy/.pyenv/versions/3.5.1/envs/envFeiraslivres/bin/python
    cachedir: .cache
    rootdir: /home/rshimithy/Documents/feiraslivressp-api, inifile:
    plugins: django-3.1.2, cov-2.4.0
    collected 6 items

    feiraslivresapi/tests/api/test_feiras.py::test_get_feira_from_api PASSED
    feiraslivresapi/tests/api/test_feiras.py::test_post_feira_on_api PASSED
    feiraslivresapi/tests/api/test_feiras.py::test_put_feira_on_api PASSED
    feiraslivresapi/tests/api/test_feiras.py::test_patch_feira_on_api PASSED
    feiraslivresapi/tests/api/test_feiras.py::test_delete_feira_on_api PASSED
    feiraslivresapi/tests/unit/test_models.py::test_is_working PASSED

    ============================================================= 6 passed in 0.56 seconds =============================================================
    ```

NOTA: Nos logs do Django server você verá algo assim:

    [19/Jan/2017 12:20:48] "GET /feiraslivres/ HTTP/1.1" 200 374
    ( Aqui, "200" é o HTTP STATUS CODE e "374" is the o tamanho do conteúdo. )


- A aplicação suporta os seguintes content types, no qual deve ser enviado no request header "Content-Type":

    ```
    application/json
    application/x-www-form-urlencoded
    multipart/form-data
    ```

- As urls utilizadas para GET no CURL também são acessíveis via Browser:

    ```
    http://localhost:8000/feiraslivres/
    http://localhost:8000/feiraslivres/2/
    ```


