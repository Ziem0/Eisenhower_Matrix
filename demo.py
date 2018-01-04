# import os
# import sys
# import csv
# import datetime

# class TodoItem:

#     def __init__(self, title, deadline):
#         self.title = title
#         self.deadline = deadline
#         self.is_done = False
#         if not isinstance(title, str):
#             raise TypeError("Invalid title format")
#         if not isinstance(deadline, datetime.date):
#             raise TypeError('Deadline must be a datetime type')

#     def mark(self):
#         self.is_done = True

#     def unmark(self):
#         self.is_done = False

#     def __str__(self):
#         x = ' '
#         if self.is_done:
#             x = 'x'
#         return "[{}] {} {}".format(x, str(self.deadline.day)+'-'+str(self.deadline.month), self.title) 

# class TodoQuarter:
    
#     def __init__(self):
#         self.todo_items = []

#     def sort_items(self):
#         self.todo_items = sorted(self.todo_items, key=lambda task: task.deadline)

#     def add_item(self, title, deadline):
#         if not isinstance(deadline, datetime.date):
#             raise TypeError('Deadline must be a datetime type')
#         else:
#             self.todo_items.append(TodoItem(title, deadline))
#             self.sort_items()

#     def remove_item(self, index):
#         self.todo_items.remove(self.todo_items[index])

#     def archive_items(self):
#         for n, task in enumerate(self.todo_items):
#             if task.is_done:
#                 self.remove_item(n)

#     def get_item(self, index):
#         if self.todo_items[index] in self.todo_items:
#             return self.todo_items[index]
#         else:
#             raise IndexError('Index is out of range')

#     def __str__(self):
#         output = ''
#         for n, task in enumerate(self.todo_items, 1):
#             output += '\n' + str(n) + '. ' + str(task) + '\n'
#         return output


# class TodoMatrix:
    
#     def __init__(self):
#         self.todo_quarters = {'IU':TodoQuarter(),    
#                               'IN':TodoQuarter(),
#                               'NU':TodoQuarter(),
#                               'NN':TodoQuarter()}
        
#     def get_quarter(self, status):
#         for key in self.todo_quarters.keys():
#             if key == status:
#                 return self.todo_quarters[key]


#     def add_item(self, title, deadline, is_important=False):
#         if not isinstance(deadline, datetime.date):
#             raise TypeError('invalid format!')
#         else:
#             difference = (deadline - datetime.date.today()).days
#             if is_important and difference <= 3:
#                 self.todo_quarters['IU'].add_item(title, deadline)
#             elif is_important:
#                 self.todo_quarters['IN'].add_item(title, deadline)
#             elif difference <= 3:
#                 self.todo_quarters["NU"].add_item(title, deadline)
#             else:
#                 self.todo_quarters["NN"].add_item(title, deadline)

#     def add_items_from_file(self, file_name='todo_items_read_test.csv'):
#         if not os.path.isfile(file_name):
#             raise FileNotFoundError('File doesn\'t exist')
#         else:
#             with open(file_name, 'r') as f:
#                 reader = csv.reader(f, delimiter="|")
#                 for row in reader:
#                     title = row[0]
#                     day = int(row[1].split('-')[0])
#                     month = int(row[1].split('-')[1])
#                     deadline = datetime.date(2017, month, day)
#                     is_important = False
#                     if row[2]:
#                         is_important = True
#                     self.add_item(title, deadline, is_important)

#     def save_items_to_file(self, file_name='MySave.csv'):
#         with open(file_name, 'w') as f:
#             writer = csv.writer(f, delimiter='|')
#             for k,v in self.todo_quarters.items():
#                 for task in v.todo_items:
#                     if k == "IU" or k == "IN":
#                         writer.writerow([task.title, str(task.deadline.day)+'-'+str(task.deadline.month), 'important'])
#                     else:
#                         writer.writerow([task.title, str(task.deadline.day)+'-'+str(task.deadline.month), ''])
                            
#     def archive_items(self):
#         for lista in self.todo_quarters.values():
#             lista.archive_items()

#     def __str__(self):
#         final_out = ''  
#         for k,v in self.todo_quarters.items():
#             final_out += '\n' + str(k) + ':' + '\n' + str(v)+'\n'
        
#         return final_out






# def task_options(matrix, quarter):
#     while 1:
#         print('''
#                 1. Mark
#                 2. Unmark
#                 3. Remove task
#                 4. Back''')
        
