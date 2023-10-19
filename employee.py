"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=None, commission=None, percommission=None, contract=None, percontract=None,bonus=None):
        self.name = name
        if contract is not None and bonus is not None:
            self.contract=contract
            self.percontract=percontract
            self.bonus=bonus
            self.pay=(contract*percontract)+bonus
            self.descripe="works on a contract of " + str(self.contract) + " hours at " + str(self.percontract)+ "/hour and receives a bonus commission of " + str(self.bonus) + ". Their total pay is "+str(self.pay)+"."
        elif salary is not None and bonus is not None:
            self.salary = salary
            self.bonus = bonus
            self.pay = salary + bonus
            self.descripe="works on a monthly salary of "+str(self.salary)+" and receives a bonus commission of "+ str(self.bonus)+". Their total pay is "+str(self.pay)+"."
        elif commission is not None and contract is not None:
            self.commission = commission
            self.percommission = percommission
            self.contract = contract
            self.percontract = percontract
            self.pay = (commission*percommission)+(contract*percontract)
            self.descripe="works on a contract of"+ str(self.contract)+" hours at "+ str(self.percontract)+"/hour and receives a commission for "+ str(self.commission)+" contract(s) at "+str(self.percommission)+"/contract. Their total pay is "+str(self.pay)+"."
        elif salary is not None and contract is not None:
            self.salary = salary
            self.contract = contract
            self.percontract = percontract
            self.pay = salary + (contract*percontract)
            self.descripe="works on a monthly salary of"+str(self.salary)+" and receives a commission for"+ str( self.contract) +"contract(s) at "+str(self.percontract)+"/contract. Their total pay is "+str(self.pay)+"."
        elif salary is None and contract is not None:
            self.contract = contract
            self.percontract = percontract
            self.pay = (contract*percontract)
            self.descripe="works on a contract of"+ str(self.contract)+" hours at "+ str(self.percontract)+"/hour. Their total pay is "+str(self.pay)+"."
        else:
            self.salary=salary
            self.pay=salary
            self.descripe="works on a monthly salary of "+str(self.salary)+". Their total pay is "+str(self.pay)+"."



    def get_pay(self):
        return self.pay

    def __str__(self):
        return self.name+ self.descripe


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', None, None, None, 100, 25, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, None, None, 4, 200, None)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', None, 3, 220, 150, 25, None)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, None, None, None, None, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', None, None, None, 120, 30, 600)
