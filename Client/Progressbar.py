__author__ = 'Daniel Roth'

import threading
from thread import allocate_lock

import sys
import time

#GLOBALS
lock = allocate_lock()


class Progressbar():
    '''
    This is an ascii command-line progress bar
    That is used to show progress in longterm loops
    max = 100%
    state = loops done / time done
    '''
    state = 0


    def __init__(self, max):
        #set value for 100%
        self.max = max

    def set_starttime(self, starttime):
        #set startime for Progress over time
        self.starttime = starttime

    def set_endurance(self, endurance):
        #set endurance for Progress over time
        self.endurance = endurance

    def update_progress(self):
        '''
        Update the Progressbar by flows
        @return:
        '''
        self.state += 1
        #calculate stat with rule of three
        progress = 100.0 / float(self.max) * self.state
        progress = int(progress)
        sys.stdout.write('\r[{0}{1}] {2}'.format('#' * (progress / 10), ' ' * (10 - progress / 10), progress))
        #clear stdout
        sys.stdout.flush()

    def update_progress_time(self, now):
        '''
        Update the Progressbar by time
        @param now:
        @return:
        '''
        self.state = now - self.starttime
        #calculate stat with rule of three
        progress = 100.0 / float(self.endurance) * self.state.seconds
        progress = int(progress)
        sys.stdout.write('\r[{0}{1}] {2}'.format('#' * (progress / 10), ' ' * (10 - progress / 10), progress))
        #clear stdout
        sys.stdout.flush()