import psycopg2
import time
from flask import Flask, request

app = Flask(__name__)

def get_connection():
    try:
        print ("establising connection")
        # val = psycopg2.connect("postgresql://postgres:password@localhost:5432/customer_data")
        try:
            val = psycopg2.connect(
                dbname="customer_data", 
                user="postgres", 
                password="password", 
                host="192.168.1.10", 
                port="5432"
            )
        except (Exception, psycopg2.Error) as error:
            print ("Error: ", error)
        return val
    except:
        return False


print ("-" * 8)
conn = get_connection()
print ("timestamp = ", int(time.time()))
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print ("conn = ", conn)
    print("Connection to the PostgreSQL encountered and error.")
print ("-" * 8)

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
