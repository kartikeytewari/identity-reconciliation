import time
import os
from flask import Flask, request
import psycopg2
from reconcile import *

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
    if ("email" in payload) and ("phoneNumber" in payload):
        contact_directory = store_data(conn, payload["email"], payload["phoneNumber"])
        return contact_directory
    else:
        return "Insufficient data"

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
