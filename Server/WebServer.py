__author__ = 'Daniel Roth'

from flask import Flask
from flask import request
from Server import Server
from flask import jsonify

# This is Bad! Very Bad! But Autobahn does not support Flask!
from twisted.internet import reactor
from autobahn.twisted.websocket import *

import sys
import os

import time

import WebsocketServer

app = Flask(__name__)
args = None


def run_async(port, repsize):
    print request.form['type']
    server = Server(port)
    server.run_asyncsocket(int(repsize))
    time.sleep(1)


@app.route("/status")
def server_status():
    return "Online!"

@app.route("/ws")
def websocket():
    WebsocketServer.run_ws()

#Trigger on a Request for a ZMQ reply socket
#the client will be a request socket
@app.route("/zmq_req", methods=['POST'])
def zmq_req_starter():
    run_async(request.form["port"],  request.form["repsize"])
    return 'initialising'


@app.route("/http_post", methods=['POST'])
def http_post():
    #print sys.getsizeof(request)
    return 'received'


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')