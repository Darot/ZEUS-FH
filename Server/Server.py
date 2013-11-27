__author__ = 'Daniel Roth'
import zmq


#This class is used to manage the settings of the client
#and runs the server with the configurations he needs.
#The information will be sent via .............

#This Class contains all the server-funktions, the ZeusCLI supports
class Server():
    port = "8080"

    #This Method runs a REP Socket
    #flow = count of loops
    def asyncsocket(self, flow, repsize):
        print "Using 0MQ Reply Socket"
        #Binding the Socket
        context = zmq.Context()
        repsocket = context.socket(zmq.REP)
        repsocket.bind("tcp://*:%s" % self.port)

        for i in range(flow):
            #Wait for next request from a client
            #A reply is not needed in this case
            message = repsocket.recv()
            print "message received " + message + " bytes"
            if repsize == 0:
                repsocket.send(bytes(1))
            else:
                repsocket.send(bytes(repsize))













