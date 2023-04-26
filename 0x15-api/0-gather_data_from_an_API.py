#!/usr/bin/python3
"""Using the GET method to retrieve infomation"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseurl = "https://jsonplaceholder.typicode.com/users"

    url = baseurl + "/" + employee_Id
    res = requests.get(url)
    employeeName = res.json().get('name')

    todos = url + "/todos"
    response = requests.get(todos)
    task = response.json()
    done = 0
    done_task = []

    for datas in task:
        if datas.get('completed'):
            done_task.append(datas)
            done += 1

    print("Employee {0} is done with tasks ({1}/{2})"
          .format(employeeName, done, len(task)))

    for task_title in task:
        print("\t {0}".format(task_title.get('title')))
