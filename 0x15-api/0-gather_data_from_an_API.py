#!/usr/bin/python3
"""Fetch from API."""


import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos?userId={}"
                         .format(sys.argv[1])).json()

    name = user.get('name')
    completed = 0
    no_of_tasks = 0
    for todo in todos:
        no_of_tasks = no_of_tasks + 1
        if (todo.get('completed') is True):
            completed = completed + 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, no_of_tasks))
    for todo in todos:
        if (todo.get('completed') is True):
            print("\t {}".format(todo.get('title')))
