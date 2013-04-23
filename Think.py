#!/usr/bin/env python
from Motorium import *
from DbCom import *
import sys
import random


class Think(object):

    def checkcommand(self, command):
        action = {
            'sarah': self.say,
            'open': self.confirm,
            'add note': self.testdbcom,
            'bye': self.close,
        }.get(command, self.dontknow)
        action()

    def say(self):
        Motorium.say("I love you Sarah!")

    def close(self):
        Motorium.say("byebye sir")
        sys.exit(0)

    def dontknow(self):
        Motorium.say("Sorry, I do not know this command.")

    def testdbcom(self):
        dbcom = DbCom()

    def confirm(self):
        rep_id = random.randrange(1, 4)
        if rep_id == 1:
            Motorium.say("Right now sir!")
        elif rep_id == 2:
            Motorium.say("Yes sir!")
        elif rep_id == 3:
            Motorium.say("I will do it for you sir!")
