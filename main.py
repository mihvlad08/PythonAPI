from flask import *
import json, time

app = Flask(__name__)
requests = 0


@app.route('/', methods=['GET'])
def test_connection():
    global requests
    requests = requests + 1
    data_set = {'Message': "You have successfully connected to the API!"}
    json_dump = jsonify(data_set)
    return data_set


@app.route('/admin', methods=['GET'])
def admin():
    global requests
    data_set = {'Message': f"The API has handled {requests} requests so far."}
    json_dump = jsonify(data_set)
    return data_set


if __name__ == "__main__":
    app.debug = True
    app.run(port=7777)
