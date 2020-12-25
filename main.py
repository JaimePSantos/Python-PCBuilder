from src.partDatabase import PartDatabase
from src.buildDatabase import DatabaseBuilder 
from src.money import MyMoney
import os
from pcpartpicker import API
from moneyed import Money
from collections import defaultdict

def main():
    os.chdir('src')
    fileName = 'parts.txt'
    builder = DatabaseBuilder(fileName) 
    builder.buildFile()
    pDb = PartDatabase(fileName)
    test = defaultdict(list)
    partsDict = pDb.getPartDict()
    partsList = pDb.sortByCheapest('cpu')
    for cpu in partsList:
        print(cpu)
    # print(pDb.sortByCheapestGraphicsCards())

if __name__ == '__main__':
    main()

