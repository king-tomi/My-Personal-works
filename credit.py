class CreditCard:
    
    #this is an initializer
    def __init__(self,customer,bank,acnt,balance,limit):
        self.customer = customer
        self.bank = bank
        self.acnt = acnt
        self.balance = balance
        self.limit = limit
        
   def get_name(self):
       return self.customer
       
   def get_bank(self):
       return self.bank
       
   def get_balance(self):
       return self.balance
       
   def get_acnt(self):
       return self.acnt
       
       
   @staticmethod
   def print_hi():
       print("Hi")
       
       
       
if __name__ == "__main__":
    card = CreditCard("John Doe","GT","0455 9867 1234 7634",400,40000)
    print(card.customer)
    print(card.print_hi())