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

    with open('{}.csv'.format(employeeId), 'w') as file:
        """ Opening a new file using the ID as the name.CSV"""

        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(employeeId,
                       employeeUsername, task.get('completed'),
                       task.get('title')))
