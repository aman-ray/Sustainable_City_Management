import os
import psycopg2
import configparser
import requests
import logging
import json

config = configparser.ConfigParser()
CFG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'config.ini')
config.read(CFG_DIR)
database = config.get('AWS', 'database')
user = config.get('USERS_CREDS', 'user')
password = config.get('USERS_CREDS', 'pwd')
host = config.get('AWS', 'host')
connection_string = "dbname=" + database + " user=" + user + " host=" + host + " password=" + password
PARKING_JSON_TABLE = "\"API_RAW\".\"R_parking.json\""

logging.basicConfig(filename='APIHandling/logs/api_caller.log', level=logging.DEBUG)


def getLatestData():
    # Call API for dublin parking
    try:
        dublinparking_data_request = requests.get(
            "http://data-sdublincoco.opendata.arcgis.com/datasets/c62b49536b5e466f807943e9a0cf6df0_0.geojson")
        dublinparking_data = json.loads(dublinparking_data_request.text)
        return dublinparking_data
    except json.JSONDecodeError:
        logging.exception('Error when parsing JSON, raw data was ' + str(dublinparking_data))
        raise requests.RequestException('Unable to do my work! Invalid JSON data returned.')


#This function uses native SQL to insert data into db, ignore if using Django models.
def pg_insert(connection_string, table_name, json_collection):
    try:
        conn = psycopg2.connect(connection_string)
        print("Connecting to Database")
        cur = conn.cursor()

        cur.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))

        for record in json_collection:
            record = json.dumps(record)
            cur.execute(("INSERT INTO {} VALUES ('{}')".format(table_name, str(record).replace("'", "<>"))))
            cur.execute("commit;")

        print("Inserted data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")
    except Exception as e:
        print('Error {}'.format(str(e)))