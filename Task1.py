def to_do_list(self):
    j = 1
    for i in range(0,len(self)):
        print(f"{j}.{self[i]}")
        j += 1
print("***** WELCOME *****")
task_list = []
while True:
    print("Enter \n 1. To create a TO-DO LIST \n 2. To add a task \n 3. To view all the tasks. \n 4. To mark a task as completed.\n 5. To remove a task. \n 6. To exit the application.")
    option = input()
    if option == '1':
        print("Enter your task(s): (Enter 'exit' to finish)")
        while 'exit' not in task_list:
            task = input("* ")
            if task in task_list:
                print("Task already exists.")
            elif task != 'exit':
                task_list.append(task)
            else:
                break
        print("Your To-do List is as follows: ")
        to_do_list(task_list)
    if option == '2':
        inp1 = input("Enter the task: ")
        if inp1 in task_list:
            print("Task already exists.")
        else:    
            task_list.append(inp1)
            print("Task added successfully!")
            print("Your updated TO-DO LIST is as follows: ")
            to_do_list(task_list)
    if option == '3':
        print("Your TO-DO LIST is as follows:")
        to_do_list(task_list)
    if option == '4':
        print("Choose the task to be selected as completed: ")
        to_do_list(task_list)
        a = '(Completed)'
        inp2 = input()
        inp2 = [int(i) for i in inp2]
        for i in inp2:
            task_list[i-1] += a
        print("Task marked as completed!")
        print("Your updated TO-DO LIST is as follows: ")
        to_do_list(task_list)
    if option == '5':
        print("Choose the task to be removed: ")
        to_do_list(task_list)
        inp3 = input()
        inp3 = [int(i) for i in inp3]
        for i in inp3:
            task_list.pop(i-1)
        print("Task removed successfully!")
        print("Your updated TO-DO LIST is as follows: ")
        to_do_list(task_list)
    if option == '6':
        print("***** GOODBYE *****")
        break
    


        
        

