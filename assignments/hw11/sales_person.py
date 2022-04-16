"""
Owen Schlagenhaft
Creating a Class to accept a file and modify

sales_force.py

I Certify that this work is mine and mine only.
"""
import math
class Salesperson:


    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []


    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sales):
        self.sales.append(sales)


    def total_sales(self):
        totalsales = 0
        for i in self.sales:
            totalsales = totalsales + i
        return totalsales

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        string = "" + str(self.get_id()) +" - " + str(self.name) + " : " + str(self.total_sales())
        return string



    #def met_quota(quota):


#create instance of the OBJECT
owen = Salesperson(123,"Owen")

#Test getter methods
print(owen.get_id())
print(owen.get_name())

#Test setter
owen.set_name("Stu")
print(owen.get_name())
owen.set_name("Owen")

#test sales
owen.enter_sale(12)
owen.enter_sale(14)
owen.enter_sale(199)
print(owen.sales)
stu = Salesperson(420, "Stu Poo")
stu.enter_sale(15)
stu.enter_sale(4)
stu.enter_sale(25)
print(stu.total_sales())
print(owen.compare_to(stu))
print(owen)



