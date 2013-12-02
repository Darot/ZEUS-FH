__author__ = 'Daniel Roth'

from flask import Flask
from flask import request
from Server import Server

app = Flask(__name__)
args = None

def run_async():
    print request.form['type']
    print 'Try to initialize ZMQ-REP Socket'
    sock = Server() #Needs Funktion to check a Ports availability!
    sock.asyncsocket(request.form['flow'], request.form['repsize'])

@app.route("/zmq_req", methods=['POST'])
def zmq_req_starter():
    run_async()
    return 'initialising'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')