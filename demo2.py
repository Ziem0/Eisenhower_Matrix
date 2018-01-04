# class Employee:
#     raise_amt = 1.04
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
    
#     def fullname(self):
#         return ("{} {}".format(self.first, self.last))

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

# class Developer(Employee):
#     raise_amt = 1.10
#     def __init__(self, first, last, pay, pro_lang):
#         super().__init__(first, last, pay)
#         self.pro_lang = pro_lang

# class Manager(Employee):
#     def __init__(self, first, last, pay):
#         super().__init__(first, last, pay)
#         self.employees = []

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
    
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('--->', emp.fullname())

# dev1 = Developer('Ziemo', 'Ando', 90000, 'Python')
# dev2 = Developer('Ziemo2', 'Ando2', 10000, 'Java')
# mgr1 = Manager('Ala', 'Bala', 99900000)
# mgr1.add_emp(dev1)
# mgr1.add_emp(dev2)
# mgr1.print_emps()
################################################################################
class Data:
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day
        
    @classmethod
    def data(cls, data):
        year, month, day = data.year,data.month,data.day         
        return cls(year, month, day)

x = Data.data(datetime.date.today())
print(x.day)
