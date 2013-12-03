__author__ = 'Daniel Roth'
import zmq

import threading
from thread import allocate_lock
import datetime

#GLOBALS
lock = allocate_lock()

class Client(threading.Thread):
    port = "8080"
    ip = "localhost"

    def setPort(self, port):
        self.port = port

    def setIp(self, ip):
        self.ip = ip

    #This function sends a Message to a REP Socket
    def sendAsync(self, flow, size):
        #Connecting the Socket
        context = zmq.Context()
        reqsocket = context.socket(zmq.REQ)
        reqsocket.connect("tcp://" + self.ip + ":" + self.port)
        #send requests
        for i in range(flow):
            now = str(datetime.datetime.now())
            lock.acquire()
            print "sending a request" + self.getName() + " " + now
            lock.release()
            reqsocket.send(bytes(size))
            #no reply is needed
            message = reqsocket.recv()
            lock.acquire()
            print "received reply " + message + " bytes in " + self.getName()
            lock.release()