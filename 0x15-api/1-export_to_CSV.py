#!/usr/bin/python3
"""Export to csv."""


import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos?userId={}"
                         .format(sys.argv[1])).json()

    csv_filename = '{}.csv'.format(user['id'])

    with open(csv_filename, "w") as csv_file:

        for todo in todos:
            user_id = str(user.get('id'))
            username = str(user.get('username'))
            completed = str(todo.get('completed'))
            task = str(todo.get('title'))
            record = [user_id, username, completed, task]
            csv.writer(csv_file, quoting=csv.QUOTE_ALL).writerow(record)
