from moneyed import Money

class MyMoney:
    moneyStringList = []
    myCurrency = ""
    myAmt = "0"

    def __init__(self,moneyString):
        self.myCurrency = self.detectCurrency(moneyString)
        if self.myCurrency == 'USD':
            self.moneyStringList = moneyString.split('$')
            self.myAmt = moneyStringList[1]
        elif self.myCurrency == 'EUR': 
            self.moneyStringList = moneyString.split(' ')
            self.myAmt = self.moneyStringList[0]  
        else:
            print("String: "+moneyString+"\t"+self.myCurrency + " is not a valid currency.")
            return
        self.myMoney = Money(self.myAmt,self.myCurrency)

    def detectCurrency(self,moneyString):
        if '$' in moneyString:
            return 'USD'
        elif '€' in moneyString:
            return 'EUR'
        else:
            return 'Undefined'

    def __lt__(self,other):
        if  self.myMoney < other.myMoney:
            return True
        else:
            return False

    def __gt__(self,other):
        if  self.myMoney > other.myMoney:
            return True
        else:
            return False

    def __str__(self):
        return str(self.myMoney)
