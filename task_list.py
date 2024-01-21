from collections import UserList
import task

class TaskList(UserList):
    def add(self, Task):
        self.data.append(Task)
    
    def remove(self, task_id):
        for task in self.data:
            if task.get_id() == task_id:
                self.data.remove(task)
    
    def show(self, status=None):
        for task in self.data:
            if status == None:
                task.task_info_short()
            else:
                if task.get_status() == status:
                    task.task_info_short()