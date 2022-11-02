import csv

expense_file = "src/csv_files/expense_report.csv"
users_file = "src/csv_files/users.csv"


def write_csv(infos, type):

    data = []
    for info in infos:
        data.append(infos[info])

    filename = users_file if type == "user" else expense_file

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(infos)
        writer.writerow(data)
