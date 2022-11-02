import csv

# Je pense que j'aurais préféré utiliser json mais trop tard hehe

expense_file = "src/csv_files/expense_report.csv"
users_file = "src/csv_files/users.csv"


def write_csv(infos, type):

    data = []
    for info in infos:
        if info == "user_invoked":
            for user in infos[info]:
                data.append(user)
        else:
            data.append(infos[info])

    filename = users_file if type == "user" else expense_file

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


def get_users_list():

    with open(users_file, 'r') as f:
        content = f.readlines()
        return content
