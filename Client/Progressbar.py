#!/usr/bin/env python
#
#  Corey Goldberg - 2010
#  ascii command-line progress bar with percentage and elapsed time display
#
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
    state = loops done
    '''
    state = 0


    def __init__(self, max):
        self.max = max

    def set_starttime(self, starttime):
        self.starttime = starttime

    def set_endurance(self, endurance):
        self.endurance = endurance

    def update_progress(self):
            self.state += 1
            progress = 100.0 / float(self.max) * self.state
            progress = int(progress)
            sys.stdout.write('\r[{0}{1}] {2}'.format('#'*(progress/10), ' '*(10-progress/10), progress))
            sys.stdout.flush()

    def update_progress_time(self, now):
            self.state = now - self.starttime
            progress = 100.0 / float(self.endurance) * self.state.seconds
            progress = int(progress)
            sys.stdout.write('\r[{0}{1}] {2}'.format('#'*(progress/10), ' '*(10-progress/10), progress))
            sys.stdout.flush()