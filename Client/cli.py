__author__ = 'Daniel Roth'

import sys

import argparse

import zmq

from Client import Client
from Validator import Validator

import httplib, urllib

import thread

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
flow = 1
repsize = 0
type = None
client_count = 1
size = 0
delay = 0

#Gloab

argparser = argparse.ArgumentParser(description='This is a CLI script for Zeus Networktool')
#################################
# SUPPORTED ARGUMENTS           #
#################################

argparser.add_argument('-p', '--port', help="Port of the destination server. Default: 8080", required=False)
argparser.add_argument('-i', '--target_ip', help="Ipv4 Aadress of the destination Server.", required=False)
argparser.add_argument('-t', '--type', help="Type of protocol.E.g.: zmq_req, zmq_sub, http_get.", required=True)
argparser.add_argument('-s', '--size', help="Size of message in byte", required=True)
argparser.add_argument('-c', '--client_count', help="Count of sending clients", required=False)
argparser.add_argument('-d', '--delay', help="Delay between Messages (seconds)", required=False)
argparser.add_argument('-f', '--flows', help="Count of flows", required=False)

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

#validate an set client count
if args.client_count is not None:
    validator.validate_client_count(int(args.client_count))
    client_count = int(args.client_count)

#validate and set target ip
if args.target_ip is not None:
    validator.validate_ip(args.target_ip)
    ip = args.target_ip

#validate and set delay
if args.delay is not None:
    delay = float(args.delay)

#validate an set flow
if args.flows is not None:
    flow = int(args.flows)

print "Trying to configure server ... on Port " + port
print "abort with Ctrl-C"
time.sleep(2)



#################################
# SEND SERVER INSTRUCTIONS      #
#################################
def run_req():
    params = urllib.urlencode({'type': type,
                               'port': port, 'flow': flow*client_count,
                               'repsize': repsize})

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}

    conn = httplib.HTTPConnection(ip + ":" + httpport)
    print "http://" + ip + ":" + httpport + "/" + str(args.type)
    conn.request("POST", "http://" + ip + ":" + httpport + "/" + str(args.type), params, headers)
    for i in range(client_count):
        client = Client()
        thread.start_new_thread(client.sendAsync, (flow, size, delay))
    response = conn.getresponse()
    if response.status == 200:
        print "Transmission complete!"
    else:
        print "Something went wrong!"


#This is a functionmap that calls a function by type
functionMap = {"zmq_req": run_req}
functionToCall = functionMap[type]
functionToCall()

