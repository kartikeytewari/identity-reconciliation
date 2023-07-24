import psycopg2
import time
from flask import Flask, request
import os

app = Flask(__name__)

def get_connection():
    print ("establising connection")
    try:
        val = psycopg2.connect(
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"), 
            password=os.environ.get("POSTGRES_PASSWORD"), 
            host=os.environ.get("HOST_IP"),
            port=os.environ.get("POSTGRES_PORT")
        )
        return val
    except (Exception, psycopg2.Error) as error:
        print ("Error: ", error)
        return False


conn = get_connection()
if conn:
    print("Connection to PSQL DB successful")
else:
    print(f"Connection to PSQL DB failed with error: {conn}")

@app.route("/", methods=["GET"])
def landing_page():
    return "Landing Page"

@app.route("/identify", methods=["POST"])
def reconciliation():
    payload = request.json
    no_data_flag = True
    if ("email" in payload):
        no_data_flag = False
        print ("payload has email")
        print (payload["email"])
    if ("phoneNumber" in payload):
        no_data_flag = False
        print ("payload has phone_number")
        print (payload["phoneNumber"])
    if (no_data_flag):
        print ("nothing present")
    return "hello"

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
