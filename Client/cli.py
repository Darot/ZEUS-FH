#! /usr/bin/env python
__author__ = 'Daniel Roth'

import argparse
from colorama import init, Fore, Back, Style

from Client import Client
from Validator import Validator
from Progressbar import Progressbar
from ClientConfigurator import ClientConfigurator

from subprocess import call

import httplib, urllib

import thread
import time
import sys

"""
This is the Zeus CLI, it is used to generate traffic via TCP wit 0MQ and Websockets.
The CLI sets up, configures an runs a client.
It will not setup the server but it allows to configure the server anyway by sending
it all the information it needs via HTTP.
REMEBER!!!! While you are working on this CLI you are able to access the serverclass,
but in productive usage you could not be able to! Don't use the serverclass here!
USAGE:"""
#colorama
init()
#Standard values
httpport = '5000'
port = '8080'
ip = 'localhost'
flow = 1
repsize = 0
type = None
client_count = 1
size = 1
delay = 0

argparser = argparse.ArgumentParser(description='This is a CLI script for Zeus Networktool')
#################################
# SUPPORTED ARGUMENTS           #
#################################
group = argparser.add_argument_group()
group_mute = argparser.add_mutually_exclusive_group()

group.add_argument('-p', '--port', help="Port of the destination server. Default: 8080", required=False)
group.add_argument('-i', '--target_ip', help="Ipv4 Aadress of the destination Server.", required=False)
group.add_argument('-t', '--type', help="Type of protocol.E.g.: zmq_req, zmq_sub, http_get.", required=False)
group.add_argument('-s', '--size', help="Size of message in byte", required=False)
group.add_argument('-c', '--client_count', help="Count of sending clients", required=False)
group.add_argument('-d', '--delay', help="Delay between Messages (seconds)", required=False)
group.add_argument('-f', '--flows', help="Count of flows", required=False)
group.add_argument('-r', '--reply_size', help="Size of replies in bytes", required=False)

group.add_argument('--save', help="Save current parameterset in a config file", required=False)
group_mute.add_argument('--config', help="Load a saved parameterset from a config file", required=False)
group_mute.add_argument('--print_config', help="Print a saved configuration file", required=False)

#Read params
args = argparser.parse_args()

if args.print_config is not None:
    c = ClientConfigurator()
    if c.check_exists(args.print_config) is False:
         print Fore.RED + "No configuration named " + args.print_config + " found!" + Fore.RESET
    else:
        c.print_config(args.print_config)
        sys.exit()


if args.config is not None:
    c = ClientConfigurator()
    if c.check_exists(args.config) is False:
         print Fore.RED + "No configuration named " + args.print_config + " found!" + Fore.RESET
    else:
        params = c.load_config(args.config)
        #set loaded params
        args.port = params["port"]
        httpport = params["httpport"]
        ip = params["ip"]
        args.flows = params["flow"]
        repsize = params["repsize"]
        args.type = params["type"]
        args.client_count = params["client_count"]
        args.size = params["size"]
        args.delay = params["delay"]

#################################
# VALIDATION                    #
#################################

#create a new Validator and validate Params
validator = Validator()

#validate replysize
if args.reply_size is not None:
    validator.validate_repsize(args.reply_size)
    repsize = args.reply_size

#validate and set Port
if args.port is not None:
    validator.validate_port(int(args.port))
    port = args.port

#validate and set type
if args.type is not None:
    validator.validate_type(args.type)
    type = args.type

#validate an set size
if args.size is not None:
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
    validator.validate_delay(args.delay)
    delay = float(args.delay)

#validate and set flow
if args.flows is not None:
    validator.validate_flows(args.flows)
    flow = int(args.flows)


if args.save is not None:
    c = ClientConfigurator()
    if c.check_exists(args.save):
         print Fore.RED + "A configuration named " + args.save + " already exists!" + Fore.RESET
    else:
        c.write_config(args.save, port, httpport, ip, flow, repsize, type,
                       client_count, size, delay)


#################################
# SEND SERVER INSTRUCTIONS      #
# AND RUN CLIENT                #
#################################
def run_req():
    p = Progressbar(flow*client_count)
    params = urllib.urlencode({'type': type,
                               'port': port, 'flow': flow*client_count,
                               'repsize': repsize})

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}

    conn = httplib.HTTPConnection(ip + ":" + httpport)
    print "http://" + ip + ":" + httpport + "/" + str(args.type)
    conn.request("POST", "http://" + ip + ":" + httpport + "/" + str(args.type), params, headers)
    for i in range(client_count):
        client = Client(p)
        thread.start_new_thread(client.sendAsync, (flow, size, delay))
    response = conn.getresponse()
    if response.status == 200:
        print "Transmission complete!"
    else:
        print "Something went wrong!"

def run_http_post():
    #initialize a progressbar
    p = Progressbar(flow*client_count)
    client = Client(p)
    client.send_http_post(ip, httpport, flow, delay, size)

def server_status():
    conn = httplib.HTTPConnection(ip + ":" + httpport)
    try:
        conn.request("GET", "http://" + ip + ":" + httpport + "/status")
        response = conn.getresponse()
        print Fore.GREEN + "Server is ONLINE" + Fore.RESET
    except:
        sys.exit(Fore.RED + "Couldn't reach a Server on " + ip + ":" + httpport +  Fore.RESET)


if type is not None:
    print "Trying to configure server ... on Port " + port
    server_status()
    print "abort with Ctrl-C"
    time.sleep(2)
    #This is a functionmap that calls a function by type
    functionMap = {"zmq_req": run_req, "http_post": run_http_post}
    functionToCall = functionMap[type]
    functionToCall()