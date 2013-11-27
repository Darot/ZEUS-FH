__author__ = 'Daniel Roth'
import sys


class Validator():

    def validate_port(self, port):
        if not 80 < port < 9999:
            sys.exit("Invalid port! Port must be between 80 and 9999")

    def validate_type(self, type):
        valid_types = ['zmq_req', 'http_get']
        if type in valid_types:
            print "Got Type: " + type  #DELETE THIS LINE!!!!
        else:
            sys.exit("Invalid Type! Read the docs to see valid types")