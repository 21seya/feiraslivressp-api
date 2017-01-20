import csv
import json
import logging
import os
import sys
import requests

LOG_FORMAT = ('[%(asctime)s PID %(process)s '
              '%(filename)s:%(lineno)s - %(funcName)s()] '
              '%(levelname)s '
              '%(message)s')
logging.basicConfig(filename="import_data.log",
                    format=LOG_FORMAT, filemode='a',
                    level=logging.INFO)


if len(sys.argv) < 2:
    print("Missing the csv filename parameter.")
    sys.exit()

if not os.path.exists(sys.argv[1]):
    print("The file does not exist. Check for its full path.")
    sys.exit()

logging.info('-' * 80)
logging.info('Beginning import of {}...'.format(sys.argv[1]))

headers = {'Content-Type': 'application/json'}

success = 0
errors = 0

file = csv.DictReader(open(sys.argv[1]))  # opens the csv file as a Dict
for row_number, row in enumerate(file):   # iterates the rows of the file in orders
    try:
        numero = row['NUMERO'].split('.')[0] if row['NUMERO'].strip() not in ['S/N', ''] else 0

        feira = {'id': row['ID'],
                 'longi': row['LONG'], 'lat': row['LAT'],
                 'setcens': row['SETCENS'], 'areap': row['AREAP'],
                 'coddist': int(row['CODDIST'].split('.')[0]) if row['CODDIST'].strip() else 0,
                 'distrito': row['DISTRITO'],
                 'codsubpref': int(row['CODSUBPREF'].split('.')[0]) if row['CODSUBPREF'].strip() else 0,
                 'subprefe': row['SUBPREFE'], 'regiao5': row['REGIAO5'],
                 'regiao8': row['REGIAO8'], 'nome_feira': row['NOME_FEIRA'],
                 'registro': row['REGISTRO'], 'logradouro': row['LOGRADOURO'],
                 'numero': numero,
                 'bairro': row['BAIRRO'], 'referencia': row['REFERENCIA']}

        res = requests.post('http://localhost:8000/feiras/',
                            data=json.dumps(feira),
                            headers=headers)
        if res.status_code != 201:
            errors += 1
            raise Exception("Error (status code {}) trying to populate db from line {}.".format(res.status_code,
                                                                                                row_number+1))
        else:
            success += 1
    except Exception as ex:
        logging.exception(ex)
        continue

logging.info('Import finished.')
logging.info('The file has a total of {} records.'.format(success + errors))
logging.info('{} records were successfully imported.'.format(success))
logging.info('{} records were NOT successfully imported due to errors.'.format(errors))
