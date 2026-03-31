class Developer:
    def work(self):
        return "Разработчик пишет код"

class Manager:
    def work(self):
        return "Менеджер управляет командой"

def show_work(employees):
    for employee in employees:
        print(employee.work())