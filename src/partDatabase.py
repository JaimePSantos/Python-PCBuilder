from src.pcParts import Processor, GraphCard, PCPart
import operator
import csv
import os

class PartDatabase:
    processors = {}
    graphicsCards = {}
    processorList = []
    graphicsCardList = []

    def __init__(self,fileName):
        self.loadFile(fileName)
        self.buildProcessorList()
        self.buildGraphicsCardList()

    def loadFile(self,fileName):
        try:
            with open(fileName,'r') as f:
                lines = f.readlines()
                for line in lines:
                    parsedLine = line.strip()
                    parsedLine = parsedLine.split(',')
                    if parsedLine[0]=='video-card' or parsedLine[0]=='cpu':
                        pcPart = self.buildPart(parsedLine)
                        print(pcPart)
                    else:
                        continue
        except:
            print("%s could not be found."%fileName)

    def buildPart(self,parsedLine):
        partType = parsedLine[0]
        partManufacturer = parsedLine[1]
        partModel = parsedLine[2]
        partPrice = parsedLine[3]
        pcPart = PCPart(partType,partModel,partPrice).makePart()
        return pcPart

    def buildProcessorList(self):
        for processor in self.processors:
            proc = Processor(processor,self.processors[processor])
            self.processorList.append(proc)
        return self.processorList

    def buildGraphicsCardList(self):
        for graphicsCard in self.graphicsCards:
            gc = GraphCard(graphicsCard,self.graphicsCards[graphicsCard])
            self.graphicsCardList.append(gc)
        return self.graphicsCardList

    def sortByCheapestGraphicsCards(self):
        cheapest = sorted(self.graphicsCardList,key=operator.attrgetter('price'))
        for gc in cheapest:
            gc.printGraphCard()
        return cheapest

    def sortByCheapestProcessor(self):
        cheapest = sorted(self.processorList,key=operator.attrgetter('price'))
        for pu in cheapest:
            pu.printProcessor()
        return cheapest

    def printProcessors(self):
        for processor in self.processorList:
            print(processor)

    def printGraphicsCards(self):
        for graphicsCard in self.graphicsCardList:
            print(graphicsCard)

    def __str__(self):
        partString = ""
        for processor in self.processorList:
            partString+=str(processor)+'\n'
        for graphicsCard in self.graphicsCardList:
            partString+=str(graphicsCard)+'\n'

        return partString
