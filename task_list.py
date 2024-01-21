from collections import UserList
import task.py

class Task():
    def __init__(self, name):
        self.name = name
    def task_info_short(self):
        print(self.name)

class TaskList(UserList):
    def add(self, Task):
        self.data.append(Task)
    
    def remove(self, Task):
        self.data.remove(Task)
    
    def show(self):
        for task in self.data:
            task.task_info_short()