__author__ = 'Daniel Roth'
import argparse

import zmq

from Client import client
from Validator import Validator

import httplib, urllib

"""
This is the Zeus CLI, it is used to generate traffic via TCP wit 0MQ and Websockets.
The CLI sets up, configures an runs a client.
It will not setup the server but it allows to configure the server anyway by sending
it all the information it needs via HTTP.
REMEBER!!!! While you are working on this CLI you are able to access the serverclass,
but in productive usage you could not be able to! Don't use serverclass here!
USAGE:"""

#Parameter standards:
port = '8080'
ip = 'localhost'
number_of_clients = 0

#Gloabals
clientList = [] #Used for multiple clientcounts
type = ''



argparser = argparse.ArgumentParser(description='This is a CLI script for Zeus Networktool')
#################################
# SUPPORTED ARGUMENTS           #
#################################

argparser.add_argument('-p', '--port', help="Port of the destination server. Default: 8080", required=False)
argparser.add_argument('-i', '--target', help="Ipv4 Aadress of the destination Server.", required=False)
argparser.add_argument('-t', '--type', help="Type of protocol.E.g.: zmq_req, zmq_sub, http_get.", required=True)
argparser.add_argument('-s', '--size', help="Size of message in byte", required=True)

#Read params
args = argparser.parse_args()


#################################
# VALIDATION                    #
#################################

#create a new Validator and validate Params
validator = Validator()

#validate and set Port
if args.port is not None:
    print args.port
    validator.validate_port(int(args.port))
    port = args.port

#validate type
validator.validate_type(args.type)


#################################
# SEND SERVER INSTRUCTIONS      #
#################################

params = urllib.urlencode({'type': args.type, 'port': args.port})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("localhost:5000")
conn.request("POST", "http://localhost:5000/zmq_req", params, headers)
response = conn.getresponse()
print response.status





#################################
# INITIALIZE CLIENT(s)          #
#################################


#create a new clientinstance
#client1 = client()
#client1.sendAsync(3, 1024)
