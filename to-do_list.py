print("Lets get started")
first=str(input("Enter your first task:"))
list=[]
list.append(first)
print(f'1.{first}')

while True:
   
    print("---MENU---")
    print("1.Add New Task")
    print("2.Delete a Task")
    print("3.View To-Do list")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    match choice:

        case 1:
            task=str(input("Enter a task:"))
            list.append(task)
            print(f'Your task {task} is added.')

        case 2:
            if (list==[]):
                print(f'To-do list is empty.')
            else:
                for i in range(0,len(list)):
                    print(f'{i+1}.{list[i]}')
                
                num=int(input("Enter the number to remove:"))
                removed=list.pop(num-1)
                print("Removed task:",removed)
        case 3:
                
                 if (list==[]):
                    print(f'To-do list is empty.')
                 else:
                    for i in range(0,len(list)):
                        print(f'{i+1}.{list[i]}')
                

        case 4:
            print("Exiting")
            break
        case _:
            print("Invalid input")


