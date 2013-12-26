__author__ = 'Gregor Milenkovic / Daniel Roth'
import ConfigParser
import os.path
from tabulate import tabulate

class ClientConfigurator():

    config = ConfigParser.ConfigParser()

    def check_exists(self, filename):
        '''
        Check confiurationfile exists
        @param filename:
        @return: True/False
        '''
        if os.path.isfile("./Config/" + filename + ".ini"):
            return True
        else:
            return False


    def write_config(self, filename, port, httpport, ip, flow, repsize, type, client_count, size, delay):
        '''
        Create a ZEUS-configurationfile.
        Values will not be validated in this class!

        @param filename:
        @param port:
        @param httpport:
        @param ip:
        @param flow:
        @param repsize:
        @param type:
        @param client_count:
        @param size:
        @param delay:
        @return:
        '''

        try:
            configfile = open("./Config/" + filename + ".ini", 'w')
            self.config.add_section('Settings')
            self.config.set('Settings', 'port', port)
            self.config.set('Settings', 'httpport', httpport)
            self.config.set('Settings', 'ip', ip)
            self.config.set('Settings', 'flow', flow)
            self.config.set('Settings', 'repsize', repsize)
            self.config.set('Settings', 'type', type)
            self.config.set('Settings', 'client_count', client_count)
            self.config.set('Settings', 'size', size)
            self.config.set('Settings', 'delay', delay)
            self.config.write(configfile)
            configfile.close()
        except:
            print "\033[1;48mA configuration named " + filename + " already exists!\33[1;m"

    def load_config(self, filename):
        '''
        Reads a configuration file and returns the values in a dictionary.
        @param filename:
        @return: dict{port: value, httpport : value, ip : value
          flow: value, repsize : value, type : value, client_count : value
          size : value, delay: value}
        '''
        self.config.read("./Config/" + filename + ".ini")
        params = { "port" : self.config.get('Settings', 'port'),
                   "httpport" : self.config.get('Settings', 'httpport'),
                   "ip" : self.config.get('Settings', 'ip'),
                   "flow" : self.config.get('Settings', 'flow'),
                   "repsize" : self.config.get('Settings', 'repsize'),
                   "type" : self.config.get('Settings', 'type'),
                   "client_count" : self.config.get('Settings', 'client_count'),
                   "size" : self.config.get('Settings', 'size'),
                   "delay" : self.config.get('Settings', 'delay') }
        return params

    def print_config(self, filename):
        params = self.load_config(filename)
        params = params.items()
        print tabulate(params)