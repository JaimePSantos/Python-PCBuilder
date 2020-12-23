class Processor:
    model=""
    price=0

    def __init__(self,model,price):
        self.model = model
        self.price = price

    def __str__(self):
        return(type(self).__name__+"> Model: "+self.model+"\tPrice: "+str(self.price))