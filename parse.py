import Domain
import Task
import Queue
import Hardware


import json
import sys
import os
import shutil
import datetime


initFileTemplate = "initTemplate.c"
initFile = "init.c"

def copy_rename(old_file_name, new_file_name,domainFolder):
    if not os.path.exists(domainFolder):
        os.makedirs(domainFolder)

    src_dir= os.curdir
    dst_dir= os.path.join(os.curdir , domainFolder)
    src_file = os.path.join(src_dir, old_file_name)
    shutil.copy(src_file,dst_dir)
    dst_file = os.path.join(dst_dir, old_file_name)

    new_dst_file_name = os.path.join(dst_dir, new_file_name)
    os.rename(dst_file, new_dst_file_name)


def printTasks(tasks,file):
    for t in tasks:
        file.append(t+"\r\n")

def printPartition(partitions,file):
    for p in partitions:
        file.append(p+"\r\n")

def printQueues(queues,file):
    for q in queues:
        file.append(q+"\r\n")

def printHardware(hardware,file):
    for h in hardware:
        file.append(h+"\r\n")


def domFromJson(jsonData,file):
    domain = Domain.Domain(jsonData)
    domain.generate()
    return domain

def generateInitFile(domain):
    dom = domain.getDomain()
    tasks = dom[0]
    partitions = dom[1]
    queues = dom[2]
    hardware = dom[3]

    initFileName = open(initFileTemplate,'r')
    fileName = open(domain.getName()+"/"+initFile,'w')

    copy = False
    for line in initFileName:
        if "//_GENERATED_SOURCE_CODE" in line:
            copy = True
        elif "//_END_OF_CODE" in line:
            copy = False
        elif copy:
            printTasks(tasks,fileName)
            printPartition(partitions,fileName)
            printQueues(queues,fileName)
            printHardware(hardware,fileName)

    fileName.close()
    initFileName.close()





def readJsonFile(jsonFile):
    f = open(jsonFile,'r')
    dataFile = json.load(f)
    f.close()
    return (dataFile)

if __name__ == '__main__':
    jsonData = readJsonFile(sys.argv[1])
    domain = domFromJson(jsonData,0)
    domainName = domain.getName()

    print("Create init file")
    copy_rename(initFileTemplate,initFile,domainName)

    generateInitFile(domain)
