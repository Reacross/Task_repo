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


