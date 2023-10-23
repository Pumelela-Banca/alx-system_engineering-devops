#!/usr/bin/python3

"""
returns information about employee TO-DO list and progress
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
    num_tasks = len(tasks_complete)
    print(f"Employee {usr_name.get('name')} "
          f"is done with tasks({num_tasks}/{len(tasks_td)}):")

    for to_do in tasks_td:
        if to_do.get("completed"):
            print(f"\t {to_do.get('title')}")
