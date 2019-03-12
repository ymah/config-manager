import json
import Task
import Queue
import Hardware
import string
import random




class Partition:


    def __init__(self,partJSON):
        self._id = partJSON['id']
        self.name = partJSON['name']
        self.priority = partJSON['priority']
        self.partitionIdentifier = self.name + str(self._id)
        self.stackSize = 128
        self.parameters= 0
        self.accessibleHw = partJSON['hw-access']
        self.accessibleQueue = partJSON['queue-access']


    def generate(self):
       return ("xProtectedTaskCreate(&%s,\"%s\",%d,%s,%d,%d);"%(self.partitionIdentifier,self.name,self.stackSize,self.parameters,self.priority,0))
