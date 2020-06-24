print("Hello Group1")

def calculator(a,b):
  Sum = a+b
  product = a*b
  print(Sum, product)

calculator(3,4)

print ("Hello")

class TelephoneBills:
    def __init__(self,billID,year,month,day,payvalue, name, company, paymentstatus, reminder):
        self._ID = billID
        self._paydate = (year,month,day)
        self._payvalue = payvalue
        self.name= name
        self.company= company
        self.paymentstatus= paymentstatus
        self.reminder=reminder
