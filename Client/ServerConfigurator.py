__author__ = 'Daniel Roth'

import httplib, urllib

class ServerConfigurator():

    def configure_req(self):
        conn = httplib.HTTPConnection(ip + ":" + httpport)
        print "http://" + ip + ":" + httpport + "/" + str(args.type)
        conn.request("POST", "http://" + ip + ":" + httpport + "/" + str(args.type), params, headers)
        client1 = client()
        client1.sendAsync(flow, repsize)
        response = conn.getresponse()
        print response.status
