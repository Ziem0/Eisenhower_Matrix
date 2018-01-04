from datetime import datetime, date
from todo_item import TodoItem


class TodoQuarter:
    """
        Parameters:
        ----------
        Raises:
        ----------
    """


    def __init__(self):

        self.todo_items = []


    def sort_items(self):

        self.todo_items = sorted(self.todo_items, key=lambda task: task.deadline)


    def add_item(self, title, deadline):

        if not isinstance(deadline, date):
           raise ValueError('Deadline should be datetime object')
                       
        else:
           self.todo_items.append(TodoItem(title, deadline))

        self.sort_items()


    def remove_item(self, index):

        self.todo_items.remove(self.todo_items[index])


    def archive_items(self):

        for item in self.todo_items:
           if item.is_done:
               self.todo_items.remove(item)


    def get_item(self, index):

        if self.todo_items[index] in self.todo_items:
            return self.todo_items[index]
        
        else:
            raise IndexError("Index is out of range")


    def __str__(self):
        
        line_number = 1
        list_of_todo = ''

        for element in self.todo_items:
            list_of_todo += str(line_number) + '. ' + str(element) + '\n'
            line_number += 1
            
        return list_of_todo


