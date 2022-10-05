import os
import time


def task_os_clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def task_close_application():
    print("Thank you for using the program...")
    time.sleep(5)
    sys.exit()
