__author__ = 'Daniel Roth'

import sys

import argparse

import zmq

from Client import Client
from Validator import Validator

import httplib, urllib

import time

"""
This is the Zeus CLI, it is used to generate traffic via TCP wit 0MQ and Websockets.
The CLI sets up, configures an runs a client.
It will not setup the server but it allows to configure the server anyway by sending
it all the information it needs via HTTP.
REMEBER!!!! While you are working on this CLI you are able to access the serverclass,
but in productive usage you could not be able to! Don't use serverclass here!
USAGE:"""

#Parameter standards:
httpport = '5000'
port = '8080'
ip = 'localhost'
number_of_clients = 0
flow = 2
repsize = 0
type = None
client_count = 1
size = 0

#Gloabals
clientList = [] #Used for multiple clientcounts



argparser = argparse.ArgumentParser(description='This is a CLI script for Zeus Networktool')
#################################
# SUPPORTED ARGUMENTS           #
#################################

argparser.add_argument('-p', '--port', help="Port of the destination server. Default: 8080", required=False)
argparser.add_argument('-i', '--target_ip', help="Ipv4 Aadress of the destination Server.", required=False)
argparser.add_argument('-t', '--type', help="Type of protocol.E.g.: zmq_req, zmq_sub, http_get.", required=True)
argparser.add_argument('-s', '--size', help="Size of message in byte", required=True)
argparser.add_argument('-c', '--client_count', help="Count of sending clients", required=False)

#Read params
args = argparser.parse_args()


#################################
# VALIDATION                    #
#################################

#create a new Validator and validate Params
validator = Validator()

#validate and set Port
#if port is not set manually use standard
if args.port is not None:
    validator.validate_port(int(args.port))
    port = args.port

#validate and set type
validator.validate_type(args.type)
type = args.type

#validate an set size
validator.validate_size(int(args.size))
size = args.size

#validate and set ip
if args.target_ip is not None:
    validator.validate_ip(args.target_ip)

print "Trying to configure server ... on Port " + port



#################################
# SEND SERVER INSTRUCTIONS      #
#################################
def configure_req():
    params = urllib.urlencode({'type': type, 'port': port, 'flow': flow, 'repsize': repsize})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(ip + ":" + httpport)
    print "http://" + ip + ":" + httpport + "/" + str(args.type)
    conn.request("POST", "http://" + ip + ":" + httpport + "/" + str(args.type), params, headers)
    client = Client()
    client.sendAsync(flow, size)
    response = conn.getresponse()
    print response.status


#This is a functionmap that calls a function by type
functionMap = {"zmq_req": configure_req}
functionToCall = functionMap[type]
functionToCall()
