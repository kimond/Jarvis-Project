#!/usr/bin/env python
import threading
from Think import *


class WriteReco(threading.Thread):

    def run(self):
        self.result = ""
        self.think = Think()
        while(True):
            self.RequestMsg()

    def RequestMsg(self):
        self.result = raw_input("What you want to do ? \n")
        if(self.result != ""):
            self.think.checkcommand(self.result)
            