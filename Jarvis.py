#!/usr/bin/env python
from SpeechReco import *
from WriteReco import *
from SpeechServer import *


class Jarvis(object):

    def __init__(self):
        #Initialise speech server
        self.ss = SpeechServer()
        #Initialise Speech reconizer
        self.sr = SpeechReco()
        #Initialise command listener
        self.wr = WriteReco()

    def start(self):
            # Start speech server
            self.ss.start()
            # start speech reco
            self.sr.start()
            # Start commande reco
            self.wr.start()

    


