class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            print(f"Deleted task: {removed}")
        except IndexError:
            print("Please enter a valid task number.")

    def show_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")
        if not self.tasks:
            print("The list is empty.")

    def run(self):
        while True:
            print("\nOptions:")
            print("1: Add a task")
            print("2: Delete a task")
            print("3: Show all tasks")
            print("4: Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                task = input("Enter the task you want to add: ")
                self.add_task(task)
            elif choice == '2':
                self.show_tasks()
                task_index = int(input("Enter the task number you want to delete: "))
                self.delete_task(task_index)
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                print("Exiting the to-do list...")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.")

# Run
todo_list = TodoList()
todo_list.run()
