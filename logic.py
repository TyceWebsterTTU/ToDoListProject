import json
from gui import GUI

class task:
    def __init__(self, time, location, description, status):
        self.time = time #string 
        self.location = location #string
        self.description = description #string 
        self.status = status #boolean
    def set_task(self, time, location, description, status):
        self._time = time
        self._location = location
        self._description = description
        self._status = status

def create_list(newList):
    newList = []

def remove_list(givenList):
    for i in givenList:
        remove_task(givenList[i], givenList)

def addTask(taskToAdd, listArray):
    listArray.append(taskToAdd)

def remove_task(taskToRemove, listArray):
    listArray.remove(taskToRemove)

def move_task(taskToMove, currentList, newList):
    addTask(taskToMove, newList)
    remove_task(taskToMove, currentList)

filePath = "db.json"
with open(filePath) as file:
    json_db = json.load(file)

print(json_db)
# To print first reminder, use print(json_db["id1"])
