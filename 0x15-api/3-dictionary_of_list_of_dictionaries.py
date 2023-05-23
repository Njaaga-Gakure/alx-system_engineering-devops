#!/usr/bin/python3
"""Export all users to json."""


import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    json_filename = 'todo_all_employees.json'

    all_employees_dict = {}
    for user in users:
        all_employees_dict[user.get('id')] = []
        for todo in todos:
            if (todo.get('userId') == user.get('id')):
                temp_dict = {
                    'username': user.get('username'),
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                }
                all_employees_dict[user.get('id')].append(temp_dict)
    with open(json_filename, 'w') as json_file:
        json.dump(all_employees_dict, json_file)
