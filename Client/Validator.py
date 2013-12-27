__author__ = 'Daniel Roth'
import sys
import socket


class Validator():

    def validate_port(self, port):
        if not 80 < port < 9999:
            sys.exit("Invalid port! Port must be between 80 and 9999")

    def validate_type(self, type):
        valid_types = ['zmq_req', 'http_get']
        if type in valid_types:
            return True
        else:
            sys.exit("Invalid Type! Read the docs to see valid types")

    def validate_ip(self, ip):
        try:
            socket.inet_aton(ip)
            return True
        except ValueError:
            sys.exit("Invalid Ip-Adress")
        except socket.error:
            sys.exit("Invalid IP-Address")

    def validate_size(self, size):
        if not 0 < size < 30001:
            sys.exit("Invalid size! max. 30000")

    def validate_client_count(self, client_count):
        if not 0 < client_count < 51:
            sys.exit("Invalid client count! max. 50")