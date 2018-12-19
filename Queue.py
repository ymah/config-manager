import json
import queue
import Queue
import Hardware





class Queue:



    def __init__(self,queueJSON):
        self._id = queueJSON['id']
        self.name = queueJSON['taskName']
        self.queueLength = queueJSON['queue-size']
        self.itemSize = queueJSON['element-size']
    def generate(self):
        print("xQueueCreate(%d,%d);"%(self.queueLength,self.itemSize))




