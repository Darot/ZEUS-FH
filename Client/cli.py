__author__ = 'Daniel Roth'
import argparse
import zmq
from Client import client


#This is the Zeus CLI, it is used to generate traffic via TCP wit 0MQ and Websockets.
#The CLI sets up, configures an runs a client.
#It will not setup the server but it allows to configure the server anyway by sending
#it all the information it needs via HTTP.
#REMEBER!!!! While you are working on this CLI you are able to access the serverclass,
#but in productive usage you could not be able to! Don't use serverclass here!
#USAGE:

#Parameter standards:
#port = '8080'
#ip = 'localhost'
#number_of_clients = 0


#argparser = argparse.ArgumentParser(description='This is a CLI Script for Zeus Networktool')

#Supported Arguments:
#argparser.add_argument('-p', '--port', help="Port of the destination server. Default: 8080", required = False)
#argparser.add_argument('-')

#create a new Client
client1 = client()
client1.sendAsync(3)
