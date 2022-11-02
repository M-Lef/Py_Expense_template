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
        "type": "list",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": [{"name": user.strip()} for user in utils.get_users_list()],
    },
    {
        "type": "checkbox",
        "name": "user_invoked",
        "message": "New Expense - Payers: ",
        "choices": [{"name": user.strip()} for user in utils.get_users_list()],
    },

]


def new_expense(*args):
    infos = prompt(expense_questions)

    utils.write_csv(infos, 'expense')

    print("Expense Added !")
    return True
