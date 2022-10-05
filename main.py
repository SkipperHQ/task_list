############################################
# AUTHOR NAME:							   #
# PROJECT NAME: TASK LIST/TO DO LIST	   #
# PROJECT STARTED: 06/OCT/2022			   #
############################################

###### Preparatory Settings ######

import time
from resources.functions import task_os_clear, task_close_application

# TASK ID, TASK NAME, TASK DESCRIPTION/OBJECTIVE, TIME LIMIT ON TASK
task_dict = {}


def menu():
    task_input = input("Navigation\n1. New Task\n2. View Task List\n3. Options\n4. Exit\n> ").strip().lower()
    if task_input == "1" or task_input == "new task" or task_input == "create task" or task_input == "new" or task_input == "create":
        new_task()
    elif task_input == "2" or task_input == "view list" or task_input == "view task list" or task_input == "view":
        view_task_list()
    elif task_input == "3" or task_input == "options" or task_input == "settings":
        options()
    elif task_input == "4" or task_input == "quit" or task_input == "close" or task_input == "exit":
        task_close_application()


def new_task():
    print("What task are you looking to complete?")
    task_name = input ("> ")
    if len(task_name) >= 3:
        print("Please enter the task description")
        task_desc_input = input("> ").title()
        if len(task_desc_input) > 9:
            print("Valid Task...")
            id_input = input("Please enter the desired ID of task\n> ").strip().lower()
            if id_input not in task_dict.keys():
                task_dict[id_input] = {}
                task_dict[id_input]["Task Name"] = task_name
                task_dict[id_input]["Task Description"] = task_desc_input
                print(task_dict[id_input])
                print("Nice task, want to create a new task? (Y/N)")
                user_input = input("> ").strip().lower()

                if user_input == "y":
                    task_os_clear()
                    new_task()

                elif user_input == "n":
                    menu()

                else:
                    print("Invalid input...")
                    new_task()

        else:
            print("Invalid task description length... Restarting...")
            menu()

    else:
        print("Invalid task name... Name must be longer than three characters... Restarting...")
        menu()


def view_task_list():
    print("Task List...")
    for key, task in enumerate(task_dict.keys()):
        print(key, "-", task_dict[task]["Task Name"], ":", task_dict[task]["Task Description"])

    print("Navigation:\n1. Main Menu\n2. Modify a Task\n3. Delete Task\n4. New Task\n5. Options\n6. Exit")
    user_input = input("> ").lower().strip()
    if user_input == "1" or user_input == "main menu" or user_input == "main" or user_input == "menu":
        menu()
    elif user_input == "2" or user_input == "modify a task" or user_input == "modify task" or user_input == "modify" or user_input == "edit":
        modify_task()
    elif user_input == "3" or user_input == "delete a task" or user_input == "delete task" or user_input == "delete" or user_input == "remove":
        delete_task()
    elif user_input == "4" or user_input == "new task" or user_input == "new" or user_input == "create":
        new_task()
    elif user_input == "5" or user_input == "settings" or user_input == "options":
        options()
    elif user_input == "6" or user_input == "quit" or user_input == "exit":
        task_close_application()


def modify_task():
    print("Please type in the ID of the task you'd like to modify.")
    user_input = input("> ").lower().strip()
    if user_input in enumerate(task_dict.keys()):
        print(task_dict["Task Name"], "\n", task_dict["Task Description"])
        print("Navigation:\n1. Edit task name\n2. Edit task description\n3. Complete this task\n4. Return")
        user_input = input("> ").strip().lower()
        if user_input == "1" or user_input == "task name" or user_input == "edit task name" or user_input == "name":
            pass
        elif user_input == "2" or user_input == "task description" or user_input == "edit task description" or user_input == "description":
            pass
        elif user_input == "3" or user_input == "complete" or user_input == "complete a task":
            pass
        elif user_input == "4" or user_input == "return":
            view_task_list()
        else:
            print("Invalid input... Returning...")
            task_os_clear()
            view_task_list()



def delete_task():
    pass


def options():
    pass


menu()
