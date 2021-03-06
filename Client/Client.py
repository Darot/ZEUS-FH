import zmq

import threading
from thread import allocate_lock
import datetime
import time
import sys

import httplib

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

from subprocess import call

#GLOBALS
lock = allocate_lock()

class Client():

    def __init__(self, progress):
        self.progress = progress


    #################################
    #           SOCKETS             #
    #################################

    #This function sends a Message to a REP Socket
    __author__ = 'Daniel Roth'
    def sendAsync(self, flow, size, delay, ip, port):
        '''
        Loops "flow"-times and sends messages to a ZMQ_Rep socket on a defined Server
        This is threadsave for multiple client instances.
        @param flow:
        @param size:
        @param delay:
        @return:
        '''
        #Connecting the Socket
        context = zmq.Context()
        reqsocket = context.socket(zmq.REQ)
        reqsocket.connect("tcp://" + ip + ":" + port)
        #send requests
        for i in range(flow):
            time.sleep(delay)
            reqsocket.send(bytes(size))
            message = reqsocket.recv()
            self.progress.update_progress()
        print "All messages sent!"

    #This function sends a Message to a REP Socket
    __author__ = 'Daniel Roth'
    def sendAsync_time(self, endurance, size, delay, ip, port):
        '''
        Loops "flow"-times and sends messages to a ZMQ_Rep socket on a defined Server
        This is threadsave for multiple client instances.
        @param flow:
        @param size:
        @param delay:
        @return:
        '''
        #Connecting the Socket
        context = zmq.Context()
        reqsocket = context.socket(zmq.REQ)
        reqsocket.connect("tcp://" + ip + ":" + port)
        #send requests
        stop = time.time() + endurance
        self.progress.set_starttime(datetime.datetime.now())
        self.progress.set_endurance(endurance)
        while time.time() < stop:
            time.sleep(delay)
            reqsocket.send(bytes(size))
            message = reqsocket.recv()
            self.progress.update_progress_time(datetime.datetime.now())
        print "\n All messages sent!"

    __author__ = 'Sinan Diehl'
    def subscriber(self, flow, ip, port):
        context = zmq.Context()
        sub = context.socket(zmq.SUB)
        sub.connect("tcp://" + ip + ":" + port)
        sub.setsockopt(zmq.SUBSCRIBE, "1")
        for i in range(flow):
            msg = sub.recv()
            channel,size = msg.split(" ")
            print "\r message received " + str(size) + "Bytes" + "\n"
            self.progress.update_progress()
        print "\n All messages received!"

    __author__ = 'Daniel Roth'
    def subscriber_time(self, endurance, ip, port):
        context = zmq.Context()
        sub = context.socket(zmq.SUB)
        sub.connect("tcp://" + ip + ":" + port)
        sub.setsockopt(zmq.SUBSCRIBE, "1")
        stop = time.time() + endurance
        self.progress.set_starttime(datetime.datetime.now())
        self.progress.set_endurance(endurance)
        while time.time() < stop:
            msg = sub.recv()
            self.progress.update_progress_time(datetime.datetime.now())
        print "\n All messages received!"

    __author__ = 'Daniel Roth'
    def stop_zmq_req(self, ip, port):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://" + ip + ":" + port)
        try:
            socket.send("EOM")
            rep = socket.recv()
            print rep
        except:
            print "Error: Theres is no Reply socket running on that address"



    #################################
    #           HTTP                #
    #################################
    __author__ = 'Daniel Roth'
    def send_http_post(self, ip, httpport, flow, delay, size):
        '''
        Loops "flow"-times and sends a file previously generated by a C Script
        to a webserver via HTTP-POST.
        This is threadsave for multiple client instances.
        @param ip:
        @param httpport:
        @param flow:
        @param delay:
        @return: True / False (Success / Fail)
        '''
        # Register the streaming http handlers with urllib2
        register_openers()
        process = call(["/usr/local/bin/Zeus/filemaker/filemaker", size])
        # Run Filemaker (a c program for filemaking by size)
        # A file with the given size(byte) will be stored in /tmp/size
        # headers contains the necessary Content-Type and Content-Length
        # datagen is a generator object that yields the encoded parameters
        datagen, headers = multipart_encode({"file": open("/tmp/size", "rb")})
        lost = 0
        for i in range(flow):
            time.sleep(delay)
            try:
                request = urllib2.Request("http://" + ip + ":" + httpport + "/http_post", datagen, headers)
                f = urllib2.urlopen(request)
            except:
                lost +=1
            #lock.acquire()
            #self.progress.update_progress()
            #lock.release()
            sys.stdout.write("\r" + str(lost) + "messages lost")
            self.progress.update_progress()
        print "\nDone! " + str(lost) + " messages lost"
        return True

    __author__ = 'Daniel Roth'
    def send_http_post_time(self, ip, httpport, endurance, delay, size):
        '''
        Loops "flow"-times and sends a file previously generated by a C Script
        to a webserver via HTTP-POST.
        This is threadsave for multiple client instances.
        @param ip:
        @param httpport:
        @param endurance:
        @param delay:
        @return: True / False (Success / Fail)
        '''
        # Register the streaming http handlers with urllib2
        register_openers()
        process = call(["/usr/local/bin/Zeus/filemaker/filemaker", size])
        # Run Filemaker (a c program for filemaking by size)
        # A file with the given size(byte) will be stored in /tmp/size
        # headers contains the necessary Content-Type and Content-Length
        # datagen is a generator object that yields the encoded parameters
        datagen, headers = multipart_encode({"file": open("/tmp/size", "rb")})
        conn = httplib.HTTPConnection(ip + ":" + httpport)
        stop = time.time() + endurance
        lost = 0
        self.progress.set_starttime(datetime.datetime.now())
        self.progress.set_endurance(endurance)
        while time.time() < stop:
            time.sleep(delay)
            try:
                request = urllib2.Request("http://" + ip + ":" + httpport + "/http_post", datagen, headers)
                f = urllib2.urlopen(request)
            except:
                lost +=1
            #lock.acquire()
            #self.progress.update_progress()
            #lock.release()
            sys.stdout.write("\r" + str(lost) + "messages lost")
            self.progress.update_progress_time(datetime.datetime.now())
        print "\nDone! " + str(lost) + " messages lost"
        return True