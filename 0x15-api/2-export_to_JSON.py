#!/usr/bin/python3
"""Accessing REST API for todo lists of employees"""

import json
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
    result = {employeeId: []}

    for t in tasks:
        result[employeeId].append({
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": employeeUsername
        })

    with open(f'{employeeId}.json', 'w') as file:
        json.dump(result, file)
