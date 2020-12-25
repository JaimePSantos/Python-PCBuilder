from src.pcParts import Processor, GraphCard, PCPart
import operator
import csv
import os
from collections import defaultdict 

class PartDatabase:
    partsList = [] 
    parsedFile= []
    partsDict = {}

    def __init__(self,fileName):
        self.partsList = []
        self.parsedFile = self.loadFile(fileName)
        self.partsDict = self.buildPartDatabase(self.parsedFile)

    def loadFile(self,fileName):
        try:
            with open(fileName,'r') as f:
                lines = f.readlines()
                for line in lines:
                    parsedLine = line.strip()
                    parsedLine = parsedLine.split(',')
                    if self.validPart(parsedLine[0]): 
                        self.parsedFile.append(parsedLine)
                    else:
                        continue
        except:
            print("%s could not be found."%fileName)
        return self.parsedFile

    def buildPartDatabase(self,parsedFile):
        partsDictAux = defaultdict(list)
        for parsedLine in parsedFile:
            partType = parsedLine[0]
            partManufacturer = parsedLine[1]
            partModel = parsedLine[2]
            partPrice = parsedLine[3]
            pcPart = PCPart(partType,partModel,partPrice).makePart()
            partsDictAux[partType].append(pcPart)
        return partsDictAux

    def sortByCheapest(self,part):
        partsListAux = self.getPartList(part)
        cheapest = sorted(partsListAux, key= operator.attrgetter('price'))
        return cheapest

    def validPart(self,parsedLine):
        if parsedLine=='video-card' or parsedLine=='cpu':
            return True
        else:
            return False

    def getPartList(self,part):
        return self.partsDict[part]

    def getPartDict(self):
        return self.partsDict

    def __str__(self):
        partString = ""
        for processor in self.processorList:
            partString+=str(processor)+'\n'
        for graphicsCard in self.graphicsCardList:
            partString+=str(graphicsCard)+'\n'

        return partString
