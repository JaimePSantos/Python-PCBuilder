# This is a sample Python script.
from src.graphCard import GraphCard
from src.processor import Processor
from src.partDatabase import PartDatabase
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # vc = GraphCard("Amd",500)
    # vc.printGraphCard()
    # pu = Processor("Amd",600)
    # pu.printProcessor()
    os.chdir('src')
    fileName = 'parts.txt'
    pDb = PartDatabase(fileName)
    # pDb.printProcessors()
    # pDb.printGraphicsCards()
    print(pDb)
    # print(pDb.sortByCheapestGraphicsCards())
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
