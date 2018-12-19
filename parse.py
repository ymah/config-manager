import Domain
import Task
import Queue
import Hardware


import json
import sys


def readJsonFile(jsonFile):
    f = open(jsonFile,'r')
    dataFile = json.load(f)
    f.close()
    return (dataFile)



def domFromJson(jsonData):
    domain = Domain.Domain(jsonData)
    domain.generate()



if __name__ == '__main__':
    jsonData = readJsonFile(sys.argv[1])
    domFromJson(jsonData)