#         try:
#             user = int(input('Choose option: '))
#             if user == 1:
#                 user2 = int(input('Choose which task you want to mark: '))
#                 matrix.get_quarter(quarter).get_item(user2-1).mark()
#             elif user == 2:
#                 user2 = int(input('Choose which task you want to unmark: '))
#                 matrix.get_quarter(quarter).get_item(user2-1).unmark()
#             elif user == 3:
#                 user2 = int(input('Choose which task you want to delete: '))
#                 matrix.get_quarter(quarter).remove_item(user2-1)
#             elif user == 4:
#                 break                
#         except ValueError:
#             print('Error')

# def quarter_options(matrix, quarter):
#     while 1:
#         print('''
#             1. Show quarter
#             2. Get task
#             3. Back\n''')

#         user = int(input('Choose option: '))
#         if user == 1:
#             print(matrix.get_quarter(quarter))
#         elif user == 2:
#             task_options(matrix, quarter)
#         elif user == 3:
#             break

# def show_quarter(matrix):
#     while 1:
#         print('''
#         1. IU 
#         2. IN 
#         3. NU 
#         4. NN
#         5. Back\n''')

#         user = int(input('Choose quarter: '))
#         if user == 1:
#             quarter_options(matrix, 'IU')
#         if user == 2:
#             quarter_options(matrix, 'IN')
#         if user == 3:
#             quarter_options(matrix, 'NU')
#         if user == 4:
#             quarter_options(matrix, 'NN')
#         if user == 5:
#             break
        

# def menu(matrix):
#     matrix.add_items_from_file()
#     os.system('clear')
#     while 1:
#         print('''
#                 Menu:
#                 1. Show all task
#                 2. Show quarter
#                 3. Add task
#                 4. Archive task
#                 5. Exit''')
#         try:
#             inn = int(input('Choose option: '))
#             if inn == 1:
#                 print(matrix)
#             elif inn == 2:
#                 show_quarter(matrix)
#             elif inn == 3:
#                 title = input('Choose a title: ')
#                 day = int(input('Choose day: '))
#                 month = int(input('Choose month: '))
#                 deadline = datetime.date(2017, month, day)
#                 is_important = int(input('Choose 1 for important or 0 for not important: '))
#                 matrix.add_item(title, deadline, is_important)
#             elif inn == 4:
#                 matrix.archive_items()
#             elif inn == 5:
#                 matrix.save_items_to_file()
#                 sys.exit()
#         except ValueError:
#             print('error')

# def main():
#     matrix = TodoMatrix()
#     menu(matrix)


# if __name__ == "__main__":
#     main()




####################################################3

# import os, sys
# import csv
# import datetime

# class TodoItem:
#     def __init__(self, title, deadline):
#         self.title = title
#         self.deadline = deadline
#         self.is_done = False
#         if not isinstance(title, str):
#             raise ValueError
#         if not isinstance(deadline, datetime.date):
#             raise ValueError
#     def mark(self):
#         self.is_done = True
#     def unmark(self):
#         self.is_done = False
#     def __str__(self):
#         out = ''
#         x = ''
#         if self.is_done:
#             x = 'x'
#         out = "[{}] {}-{} {}".format(x, self.deadline.day, self.deadline.month, self.title)
#         return out

# class TodoQuarter:
#     def __init__(self):
#         self.todo_items = []
#     def sort_items(self):
#         self.todo_items = sorted(self.todo_items, key=lambda task: task.deadline) 
#     def add_item(self, title, deadline):
#         if not isinstance(deadline, datetime.date):
#             raise TypeError('ups')
#         else:
#             self.todo_items.append(TodoItem(title, deadline))
#             self.sort_items            
#     def remove_item(self, index):
#         del self.todo_items[index]
#     def archive_items(self):
#         for task in self.todo_items:
#             if task.is_done:
#                 self.todo_items.remove(task)
#     def get_item(self, index):
#         if not self.todo_items[index] in self.todo_items:
#             raise IndexError
#         else:
#             return self.todo_items[index]
#     def __str__(self):
#         out = ''
#         for n,task in enumerate(self.todo_items,1):
#             out += '\n{}.{}\n'.format(n, task)
#         return out

# class TodoMatrix:
#     def __init__(self):
#         self.todo_quarters = {"IU":TodoQuarter(),
#                             'IN':TodoQuarter(),
#                             'NU':TodoQuarter(),
#                             'NN':TodoQuarter()}
#     def get_quarter(self, status):
#         for k,v in self.todo_quarters.items():
#             if k == status:
#                 return v

