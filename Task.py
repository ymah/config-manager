import json
import Task
import Queue
import Hardware





class Task:



    def __init__(self,taskJSON):
        self._id = taskJSON['id']
        self.name = taskJSON['name']
        self.priority = taskJSON['priority']
        self.function = taskJSON['function']
        self.stackSize = taskJSON['stackSize']
        self.parameters= taskJSON['parameters']

    def generate(self,):
        return "xTaskCreate(&%s,\"%s\",%d,%s,%d,%d);"%(self.function,self.name,self.stackSize,self.parameters,self.priority,0)
