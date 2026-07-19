# BUILD BY MUHAMMAD TAHIR

Task = []    # Empyt list

while True:     # Loop
    try:
        title1 = "== TO-DO-LIST =="            # Center method
        print(title1.center(80))

        title2 = "== Categories ==\n"
        print(title2.center(82))

        print("1 - Add Task")
        print("2 - View Task")
        print("3 - Delete Task")
        print("4 - Exit\n")

        choice1 = int(input("Enter choice(1-4): "))

        if choice1 == 1:                                  # if-else condition
            new_task = input("\nEnter your task: ")
            Task.append(new_task)                                # Append task in the empty list

            print(f"Task added = {Task}.\n")
            
        elif choice1 == 2:
            print(f"Task = {Task}.\n")               # Print all Task

        elif choice1 == 3:
            remove_task = int(input("Enter task index: "))    # Pop remove the list index
            Task.pop(remove_task)

            print(f"Task after deletion: {Task}.\n")

        elif choice1 == 4:
            print("\nThanks for using this program:)")
            break

        else:
            print("\nInvalid option") 
            break

    except Exception as e:                # Error handling
        print(f"Error occured: {e}.\n")