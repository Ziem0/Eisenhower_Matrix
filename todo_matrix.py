import csv
import os
from datetime import datetime, date
from todo_item import TodoItem
from todo_quarter import TodoQuarter


class TodoMatrix:
    """
        Parameters:
        ----------
        Raises:
        ----------
    """

    def __init__(self):

        self.todo_quarters = {'IU': TodoQuarter(),
                              'IN': TodoQuarter(),
                              'NU': TodoQuarter(),
                              'NN': TodoQuarter()}


    def get_quarter(self, status):

        for item in self.todo_quarters.keys():

            if status == item:
                
                return self.todo_quarters[status]


    def add_item(self, title, deadline, is_important=False):

        if not isinstance(deadline, date):
            raise TypeError("wrong date format!")

        else:
            if is_important and (deadline - datetime.today()).days <= 3:
                self.todo_quarters['IU'].add_item(title, deadline)
            elif is_important:
                self.todo_quarters['IN'].add_item(title, deadline)
            elif is_important is False and (deadline - datetime.today()).days <= 3:
                self.todo_quarters['NU'].add_item(title, deadline)
            elif is_important is False:
                self.todo_quarters['NN'].add_item(title, deadline)


    def add_items_from_file(self, file_name = 'todo_items_read_test.csv'):

        if not os.path.isfile(file_name):
            raise FileNotFoundError

        else:
            with open(file_name, 'r') as csvfile:
                spamreader = csv.reader(csvfile, delimiter='|')

                for row in spamreader:
                    title = row[0]
                    is_important = False
                    if row[2]:
                        is_important = True

                    deadline = datetime.strptime(row[1]+"-2017", "%d-%m-%Y")
                    self.add_item(title, deadline, is_important)


    def save_items_to_file(self, file_name = 'todo_items_save_test.csv'):


        with open(file_name, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')

            for key, value in self.todo_quarters.items():
                for task in value.todo_items:
                    # print (task)
                    date = '-'.join([str(task.deadline.day), str(task.deadline.month)])

                    if key == 'IU' or key == 'IN':
                        writer.writerow([task.title, date, "important"])
                    else:
                        writer.writerow([task.title, date, ""])


    def archive_items(self):

        for key, value in self.todo_quarters.items():
           value.archive_items()


    def __str__(self):

        for key in self.todo_quarters.keys():
            print (key + ':')
            print (str(self.todo_quarters[key]))

