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
        self.myMoney = Money(self.myAmt,self.myCurrency)

    def detectCurrency(self,moneyString):
        if '$' in moneyString:
            return 'USD'
        elif '€' in moneyString:
            return 'EUR'
        else:
            return 'Undefined'

    def __str__(self):
        return str(self.myMoney)