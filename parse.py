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

assemblyFile = "partitions.S"

linkerFileTemplate = "linkerTemplate.ld"



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


def commentary(str,file):
    file.append("\n//%s\n"%(str))

def printTasks(tasks,file):
    commentary("Create Tasks",file)
    for t in tasks:
        file.append(t+"\n")

def printPartition(partitions,file):
    commentary("Create partitions",file)
    for p in partitions:
        file.append(p+"\n")

def printQueues(queues,file):
    commentary("Creates queues",file)
    for q in queues:
        file.append(q+"\n")

def printHardware(hardware,file):
    commentary("Allow hardware access to partitions",file)
    for h in hardware:
        file.append(h+"\n")


def readJsonFile(jsonFile):
    f = open(jsonFile,'r')
    dataFile = json.load(f)
    f.close()
    return (dataFile)


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


    with open(initFileTemplate,'r') as fileName:
        in_file = fileName.readlines()

    copy = False
    out_file = []
    for line in in_file:
        out_file.append(line)
        if '//_GENERATED_SOURCE_CODE' in line:
            out_file.append("\r\n")
            printTasks(tasks,out_file)
            printPartition(partitions,out_file)
            printQueues(queues,out_file)
            printHardware(hardware,out_file)

    with open(domain.getName()+'/'+initFile,'w') as outFile:
        outFile.writelines(out_file)

    outFile.close()

def generateLinkerFile(domain):
    partitions = domain.getSubPartitions()


    with open(linkerFileTemplate,'r') as fileName:
        in_file = fileName.readlines()

    copy = False
    out_file = []
    for line in in_file:
        out_file.append(line)

        if "/* START OF PARTITIONS LINKING */" in line:

            for p in partitions:
                out_file.append("\n")
                out_file.append(p.getLinkerScript())

    with open(domain.getName()+'/'+"linker.ld",'w') as outFile:
        outFile.writelines(out_file)

    outFile.close()



def generateInitFile(domain):
    dom = domain.getDomain()
    tasks = dom[0]
    partitions = dom[1]
    queues = dom[2]
    hardware = dom[3]


    with open(initFileTemplate,'r') as fileName:
        in_file = fileName.readlines()

    copy = False
    out_file = []
    for line in in_file:
        out_file.append(line)
        if '//_GENERATED_SOURCE_CODE' in line:
            out_file.append("\n")
            printTasks(tasks,out_file)
            printPartition(partitions,out_file)
            printQueues(queues,out_file)
            printHardware(hardware,out_file)

    with open(domain.getName()+'/'+initFile,'w') as outFile:
        outFile.writelines(out_file)

    outFile.close()












def generateAssemblyFile(domain):
    partitions = domain.getSubPartitions()

    with open(domain.getName()+"/"+assemblyFile,'w') as assFile:
        for part in partitions:
            assFile.write(part.getAssemblySource()+"\r\n")



if __name__ == '__main__':
    jsonData = readJsonFile(sys.argv[1])
    domain = domFromJson(jsonData,0)
    domainName = domain.getName()

    print("Create init file")
    copy_rename(initFileTemplate,initFile,domainName)

    generateInitFile(domain)
    generateAssemblyFile(domain)

    copy_rename(linkerFileTemplate,"linker.ld",domainName)
    generateLinkerFile(domain)
