__author__ = 'Daniel Roth'

from colorama import init, Fore, Back, Style


class Server_status():
    servers = [{}]
    server_count = 0
    #servers[0] = {"HTTP" : "5000"}


    def add_server(self, Type, Port):
        self.servers.append({Type: Port})
        return True

    def delete_server(self, port):
        for server in self.servers:
            if "".join(server.values()) == str(port):
                self.servers.remove(server)

    def get_printable(self):
        output = "| Type  | Port  | Properties          |\n"
        output +="|-------------------------------------|\n"
        i = 0
        for server in self.servers:
            try:
                port,properties = "".join(server.values()).split(",")
                output += "| " + "".join(server.keys()) + "\t| " + Fore.GREEN + port + Fore.RESET + "\t| " + properties + "\n"
            except ValueError:
                output += "| " + "".join(server.keys())  + "\t| " + Fore.GREEN + "".join(server.values()) + Fore.RESET + "\t|\n"
        i += 1
        return output

    def check_running(self, port):
        for server in self.servers:
            if "".join(server.values()) == str(port):
                return "True"
        return "False"









