from ctypes import util
import utils

def show_status():
    expenses = utils.get_expenses()

    user_list = dict()

    for expense in expenses:
        item = expense.split(',')
        amount = int(item[0])
        divide = amount / (len(item) - 3)
        x = 3
        while x != len(item):
            user_list[item[x]] += divide
    
    print(user_list)