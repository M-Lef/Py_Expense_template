from PyInquirer import prompt
import utils

user_questions = [
    {
        "type": "input",
        "name": "given name",
        "message": "New User - Given Name: ",
    },
    {
        "type": "input",
        "name": "family_name",
        "message": "New User - Family Name: ",
    },
    {
        "type": "input",
        "name": "email",
        "message": "New User - email: "
    }
]


def add_user():
    infos = prompt(user_questions)

    utils.write_csv(infos, 'user')

    print("User Added !")
    return True
