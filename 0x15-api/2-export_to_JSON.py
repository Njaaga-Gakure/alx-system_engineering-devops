#!/usr/bin/python3
"""Export to json."""


import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos?userId={}"
                         .format(sys.argv[1])).json()

    json_filename = '{}.json'.format(user['id'])

    userId = user['id']
    user_dict = {userId: []}
    for todo in todos:
        temp_dict = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user.get('username')
        }
        user_dict.get(userId).append(temp_dict)
    with open(json_filename, 'w') as json_file:
        json.dump(user_dict, json_file)
