from src.partDatabase import PartDatabase
from src.buildDatabase import DatabaseBuilder 
from src.money import MyMoney
import os
from pcpartpicker import API
from moneyed import Money

def main():
    os.chdir('src')
    fileName = 'parts.txt'
#    builder = DatabaseBuilder(fileName) 
#    builder.buildFile()
    pDb = PartDatabase(fileName)
    pDb.printProcessors()
    pDb.printGraphicsCards()
    #print(pDb)
    # print(pDb.sortByCheapestGraphicsCards())

if __name__ == '__main__':
    main()

