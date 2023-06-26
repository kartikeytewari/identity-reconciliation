from flask import Flask, request

app = Flask(__name__)

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
