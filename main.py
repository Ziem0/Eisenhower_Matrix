import csv
import os
import sys
from datetime import datetime, date
from todo_item import TodoItem
from todo_quarter import TodoQuarter
from todo_matrix import TodoMatrix


def display_quarter_menu(quarter, matrix):
    
    os.system('clear')

    while True:
        print('''
            Choose quarter:
            -1- IU
            -2- IN
            -3- NU
            -4- NN
            -5- Return to main menu
        ''')

        try:

           quarter_choose = int(input("Choose number: "))
           if quarter_choose == 1:
               quarters_menu(matrix, quarter, 'IU')
           elif quarter_choose == 2:
               quarters_menu(matrix, quarter, 'IN')
           elif quarter_choose == 3:
               quarters_menu(matrix, quarter, 'NU')
           elif quarter_choose == 4:
               quarters_menu(matrix, quarter, 'NN')
           elif quarter_choose == 5:
               break

        except ValueError:
            print("Incorrect index")


def quarters_menu(matrix, quarter, key_matrix):
    """
    Shows quarter menu and possible option
    Parameters:
    ----------
    matrix: TodoMatrix object
    quarter: TodoQuarter object
    key_matrix: variable with name of the key
    ----------
    """

    os.system('clear')
    while True:

        print(''' 
                Choose option in quarter:
                -1- Show quarter
                -2- Remove task
                -3- Get task
                -4- Back to quarter menu
        ''')

        try:
            user_quarter_choice = int(input("Choose number: "))
            if user_quarter_choice == 1:
                print(matrix.get_quarter(key_matrix))
            elif user_quarter_choice == 2:
                remove_item_from_quarter(matrix, quarter, key_matrix)
            elif user_quarter_choice == 3:
                get_task_from_quarter(matrix, quarter, key_matrix)
            elif user_quarter_choice == 4:
                break

        except ValueError:
            print("Invalid index")


def add_task_to_quarter(matrix):
    """
    Parameters
    ----------
    matrix: TodoMatrix object
    -------
    """

    title = input("Choose task: ")
    gradation = input("Type 1 for important or 0 for not important: ")

    if gradation == '1':
        matrix.add_item(title, user_date(), True)
    elif gradation == '0':
        matrix.add_item(title, user_date())
    else:
        raise ValueError


def user_date():
    """
    Formats user input to valid type
    """
    day = input("Choose the deadline(day): ")
    month = input("Choose the month: ")

    if not day.isdigit() and not month.isdigit():
        raise ValueError("Integer is valid")
    else:
        deadline = datetime.strptime('2017-' + month + '-' + day, '%Y-%m-%d')

    return deadline


def remove_item_from_quarter(matrix, quarter, key_matrix):
    """
    Parameters:
    ----------
    matrix: TodoMatrix object
    quarter: TodoQuarter object
    key_matrix: variable with name of the key
    ----------
    """
    index = int(input("Choose index of the item: "))
    if index > 0 and index <= len(matrix.todo_quarters[key_matrix].todo_items):
        matrix.todo_quarters[key_matrix].remove_item(index - 1)
    else:
        raise ValueError('Invalid input')


def get_task_from_quarter(matrix, quarter, key_matrix):
    """
    Makes possible to change mark of the given item in quarter
    Parameters:
    ----------
    matrix: TodoMatrix object
    quarter: TodoQuarter object 
    key_matrix: variable with name of the key
    ----------
    """
    while True:
        index = int(input("Choose index: "))
        if index > 0 and index <= len(matrix.todo_quarters[key_matrix].todo_items):
            print(matrix.todo_quarters[key_matrix].todo_items[index - 1])
            print('''
                       Choose an option:
                       -1- mark
                       -2- unmark
                       -3- go back
                       ''')

            option = int(input("Choose number: "))
            if option == 1:
                matrix.todo_quarters[key_matrix].todo_items[index - 1].mark()
            elif option == 2:
                matrix.todo_quarters[key_matrix].todo_items[index - 1].unmark()
            elif option == 3:
                break
        else:
            raise ValueError('Invalid input')


def menu(matrix, quarter):
    
    os.system('clear')
    matrix.add_items_from_file()
    
    while True:
        
        print('''
            Main menu
        -1- Show tasks
        -2- Choose Quarter
        -3- Add task
        -0- Exit
        ''')

        try:
            user_choice = int(input('Choose number from menu: '))
            if user_choice == 1:
                matrix.__str__()
            elif user_choice == 2:
                display_quarter_menu(quarter, matrix)
            elif user_choice == 3:
                add_task_to_quarter(matrix)
            elif user_choice == 0:
                matrix.archive_items()
                matrix.save_items_to_file()
                sys.exit()
        except ValueError:
            print ("Invalid number")


def main():
    quarter = TodoQuarter()
    matrix = TodoMatrix()
    menu(matrix, quarter)


if __name__ == "__main__":
    main()