#     def add_item(self, title, deadline, is_important=False):
#         if not isinstance(deadline, datetime.date):
#             raise ValueError
#         else:
#             difference = (deadline - datetime.date.today()).days
#             if is_important and difference < 3:
#                 self.todo_quarters['IU'].add_item(title, deadline)
#             elif is_important:
#                 self.todo_quarters['IN'].add_item(title, deadline)
#             elif difference < 3:
#                 self.todo_quarters['NU'].add_item(title, deadline)
#             else:
#                 self.todo_quarters['NN'].add_item(title, deadline)
#     def add_items_from_file(self, file='todo_items_read_test.csv'):
#         if not os.path.isfile(file):
#             raise FileNotFoundError
#         else:
#             with open(file, 'r') as f:
#                 reader = csv.reader(f, delimiter='|')
#                 for row in reader:
#                     title = row[0]
#                     day = int(row[1].split('-')[0])
#                     month = int(row[1].split('-')[1])
#                     deadline = datetime.date(2017, month, day)
#                     is_important = False
#                     if row[2]:
#                         is_important = True
#                     self.add_item(title, deadline, is_important)
#     def save_items_to_file(self, file='todo_items_save_test.csv'):
#         with open(file, 'w') as f:
#             writer = csv.writer(f, delimiter="|")
#             for k,v in self.todo_quarters.items():
#                 for task in v.todo_items:
#                     if k == 'IU' or k == 'IN':
#                         writer.writerow([task.title, str(task.deadline.day)+'-'+str(task.deadline.month), 'important'])
#                     else:
#                         writer.writerow([task.title, str(task.deadline.day)+'-'+str(task.deadline.month), ''])
#     def archive_items(self):
#         for k,v in self.todo_quarters.items():
#             v.archive_items()
#     def __str__(self):
#         out = ''
#         for k,v in self.todo_quarters.items():
#             out += "{}:\n{}\n".format(k, v)
#         return out



# def task_options(matrix, v):
#     while 1:
#         print('''
#         1. Mark
#         2. Unmark
#         3. Remove
#         4. back''')
#         try:
#             user = int(input('option: '))
#             if user == 1:
#                 user = int(input('number task: '))
#                 matrix.get_quarter(v).get_item(user-1).mark()
#             elif user == 2:
#                 user = int(input('number task: '))
#                 matrix.get_quarter(v).get_item(user-1).unmark()
#             elif user == 3:
#                 user = int(input('number task to remove: '))
#                 matrix.get_quarter(v).remove_item(user-1)
#             elif user == 4:
#                 break
#         except ValueError:
#             print('no')

# def quarter_options(matrix, v):
#     while 1:
#         print('''
#         1. Show quarter
#         2. Get task
#         3. back''')
#         try:
#             user = int(input('option: '))
#             if user == 1:
#                 print(matrix.get_quarter(v))
#             elif user == 2:
#                 task_options(matrix, v)
#             elif user == 3:
#                 break
#         except ValueError:
#             print('no')

# def quarters(matrix):
#     quarters_dict = {1:'IU', 2:'IN', 3:'NU', 4:'NN'}
#     while 1:
#         print('''
#         1. IU
#         2. IN
#         3. NU
#         4. NN
#         5. back''')
#         try:
#             user = int(input('option: '))
#             if user == 5:
#                 break
#             else:
#                 for k, v in quarters_dict.items():
#                     if user == k:
#                         quarter_options(matrix, v)

#         except ValueError:
#             print('no')

# def menu(matrix):
#     os.system('clear')
#     matrix.add_items_from_file()
#     while 1:
#         print('''
#         menu:
#         1. SHow all
#         2. Get quarter
#         3. Add task
#         4. Exit''')
#         try:
#             user = int(input('option: '))
#             if user == 1:
#                 print(matrix)
#             elif user == 2:
#                 quarters(matrix)
#             elif user == 3:
#                 try:
#                     title = input('title: ')
#                     day = int(input('day: '))
#                     month = int(input('month: '))
#                     deadline = datetime.date(2017, month, day)
#                     is_important = int(input('1 for important, 0 for not important: '))
#                     if is_important != 0 and is_important != 1:
#                         raise OverflowError('1 or 2 only!')
#                 except ValueError:
#                     print('no')
#                 else:
#                     matrix.add_item(title, deadline, is_important)
#             elif user == 4:
#                 matrix.archive_items()
#                 sys.exit()
#         except ValueError:
#             print('no') 

# def main():
#     matrix = TodoMatrix()
#     menu(matrix)



# if __name__ == "__main__":
#     main()


#######################################################################################

import csv
import sys, os
from datetime import date

