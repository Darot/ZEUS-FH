__author__ = 'Daniel Roth'

from colorama import init, Fore, Back, Style

class Server_status():
    servers = [{}]
    server_count = 0
    #servers[0] = {"HTTP" : "5000"}


    def add_server(self, Type, Port):
	self.servers.append({Type : Port})
	return True
      
    def get_printable(self):
	output = "| Type  | Port  |\n"
	output += "|---------------|\n"
	i = 0
	for server in self.servers:
	    output += "| " + "".join(server.keys())  + "\t| " + Fore.GREEN + "".join(server.values()) + Fore.RESET + "\t|\n"
	i += 1
	return output












