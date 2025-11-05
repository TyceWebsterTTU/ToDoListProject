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


taskArray = []



def create_list(taskToAdd, taskArray):
    taskArray.append(taskToAdd)
    
    
def remove_list(taskToRemove, taskArray):
    taskArray.remove(taskToRemove)
  

    
def remove_task():
    
def move_task():
    
def save()
    

file = "db.json"

with open(file) as file:
    json_db = json.load(file)

print(json_db)
# To print first reminder, use print(json_db["id1"])