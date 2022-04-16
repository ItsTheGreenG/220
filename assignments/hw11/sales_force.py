"""
Owen Schlagenhaft
Creating a Class to accept a file and modify

sales_force.py

I Certify that this work is mine and mine only.
"""

from sales_person import *
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        for i in file:
            i = i.strip("\n")
            self.sales_people.append(i)
        pass

    def quota_report(self, quota):
        employee_list = []
        for employees in self.sales_people:
            employees = employees.split(",")
            for i in employees:
                employee_id = employees[0]
                name = employees[1]
                totalsales = employees[2]
                totalsales = totalsales.split()
            total = 0
            for i in totalsales:
                i = int(i)
                total = i + total
            met_quota = False

            if total >= quota:
                met_quota = True


            employee_list.append((int(employee_id), str(name), float(total), bool(met_quota)))
        return employee_list

    def top_seller(self):
        totalsaleslist = []
        for employees in self.sales_people:
            winner - []
            i = i.split(",")
            for element in i:
                sales = i[2]
                sales = sales.split()
            total = 0
            total = 0
            for i in sales:
                i = int(i)
                total += i
            sales_list.append(total)

        print(max(sales_list))
    def individual_sales(self, employee_id):
        if employee_id == self.sales_people:
            return
        else:
            return None


#Test Code
sales_list = SalesForce()
sales_list.add_data('testfile.txt')

sales_list.individual_sales(334)

