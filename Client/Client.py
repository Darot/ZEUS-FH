__author__ = 'Daniel Roth'
import zmq

class client():
    port = "8080"
    ip = "localhost"

    def setPort(self, port):
        self.port = port

    def setIp(self, ip):
        self.ip = ip

    #This function sends a Message to a REP Socket
    #Flow = Count of loops
    def sendAsync(self, flow, size):
        #Connecting the Socket
        context = zmq.Context()
        reqsocket = context.socket(zmq.REQ)
        reqsocket.connect("tcp://" + self.ip + ":" + self.port)
        #REMOVE THIS LINE !!!
        print ("tcp://" + self.ip + self.port)
        #send requests
        for i in range(flow):
            print "sending a request"
            reqsocket.send(bytes(size))
            #no reply is needed
            message = reqsocket.recv()
            print "received reply " + message + " bytes"
