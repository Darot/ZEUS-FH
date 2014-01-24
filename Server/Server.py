__author__ = 'Daniel Roth'
import zmq
import sys
from Server_status import Server_status
import time


class Server():
    """
    This class is used to manage the settings given by a client
    and runs the server with the configurations he needs.
    The information will be sent via HTTP and Handled via Flask WSGI.

    This Class contains all the server-functions, the ZeusCLI supports
    """

    port = "8080"

    def __init__(self, port, status):
        self.port = port
        self.status = status

    def run_asyncsocket(self, repsize):
        print "running 0MQ Reply Socket on %s" % self.port
        #Binding the Socket
        context = zmq.Context()
        repsocket = context.socket(zmq.REP)
        try:
            repsocket.bind("tcp://*:%s" % self.port)
            self.status.add_server("ZMQ_R", str(self.port))
        except zmq.ZMQError:
            print "A server is already running on that port."

        while True:
            #Wait for next request from a client
            #A reply is not needed in this case
            message = repsocket.recv()
            print "message received " + message + " bytes"
            if message == "EOM":
                break
            if repsize == 0:
                repsocket.send(bytes(1))
            else:
                repsocket.send(bytes(repsize))

    def run_publisher(self, size, delay):
        print "running 0MQ Publisher Socket on %s" % self.port
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        msg = bytes(size)
        topic = 1
        try:
            socket.bind("tcp://*:%s" % str(self.port))
            self.status.add_server("ZMQ_P", str(self.port))
        except zmq.ZMQError:
            print "A server is already running on that port"
        while True:
            socket.send("%d %s" % (topic, msg))
            print "sending"
            time.sleep(delay)














