__author__ = 'Daniel Roth'
import zmq
import sys

class Server():
    """
    This class is used to manage the settings given by a client
    and runs the server with the configurations he needs.
    The information will be sent via HTTP and Handled via Flask WSGI.

    This Class contains all the server-functions, the ZeusCLI supports
    """

    port = "8080"

    def __init__(self, port):
        self.port = port

    #This Method runs a REP Socket
    #flow = count of loops
    #def run_asyncsocket(self, flow, repsize):
    #    print "Using 0MQ Reply Socket"
    #    #Binding the Socket
    #    context = zmq.Context()
    #    repsocket = context.socket(zmq.REP)
    #    repsocket.bind("tcp://*:%s" % self.port)
    #
    #    for i in range(flow):
    #        #Wait for next request from a client
    #        #A reply is not needed in this case
    #        message = repsocket.recv()
    #        print sys.getsizeof(message)
    #        print "message received " + message + " bytes"
    #        if repsize == 0:
    #            repsocket.send(bytes(1))
    #        else:
    #            repsocket.send(bytes(repsize))

    def run_asyncsocket(self, repsize):
        print "Using 0MQ Reply Socket"
        #Binding the Socket
        context = zmq.Context()
        repsocket = context.socket(zmq.REP)
        repsocket.bind("tcp://*:%s" % self.port)

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
