class TodoItem:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.is_done = False

        if not isinstance(self.title, str):
            raise TypeError
        if not isinstance(deadline, date):
            raise TypeError
    def mark(self):
        self.is_done = True
    def unmark(self):
        self.is_done = False
    def __str__(self):
        x = ' '
        if self.is_done:
            x = 'x'
        return "[{}] {}-{} {}".format(x, self.deadline.day, self.deadline.month, self.title)

class TodoQuarter:
    def __init__(self):
        self.todo_items = []
    def sort_items(self):
        self.todo_items = sorted(self.todo_items, key=lambda task: task.deadline)
    def add_item(self, title, deadline):
        if not isinstance(deadline, date):
            raise TypeError
        else:
            self.todo_items.append(TodoItem(title, deadline))
            self.sort_items()
    def remove_item(self, index):
        del self.todo_items[index]
    def archive_items(self):
        for task in self.todo_items:
            if task.is_done:
                self.todo_items.remove(task)
    def get_item(self, index):
        if self.todo_items[index] in self.todo_items:
            return self.todo_items[index]
        else: 
            raise IndexError
    def __str__(self):
        out = ''
        for n, task in enumerate(self.todo_items):
            out += "\n{}. {}\n".format(n, task)
        return out

class TodoMatrix:
    def __init__(self):
        self.todo_quarters = {'IU':TodoQuarter(),'IN':TodoQuarter(),'NU':TodoQuarter(),'NN':TodoQuarter()}
    def get_quarter(self, status):
        for k,v in self.todo_quarters.items():
            if k==status:
                return v
    def add_item(self, title, deadline, is_important=False):
        if not isinstance(deadline, date):
            raise TypeError
        else:
            difference = (deadline - date.today()).days
            if is_important and difference < 3:
                self.todo_quarters['IU'].add_item(title, deadline) 
            elif is_important:
                self.todo_quarters['IN'].add_item(title, deadline) 
            elif difference < 3:
                self.todo_quarters['NU'].add_item(title, deadline) 
            else:
                self.todo_quarters['NN'].add_item(title, deadline)
    def add_items_from_file(self, file='todo_items_read_test.csv'):
        if not os.path.isfile(file):
            raise FileNotFoundError
        else:
            with open(file, 'r') as f:
                reader = csv.reader(f, delimiter='|')
                for row in reader:
                    title = row[0]
                    day = int(row[1].split('-')[0])
                    month = int(row[1].split('-')[1])
                    deadline = date(2017, month, day)
                    is_important = False
                    if row[2]:
                        is_important = True
                    self.add_item(title, deadline, is_important)
    def save_items_to_file(self, file='todo_items_save_test.csv'):
        with open(file, 'w') as f:
            writer = csv.writer(f, delimiter="|")
            for k,v in self.todo_quarters.items():
                for task in v.todo_items:
                    if k=='IU' or k=='IN':
                        writer.writerow([task.title, task.deadline.day, task.deadline.month, 'important'])
                    else:
                        writer.writerow([task.title, task.deadline.day, task.deadline.month, ''])
    def archive_items(self):
        for k,v in self.todo_quarters.items():
            v.archive_items()
    def __str__(self):
        out = ''
        for k,v in self.todo_quarters.items():
            out += "\n{}:\n {}\n".format(k, v)
        return out






def task_options(matrix, quarter):
    while 1:
        print('''
        1. Mark
        2. Unmark
        3. Remove
        4. Back''')
        try:
            user = int(input('What to do?: '))
            if user == 1:
                user = int(input('Gimme task number: '))
                matrix.get_quarter(quarter).get_item(user).mark()
            elif user == 2:
                user = int(input('Gimme task number: '))
                matrix.get_quarter(quarter).get_item(user).unmark()
            elif user == 3:
                user = int(input('Gimme task number: '))
                matrix.get_quarter(quarter).remove_item(user)
            elif user == 4:
                break
        except ValueError as err:
            print(err)

def quarter_options(matrix, quarter):
    os.system('clear')
    while 1:
        print('''
        1. Show quarter
        2. Get task
        3. Back''')
        try:
            user = int(input('options: '))
            if user == 1:
                print(matrix.get_quarter(quarter))
            elif user == 2:
                task_options(matrix, quarter)                
            elif user == 3:
                break
        except ValueError as err:
            print(err)

def quarters_options(matrix):
    os.system('clear')
    dic = {1:'IU', 2:'IN', 3:'NU', 4:'NN'}
    while 1:
        print('''
        1.
        2.
        3.
        4.
        5. Exit''')
        try:
            user = int(input('option: '))
            if user == 5:
                break
            else:
                for k,v in dic.items():
                    if user==k:
                        quarter_options(matrix, v)
        except ValueError as err:
            print(err)
