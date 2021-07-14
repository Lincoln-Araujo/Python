users = {} # this gets all the new users and old users
status = "" # a variable to hold the user status input

def displayMenu(): # this function gets an input to verify if the user already is registered or not
    status = input("Are you registered user? y/n ? Press q to quit ")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()

def newUser(): # this function creates a new user
    createLogin = input("Create login name: ")

    if createLogin in users:
        print("\nLogin name already exists!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser Created\n")

def oldUser(): # This function gets the user data to log in
    login = input("Enter login name: ")
    passw = input("Enter password: ")
    
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    elif login in users and users[login] != passw:
        print("\nThe passoword is incorret! Please try again!\n")
    else:
        print("\nLogin not fault! Please try again.\n")
        displayMenu()    

while status != "q": # a loop for while the input is not equal to 'quit' the system will keep working
    displayMenu()
