from collections import UserList
import task

class TaskList(UserList):
    def add(self, Task):
        self.data.append(Task)
    
    def remove(self, Task):
        self.data.remove(Task)
    
    def show(self):
        for task in self.data:
            task.task_info_short()
