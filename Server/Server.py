__author__ = 'Daniel Roth'
import zmq

#This class is used to manage the settings of the client
#and runs the server with the configurations he needs.
#The information will be sent via .............
def main():

    #Create a new serverinstance
    serv = Server()
    serv.asyncsocket(3)

#This Class contains all the server-funktions, the ZeusCLI supports
class Server():
    port = "8080"

    #This Method runs a REP Socket
    #flow = count of loops
    def asyncsocket(self, flow):
        print "Using 0MQ Reply Socket"
        #Binding the Socket
        context = zmq.Context()
        repsocket = context.socket(zmq.REP)
        repsocket.bind("tcp://*:%s" % self.port)

        for i in range(flow):
            #Wait for next request from a client
            #A reply is not needed in this case
            message = repsocket.recv()
            print "message received"
            repsocket.send(bytes(1))

if __name__ == '__main__':
    main()


