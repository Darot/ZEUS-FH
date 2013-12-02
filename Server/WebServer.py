__author__ = 'Daniel Roth'

from flask import Flask
from flask import request
from Server import Server
import time

app = Flask(__name__)
args = None

def run_async():
    print request.form['type']
    server = Server('8080')
    server.run_asyncsocket(99999999, 1)
    time.sleep(1)


@app.route("/zmq_req", methods=['POST'])
def zmq_req_starter():
    run_async()
    return 'initialising'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')