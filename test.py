from collections import UserList
import task
from datetime import date, datetime, timedelta

class TaskList(UserList):
    def add(self, Task):
        self.data.append(Task)
    
    def remove(self, Task):
        self.data.remove(Task)
    
    def show(self):
        for task in self.data:
            task.task_info_short()
    
    def reminder(self, id, due_date):
        today = datetime.today(date)
        deadline = self.due_date(date)
        if timedelta(deadline, today) < 7:
            print(f'Hurry up! Task {self.id} must be done to {self.due_date}!')

        
