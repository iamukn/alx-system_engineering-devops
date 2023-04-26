#!/usr/bin/python3
"""Accessing REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')
    employeeUsername = response.json().get('username')
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))

    with open(f"{employeeId}.csv", 'w') as f:
        """ Opening a new file using the ID as the name.CSV"""

        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(employeeId,
                    employeeUsername, task.get('completed'),
                    task.get('title')))
