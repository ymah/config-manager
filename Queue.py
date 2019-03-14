import json
import queue
import Queue
import Hardware





class Queue:



    def __init__(self,queueJSON):
        self._id = queueJSON['id']
        self.name = queueJSON['queue-name']
        self.queueLength = queueJSON['queue-size']
        self.itemSize = queueJSON['element-size']

    def generate(self):
        return ("QueueHandle_t %s ="
                " QueuexQueueCreate(%d,%d);\n"
                %(self.name,self.queueLength,self.itemSize))
