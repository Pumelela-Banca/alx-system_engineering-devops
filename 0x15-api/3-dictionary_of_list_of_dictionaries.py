#!/usr/bin/python3

"""
Returns information about employee TO-DO list and progress.
Also exports to cvv
"""

import json
import requests
import sys


if __name__ == "__main__":

    test_url = "https://jsonplaceholder.typicode.com"
    usr_name = requests.get(
        test_url + f"/users/{sys.argv[1]}").json()
    tasks_td = requests.get(
        test_url + f"/users/{sys.argv[1]}/todos").json()
    tasks_complete = [task for task in tasks_td
                      if task.get("completed")]

    with open("todo_all_employees.json", 'w') as file:
        all_vals = []
        for x in tasks_td:
            if int(sys.argv[1]) == x.get("userID"):
                continue
            user_id = sys.argv[1]
            user_name = usr_name.get("username")
            completed = x.get("completed")
            title = x.get("title")
            stor_dict = {"task": title,
                         "completed": completed,
                         "username": user_name}
            all_vals.append(stor_dict)
        json.dump({sys.argv[1]: all_vals}, file)
