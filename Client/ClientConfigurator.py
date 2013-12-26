__author__ = 'Gregor Milenkovic / Daniel Roth'
import ConfigParser
import os.path

class ClientConfigurator():

    config = ConfigParser.ConfigParser()

    def check_exists(self, filename):
        '''
        Check confiurationfile exists
        @param filename:
        @return: True/False
        '''
        if os.path.isfile(filename + ".ini"):
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
            self.config.set('Settings', 'Port', port)
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
            print "A configuration name " + filename + " already exists!"

