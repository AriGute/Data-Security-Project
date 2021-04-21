# read from txt the user and the password.
def login(uname):
    username = uname
    for line in open("accounts.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0]:
            return login_info[2]
    print("Incorrect credentials.")
    return exit()




