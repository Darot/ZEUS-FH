#! /usr/bin/env python
__author__ = 'Daniel Roth'

from flask import Flask
from flask import request
from flask import g

from Server import Server
from Server_status import Server_status

from threading import Thread

import time

import WebsocketServer


app = Flask(__name__)
args = None

#Konstants for print

status = Server_status()

status.add_server("HTTP" , "5000")

def run_async(port, repsize):
    server = Server(port, status)
    server.run_asyncsocket(int(repsize))
    time.sleep(1)

def run_pub(port, size, delay):
    server = Server(port, status)
    server.run_publisher(int(size), float(delay))
    time.sleep(1)

@app.route("/status")
def server_status():
    return status.get_printable()
  
@app.route("/check_running")
def check_running():
    return status.check_running(request.args["port"])

@app.route("/ws", methods=['POST'])
def websocket():
    thread = Thread(target=WebsocketServer.run_ws, args=(request.form["port"], status))
    #WebsocketServer.run_ws()
    thread.start()
    return "initialising"

#Trigger on a Request for a ZMQ reply socket
#the client will be a request socket
@app.route("/zmq_req", methods=['POST'])
def zmq_req_starter():
    thread = Thread(target = run_async, args = (request.form["port"],  request.form["repsize"]))
    #run_async(request.form["port"],  request.form["repsize"])
    thread.start()
    return "initialising"

@app.route("/zmq_pub", methods=['POST'])
def zmq_pub_starter():
    thread = Thread(target = run_pub, args = (request.form["port"],  request.form["size"]
                                      , request.form["delay"]))
    thread.start()
    return "initialising"

@app.route("/http_post", methods=['POST'])
def http_post():
    time.sleep(0.1)
    return 'received'


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')