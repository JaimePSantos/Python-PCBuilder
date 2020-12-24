from src.money import MyMoney

class GraphCard:
    model=""

    def __init__(self,model,price):
        self.model = model
        self.price = MyMoney(price) 

    def getModel(self):
        return self.model

    def getPrice(self):
        return self.price

    def __str__(self):
        return(type(self).__name__+"> Model: "+self.model+"\tPrice: "+str(self.price))

class Processor:
    model=""

    def __init__(self,model,price):
        self.model = model
        self.price = MyMoney(price) 

    def __str__(self):
        return(type(self).__name__+"> Model: "+self.model+"\tPrice: "+str(self.price))

class PCPart:

    def __init__(self,partType, model, price):
        self.partType = partType
        self.model = model
        self.price = price

    def makePart(self):
        if self.partType == "cpu":
            pcPart = Processor(self.model,self.price)
        elif self.partType == "video-card":
            pcPart = GraphCard(self.model,self.price)
        else:
            print("invalid part")
            return
        return pcPart

    def __str__(self):
        return(str(self.pcPart))
    
