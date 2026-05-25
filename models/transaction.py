from datetime import datetime
class Transaction:
   t_id :int
   t_type :str
   amount :float
   category :str
   description :str
   date :datetime.now()

   def __init__(self, t_id, t_type, amount, category, description):
       self.id = t_id
       if type!=("income","expense"):
           exit("Invalid transaction type")
       else:
        self.type = t_type  # 'income' or 'expense'
       self.amount = amount

       self.category = category
       self.description = description
       self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   def to_dict(self):
       return {
           'id' : self.id,
           'type' : self.type,
           'amount' : self.amount,
            'category' : self.category,
           'description' : self.description,
           'date' : self.date
       }

   @staticmethod
   def from_dict(data):
       return Transaction(data['id'], data['type'], data['amount'], data['category'], data['description'])
   def desplay(self):
       print(str(self.id) + "|" + self.type + "|" + str(self.amount) + "|" +  self.category + "|" + self.description)


