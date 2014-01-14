__author__ = 'Daniel Roth'

from flask import Flask
from flask import request
from Server import Server
from flask import jsonify

import sys
import os

import time

app = Flask(__name__)
args = None


def run_async(port, flow, repsize):
    print request.form['type']
    server = Server(port)
    server.run_asyncsocket(int(flow), int(repsize))
    time.sleep(1)


@app.route("/status")
def server_status():
    return "Online!"

#Trigger on a Request for a ZMQ reply socket
#the client will be a request socket
@app.route("/zmq_req", methods=['POST'])
def zmq_req_starter():
    run_async(request.form["port"], request.form["flow"], request.form["repsize"])
    return 'initialising'

@app.route("/http_post", methods=['POST'])
def http_post():
    #print sys.getsizeof(request)
    request.files['file'].save('/tmp/foo')
    size = os.stat('/tmp/foo').st_size
    print "Received " + str(size) + " Bytes"
    return 'file received'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')