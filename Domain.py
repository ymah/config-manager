import json
import Task
import Queue
import Hardware
import Partition




class Domain:



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
        print("/*")
        print("Creating domain %s"%(self.name))
        print("*/")

        print("//Creating tasks if any")
        for subTask in self.subTask:
            subTask.generate()
        print("//Creating sub-partitions if any")
        for subPart in self.subPartition:
            subPart.generate()
        print("//Creating queues if any")
        for qu in self.queue:
            qu.generate()
        print("//Enabling hardware access if any")
        for hw in self.hardware:
            hw.generate()


