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
        self.binary_location = partJSON['binary-location']

    def generate(self):
        binary = ("extern uint32_t _%s, _e%s;"%(self.partitionIdentifier,self.partitionIdentifier))
        size = ("uint32_t size_%s = _e%s - _%s;"%(self.partitionIdentifier,self.partitionIdentifier,self.partitionIdentifier))
        entry = ("uint32_t %s;\n"%(self.partitionIdentifier))
        return ("%s\n"
                "%s\n"
                "%s\n"
                "BaseType_t %s_handler = "
                "xProtectedTaskCreate(&%s,\"%s\",%size_%s,%s,%d,%d);"
                %(binary,size,entry,self.name,self.name,self.partitionIdentifier,self.name,self.partitionIdentifier,self.parameters,self.priority,0))


    def getAssemblySource(self):
        return (".section .%s\n"
                ".incbin \"%s\"\n"
                %(self.partitionIdentifier,self.binary_location))

    def getLinkerScript(self):
        return (".%s : ALIGN(4096) { \n"
                " _%s = . ; \n "
                "*(.%s) \n "
                ". = ALIGN(0x40000); \n"
                " _e%s = .;\n  }\n"
                %(self.partitionIdentifier,self.partitionIdentifier,self.partitionIdentifier,self.partitionIdentifier))