def menu(matrix):
    os.system('clear')
    matrix.add_items_from_file()
    while 1:
        print('''
        1. Show all
        2. Show quarter
        3. Add task
        4. Exit''')
        try:
            user = int(input('choose: '))
            if user == 1:
                print(matrix)
            elif user == 2:
                quarters_options(matrix)
            elif user == 3:
                title = input('title: ')
                day = int(input('day: '))
                month = int(input('month: '))
                deadline = date(2017, month, day)
                is_important = int(input('1 for important, 0 for not important: '))
                matrix.add_item(title, deadline, is_important)
            elif user == 4:
                matrix.archive_items()
                sys.exit()
        except ValueError as err:
            print(err)

# def main():
#     matrix = TodoMatrix()
#     menu(matrix)


# if __name__=="__main__":
#     main()

########################################################################
########################################################################
########################################################################

from datetime import date
import os, sys
import csv

class Person:
    def __init__(self, name):
        self.name = name 
        self.to_do = []
    def add_task(self, task):
        self.to_do.append(task)

class Task:
    def __init__(self, title, deadline, name):
        self.title = title 
        self.deadline = deadline
        self.is_done = False
        self.owner = Person(name)
        self.owner.add_task(self)
    def __str__(self):
        x = 'x'
        return "[{}] {}-{} {} task for: {}".format(x, self.deadline.day, self.deadline.month, self.title, self.owner.name)

class List:
    def __init__(self):
        self.lista = []
    def add_task(self, title, deadline, name):
        self.lista.append(Task(title, deadline, name))
    def get_task(self, index):
        return self.lista[index]
    def remove(self, index):
        del self.lista[index]
    def __str__(self):
        out = ''
        for n, task in enumerate(self.lista):
            out += "\n{}. {}\n".format(n, task)
        return out
class Matrix:
    a,b = 'alpha', 'beta'
    def __init__(self):
        self.all = {self.a:List(), self.b:List()}
    def add_list(self, title, deadline, name):
        diff = (deadline - date.today()).days
        if diff <= 3:
            self.all[self.a].add_task(title, deadline, name)
        else:
            self.all[self.b].add_task(title, deadline, name)
    def from_file(self, file='todo_items_read_test.csv'):
        if not os.path.isfile(file):
            raise FileNotFoundError
        else:
            with open(file, 'r') as f:
                reader = csv.reader(f, delimiter="|")
                for row in reader:
                    title = row[0]
                    day = int(row[1].split('-')[0]) 
                    month = int(row[1].split('-')[1])
                    deadline = date(2017, month, day)
                    name = str(row[2]) + ' ziemo'
                    self.add_list(title, deadline, name)
    def __str__(self):
        out = ''
        for k, v in self.all.items():
            out += "{}:\n {}\n".format(k, v)
        return out

def list_options(matrix, list):
    while 1:
        print(matrix.all[list])
        print('''
        1. Show name for task
        2. back''')
        try:
            user = int(input('type: '))
            if user == 1:
                for task in matrix.all[list].lista:
                    print(task.owner.name)
            elif user == 2:
                break
        except ValueError as err:
            print(err)
def show_lists(matrix):
    while 1:
        print(' 1: ',matrix.a,'\n','2: ',matrix.b,'\n 3: exit')
        try:
            user = int(input('type:'))
            if user == 1:
                list_options(matrix, matrix.a)
            elif user == 2:
                list_options(matrix, matrix.b)
            elif user == 3:
                break
        except ValueError as err:
            print(err)
def menu(matrix):
    os.system('clear')
    matrix.from_file()
    list_options = ['Menu:', '1. show all', '2. add task', '3. show specific list', '4. show tasks for name','5. exit']
    while 1:
        for option in list_options:
            print(option)
        try:
            user = int(input('type: '))
            if user == 1:
                print(matrix)
            elif user == 2:
                title = input('title:')
                day = int(input('day: '))
                month = int(input('month: '))
                deadline = date(2017, month, day)
                name = input('person: ')
                matrix.add_list(title, deadline, name)
            elif user == 3:
                show_lists(matrix)
            elif user == 4:
                user_name = input('name: ')
                for k, v in matrix.all.items():
                    for task in v.lista:
                        if task.owner.name == user_name:
                            print(task)
            elif user == 5:
                sys.exit()
        except ValueError as err:
            print(err) 
def main():
    matrix = Matrix()
    menu(matrix)

if __name__ == '__main__':
    main()