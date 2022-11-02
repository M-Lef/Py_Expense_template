from ctypes import util
from PyInquirer import prompt
import utils

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
    },

]


def new_expense(*args):
    infos = prompt(expense_questions)

    utils.write_csv(infos, 'expense')

    print("Expense Added !")
    return True
