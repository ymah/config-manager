import json
import Task
import Queue
import Hardware
import Partition




class Domain:

    listOfTask = []
    listOfPartition = []
    listOfQueues = []
    listOfHardware = []

    domain = []

    def __init__(self,domainJSON):
        self._id = domainJSON['id']
        self.name = domainJSON['domainName']
        self.subTask = []
        self.subPartition = []
        self.queue = []
        self.hardware = []

        for subTask in domainJSON['tasks']:
            self.subTask.append(Task.Task(subTask))

        for subPartition in domainJSON['sub-partitions']:
            self.subPartition.append(Partition.Partition(subPartition))

        for queue in domainJSON['queues']:
            self.queue.append(Queue.Queue(queue))

        for hw in domainJSON['hardware']:
            self.hardware.append(Hardware.Hardware(hw))


    def generate(self):

        for subTask in self.subTask:
            self.listOfTask.append(subTask.generate())

        self.domain.append(self.listOfTask)
        for subPart in self.subPartition:
            self.listOfPartition.append(subPart.generate())
        self.domain.append(self.listOfPartition)
        for qu in self.queue:
            self.listOfQueues.append(qu.generate())
        self.domain.append(self.listOfQueues)
        for hw in self.hardware:
            self.listOfHardware.append(hw.generate())
        self.domain.append(self.listOfHardware)


    def getDomain(self):
        return self.domain

    def getName(self):
        return self.name
