# This is the e-register application for a school. It allows you to create students, teachers, supervisors.
# It has the following features: create, edit, view.
# It saves the data in the json file. It reads the data from the json file.
# It's operated by the terminal and takes the input from the user.

import json

# menu options:
main_menu = ("Create [C]", "Manage [M]", "Quit [Q]")
create_menu = ("Student [S]", "Teacher [T]", "Supervisor [SV]", "Quit [Q]")
manage_menu = ("Group [G]", "Student [S]", "Teacher [T]", "Supervisor [SV]", "Quit [Q]")

def takeUserInput():    
    print(*main_menu, sep="\n")

    option = input("Please choose an option: \n")
    if option == "C" or option == "c":
        print(*create_menu, sep="\n")
        option = input("Please choose what you want to create: \n")
    elif option == "M" or option == "m":
        print(*manage_menu, sep="\n")
        option = input("Please choose what you want to manage: \n")
    elif option == "Q" or option == "q":
        quit("Thanks, see you later.")

    else:
        print("Invalid option. Please try again.\n")
        takeUserInput()

    return option

takeUserInput()

