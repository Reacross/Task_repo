import task_list

class Task:
    def __init__(self, id, title, description, status, due_date):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

    def change_status(self, status):
        self.status = status

    def task_info_short(self):
        print('{:^5} {:^10} {:^10}'.format(self.id, self.status, self.due_date))

    def task_info_full(self):
        print('{:^5} {:^15} {:^15} {:^10} {:^10}'.format(self.id, self.title, self.description, self.status, self.due_date))
    
    def get_status(self):
        return self.status
    
    def get_id(self):
        return self.id


if __name__ == '__main__':
    task_1 = Task(2496, "To-do-do", 'First-to finnish', 'In Process', '25-01-2024')
    task_2 = Task(2487, "To-do-or-not", 'First-to finish', 'To do', '25-11-2024')

    tasks = task_list.TaskList()
    tasks.add(task_1)
    tasks.add(task_1)
    asks.show('In Process')
    tasks.show('To do')