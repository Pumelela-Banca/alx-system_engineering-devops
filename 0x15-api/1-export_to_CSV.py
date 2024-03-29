#!/usr/bin/python3

"""
Returns information about employee TO-DO list and progress.
Also exports to cvv
"""

import csv
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

    with open(f"{sys.argv[1]}.csv", 'w', newline="") as file:
        titles = ["USER_ID",
                  "USERNAME", "TASK_COMPLETED_STATUS",
                  "TASK_TITLE"]
        all_vals = []
        for x in tasks_td:
            user_id = sys.argv[1]
            user_name = usr_name.get("username")
            completed = x.get("completed")
            title = x.get("title")
            stor_dict = {titles[0]: user_id,
                         titles[1]: user_name,
                         titles[2]: completed,
                         titles[3]: title}
            all_vals.append(stor_dict)
        writer = csv.DictWriter(file, fieldnames=titles, quoting=csv.QUOTE_ALL)
        writer.writerows(all_vals)
