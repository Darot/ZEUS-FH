__author__ = 'Daniel Roth'

from flask import Flask
from flask import request

app = Flask(__name__)
args = None

@app.route("/zmq_req", methods=['POST'])
def zmq_req_starter():
    print request

if __name__ == "__main__":
    app.run(host='0.0.0.0')