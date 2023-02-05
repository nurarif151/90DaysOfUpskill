class Todo:
    def __init__(self, task):
        self.task = task
        self.is_done = False

    def __str__(self):
        return self.task + (' (Done)' if self.is_done else ' (Not done)')

    def mark_as_done(self):
        self.is_done = True


class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(Todo(task))

    def mark_as_done(self, task):
        for todo in self.todos:
            if todo.task == task:
                todo.mark_as_done()

    def __str__(self):
        return '\n'.join(str(todo) for todo in self.todos)


if __name__ == '__main__':
    todo_list = TodoList()
    while True:
        print('[1] Add task')
        print('[2] Mark task as done')
        print('[3] Quit')
        choice = int(input('Choose an option: '))
        if choice == 1:
            task = input('Enter task: ')
            todo_list.add_task(task)
        elif choice == 2:
            task = input('Enter task: ')
            todo_list.mark_as_done(task)
        elif choice == 3:
            break
        else:
            print('Invalid option.')
        print(todo_list)
