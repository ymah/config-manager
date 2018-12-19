import json
import Task
import Queue
import Hardware





class Hardware:



    def __init__(self,hdwreJSON):
        self._id = hdwreJSON['id']
        self.name = hdwreJSON['hardware-name']

    def generate(self):
        print("giveHardwareAccess(%d,%s)"%(self._id,self.name))
