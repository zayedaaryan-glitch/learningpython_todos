import todos_functions

while True:
    user_action = input("what do you want to do?:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        job = user_action[4:]

        pending_jobs = todos_functions.get_jobs()

        pending_jobs.append(job.title() + "\n")

        todos_functions.write_jobs(pending_jobs)

    elif user_action.startswith("see tasks" or "show tasks"):

        pending_jobs = todos_functions.get_jobs()

        print("current pending jobs: ")

        for index, task in enumerate(pending_jobs):
            task = task.strip('\n')
            print(f'{index + 1}.{task}')

    elif user_action.startswith("quit"):
        break

    elif user_action.startswith("edit") :
        try:
            replace = int(user_action[5:])
            replace = replace - 1

            pending_jobs = todos_functions.get_jobs()

            new_job = input("enter a new task: ")
            new_job = new_job.title()
            pending_jobs[replace] = new_job + "\n"

            todos_functions.write_jobs(pending_jobs)

        except ValueError:
            print("invalid input")
            continue

    elif user_action.startswith("complete") :
        try:
            clear = int(user_action[9:])

            pending_jobs = todos_functions.get_jobs()

            pick = clear - 1
            task_to_be_removed = pending_jobs[pick].strip('\n')
            pending_jobs.pop(pick)

            print(f"The task {task_to_be_removed} was removed from the pending jobs list.")

            todos_functions.write_jobs(pending_jobs)

        except ValueError:
            print("invalid input")
    else :
        print("invalid input")

import time

for text in "shutting down" :
    print(text.upper())
    time.sleep(0.24)