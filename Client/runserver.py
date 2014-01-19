__author__ = 'zeus'

import argparse
from colorama import init, Fore, Back, Style


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
endurance = 4900

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
group.add_argument('-r', '--reply_size', help="Size of replies in bytes", required=False)
group.add_argument('-e', '--endurance', help="Time to send. Don't use with -f, --flows", required=False)

args = argparser.parse_args()