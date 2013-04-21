#!/usr/bin/env python
import sys
import pyttsx
import aspeak


class Motorium(object):
    # Initialise le moteur de speech
    engine = pyttsx.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', "english-us")

    @staticmethod
    def say(text):
        Motorium.engine.say(text)
        Motorium.engine.runAndWait()
        print(text)

