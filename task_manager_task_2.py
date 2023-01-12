# =====importing libraries===========
"""This is the section where you will import libraries"""
# Open the user document and prepare it for use. Use encoding to ensure compatibility with other systems.
user_file = open("user.txt", "r", encoding="utf-8-sig")
user_text = user_file.read()

# Create an empty dictionary to store the user data in.
user_dict = {

}

# Create a list from by splitting the text document on each new line of data.
list_of_users = user_text.split("\n")

user_count = len(list_of_users)

# use a for loop to split the username and password and then store them in the
# dictionary, the username is the key and the password the value.
for part in list_of_users:
    split_part = part.split(", ")
    user_dict[split_part[0]] = split_part[1]

# Prepare the task document for use.
task_file = open("tasks.txt", "r", encoding="utf-8-sig")
task_text = task_file.read()

# Create a dictionary to hold the tasks and their descriptions.
task_dict = {
    "Task": "",
    "Assigned to": "",
    "Date assigned": "",
    "Due date": "",
    "Task complete?": "",
    "Task description": "",

}

# split the text document into a list.
list_of_tasks = task_text.split("\n")

task_count = len(list_of_tasks)


# ====Login Section====
# Ask the user for an input, use a while loop to check the input against the dictionary keys and values.
# If input is not in the dictionary, user is asked to enter again.


enter_username = input("Please enter your username: ")

while enter_username.lower() not in user_dict.keys():
    enter_username = input("Username not found, Please enter your username: ")

enter_password = input("Please enter your password: ")

while enter_password.lower() not in user_dict.values():
    enter_password = input("Password does not match username, please enter your password: ")

else:
    print("\nLogin Successful!")
    # present the menu to the user and ensure it records the response in lowercase to reduce errors.
    if enter_username == "admin":
        menu = input('''\nSelect one of the following Options below:
\nr - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - User/task statistics
e - Exit
: ''').lower()
    if enter_username != "admin":
        menu = input('''\nSelect one of the following Options below:
\na - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r' and enter_username.lower() == "admin":

        # Open the user file and set to append. Ask the user to input the new data that needs to be saved
        users_file = open("user.txt", "a")
        new_user = input("Please enter a username: ")
        new_password = input("Please enter a password: ")
        password_check = input("Please confirm your password: ")
        # Use a while loop to check the password is correct, otherwise as to input again.
        while password_check != new_password:
            password_check = input("Sorry, those passwords do not match. Please try again: ")
        # Once the password has been confirmed, add the username and password to the external file.
        else:
            users_file.write(f"\n{new_user}, {new_password}")
            print("\nNew user has been added!")
            users_file.close()

    elif menu == 'a':
        # Ask the user to enter a username to assign a task to, use a while loop to check the user is registered.
        # If not, the user is asked to input a valid username.
        assign = input("Please enter the username you would like to assign this task to: ")
        while assign.lower() not in user_dict.keys():
            assign = input("Username not found, Please enter a valid username: ")
        # request user input for the task creation. Once the data has been collected write it to the text file.
        title = input("Enter a title for this task: ")
        description = input("Enter a brief description of this task: ")
        end_date = input("Enter a completion date for this task in the following format 10 Dec 2020: ")
        date_created = input("Enter today's date in the following format 10 Dec 2020: ")
        task_file = open("tasks.txt", "a")
        task_file.write(f"\n{assign}, {title}, {description}, {date_created}, {end_date}, No")
        print(f"New task has been added for {assign}!")
        task_file.close()

    elif menu == 'va':
        # Use a for loop to cycle through the list and use index positions to arrange the lists into the correct
        # order to store in the dictionary.
        for task in list_of_tasks:
            split_tasks = task.split(", ")
            task_dict["Task"] = split_tasks[1]
            task_dict["Assigned to"] = split_tasks[0]
            task_dict["Date assigned"] = split_tasks[3]
            task_dict["Due date"] = split_tasks[4]
            task_dict["Task complete?"] = split_tasks[5]
            task_dict["Task description"] = split_tasks[2]
            # Call the values of the dictionary to complete the form and show the user all the current tasks.
            # A new form is displayed for each entry.

            print(f"""\n     
            ════════════════════════════════════════════════════════════════════════════════════════════════════       
            Task:                   {task_dict["Task"]}
            Assigned to:            {task_dict["Assigned to"]}
            Date assigned:          {task_dict["Date assigned"]}
            Due date:               {task_dict["Due date"]}
            Task complete:          {task_dict["Task complete?"]}
            Task Description:       {task_dict["Task description"]}
            ════════════════════════════════════════════════════════════════════════════════════════════════════""")

    elif menu == 'vm':
        # Check to see if the current user logged in is in the task dictionary. If the username appears, only the
        #  tasks currently assigned to that user will be displayed.
        no_tasks = True
        for task in list_of_tasks:
            if enter_username.lower() in task:
                no_tasks = False
                split_tasks = task.split(", ")
                task_dict["Task"] = split_tasks[1]
                task_dict["Assigned to"] = split_tasks[0]
                task_dict["Date assigned"] = split_tasks[3]
                task_dict["Due date"] = split_tasks[4]
                task_dict["Task complete?"] = split_tasks[5]
                task_dict["Task description"] = split_tasks[2]
                print(f"""\n          
                ════════════════════════════════════════════════════════════════════════════════════════════════════    
                Task:                   {task_dict["Task"]}
                Assigned to:            {task_dict["Assigned to"]}
                Date assigned:          {task_dict["Date assigned"]}
                Due date:               {task_dict["Due date"]}
                Task complete:          {task_dict["Task complete?"]}
                Task Description:       {task_dict["Task description"]}
                ════════════════════════════════════════════════════════════════════════════════════════════════════""")
            task_file.close()

        # If there are no tasks available for the user, display the following message.
        if no_tasks:
            print("There are currently no tasks for you.")

    elif menu == 's' and enter_username.lower() == "admin":
        print(f"""                                  
                                TASK MANAGER STATISTICS
                ══════════════════════════════════════════════════════
                Registered users:           {user_count}
                Current number of Tasks:    {task_count}
                ══════════════════════════════════════════════════════""")

    # if e is selected, print "goodbye" and exit the program.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
