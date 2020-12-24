from src.pcParts import Processor, GraphCard
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
                print("1")
                lines = csv.reader(f,delimiter= ',')
                print("2")
                print(lines)
                for line in lines:
#                    if("cpu" in line[0].lower()):
#                        print(line)
#                        self.processors[line[1]] = line[2]
#                    if("gpu" in line[0].lower()):
#                        print(line)
#                        self.graphicsCards[line[1]] = line[2]
#                    else:
#                        print("bla") 
#                        continue
                    if line[0] != "gpu" and line[0]!= "cpu":
                        print(line)
                    else:
                        continue
        except:
            print("%s could not be found."%fileName)

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
