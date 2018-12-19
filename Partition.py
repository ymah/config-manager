import json
import Task
import Queue
import Hardware





class Partition:



    def __init__(self,partJSON):
        self._id = partJSON['id']
        self.name = partJSON['name']
        self.priority = partJSON['priority']
        self.function = partJSON['function']
        self.stackSize = partJSON['stackSize']
        self.parameters= partJSON['parameters']
        self.accessibleHw = partJSON['hw-access']
        self.accessibleQueue = partJSON['queue-access']
    def generate(self):
       print("xProtectedTaskCreate(&%s,%s,%d,%s,%d,%d);"%(self.function,self.name,self.stackSize,self.parameters,self.priority,0))





