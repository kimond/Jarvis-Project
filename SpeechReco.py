#!/usr/bin/env python
import threading
from Think import *
import pyjulius
import Queue


class SpeechReco(threading.Thread):

    def run(self):
        # Initialize and try to connect
        self.client = pyjulius.Client('localhost', 10500)
        self.client.modelize = True
        try:
            self.client.connect()
        except pyjulius.ConnectionError:
            print 'Start julius as module first!'
            sys.exit(1)
        # Start listening to the server
        self.client.start()
        self.result = ""
        self.think = Think()
        while(True):
            self.RequestMsg()

    def RequestMsg(self):
        sentence = ""
        try:
            self.result = self.client.results.get(True)
        except Queue.Empty:
            pass
        if isinstance(self.result, pyjulius.Sentence):
            for word in self.result.words:
                sentence += "{0} ".format(word)
            print sentence
            if(sentence != ""):
                self.think.checkcommand(sentence)

