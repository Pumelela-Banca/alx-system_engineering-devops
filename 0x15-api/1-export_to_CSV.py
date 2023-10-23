#!/usr/bin/python3

"""
Returns information about employee TO-DO list and progress.
Also exports to cvv
"""

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

    with open(f"{sys.argv[1]}.csv", 'w') as file:
        for x in tasks_td:
            line = f'"{usr_name.get("userId")}",' \
                   f'"{usr_name.get("username")}",' \
                   f'"{x.get("completed")}",' \
                   f'"{x.get("title")}"'
            file.writelines(line + "\n")
