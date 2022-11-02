from PyInquirer import prompt
import utils

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name: ",
    }
]


def add_user():
    infos = prompt(user_questions)

    utils.write_csv(infos, 'user')

    print("User Added !")
    return True
