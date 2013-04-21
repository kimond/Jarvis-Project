#!/usr/bin/env python
import threading
import subprocess
import os


class SpeechServer(threading.Thread):

    def run(self):
        #subprocess.call(["./startjulius.sh"])
        os.system("./startjulius.sh")
