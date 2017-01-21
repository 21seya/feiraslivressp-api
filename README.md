## API using Python 3.5 and Django Rest Framework for basic CRUD of São Paulo's Free Fairs

1) Install the requirements that contain django and django rest framework from the project home directory

    ```
    $ pip install -r requirements.txt
    ```

2) Test the application:

    ```
    $ python manage.py runserver
    ```

- To import the CSV data, just in the root of the project execute the following command and this will make use of the API to insert the data in SQLite3

    ```
    $ python import_data.py DEINFO_AB_FEIRASLIVRES_2014.csv
    ```

- The import log is in import_data.log


# Testing with curl:

- Return all fairs

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

- Create a new fair

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

- Delete a fair using your Primary Key

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

- Change the registered fields of a fair, except the Primary Key

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

- Search for fairs using any of the parameters (distrito,regiao5, nome_feira, bairro)

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

NOTE: Because the application has no business logic and any complex behaviors, a structured text file log has not been applied. The application logs are in the terminal in DEBUG mode by default, so you'll see something like this:

    [19/Jan/2017 12:20:48] "GET /feiraslivres/ HTTP/1.1" 200 374
    ( Here, "200" is the HTTP STATUS CODE and "374" is the content length. )


- The application supports the following content types, it is not necessary to send "Content-Type" request header:

    ```
    application/json
    application/x-www-form-urlencoded
    multipart/form-data
    ```

- The urls used for GET in CURL are also accessible via Browser:

    ```
    http://localhost:8000/feiraslivres/
    http://localhost:8000/feiraslivres/2/
    ```

# To observe coverage tests, run the following commands

    ```
    $ cd feiraslivresapi
    $ python manage.py test -v 2 feiraslivres --with-coverage --cover-html
    ```

NOTE: The coverage report will be on feiraslivressp-api/fairslivresapi/cover/index.html. By clicking on the report file you can see the coverage line by line.

