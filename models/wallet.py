from finance_tracker.models.transaction import Transaction


class Wallet:
    owner :str
    transactions :[]
    def __init__(self, owner, transactions):
        self.owner = owner
        self.transactions = transactions
    def add_income(self, amount, category, description):
        t = Transaction(len(self.transactions)+1,"income", amount, category, description)
        self.transactions.append(t)
        print("income added to wallet")
    def add_expense(self, amount, category, description):
        t = Transaction(len(self.transactions)+1,"expense", amount, category, description)
        self.transactions.append(t)
        print("expense added to wallet")
    def get_total(self):
        total =0
        for t in self.transactions:
            total += t.amount

        return total
    def get_total_income(self):
        total =0
        for t in self.transactions:
            if(t.type == "income"):
                total += t.amount
        return total
    def get_total_expense(self):
        total =0
        for t in self.transactions:
            if(t.type == "expense"):
                total += t.amount
        return total
    def get_by_category(self, category):
        tl= []
        for t in self.transactions:
            if t.category == category:
                tl.append(t)
        return tl
    def get_static(self):
       if self.get_by_category("income")>self.get_by_category("expense")  :
        print("balenc: "+str(self.get_total())+"income : "+str(self.get_total_income())+"expense : "+str(self.get_total_expense())+"top category:income")
       else:
           print("balenc: " + str(self.get_total()) + "income : " + str(self.get_total_income()) + "expense : " + str(
               self.get_total_expense()) + "top category:expense")
    def get_mountly_static(self,date):
        for t in self.transactions:

            if(t.date.startswith(date)):
               print(t.desplay())




