# This is the e-register application for a school. It allows you to create students, teachers, supervisors.
# It has the following features: create, edit, view.
# It saves the data in the json file. It reads the data from the json file.
# It's operated by the terminal and takes the input from the user.

import json


while True:
    with open ("school.json", "r") as file:
        school = {}
        school["groups_in_school"] = []
        school["students_in_school"] = []
        school["teachers_in_school"] = []
        school["superviors_in_school"] = []

        # menu options:
        main_menu = ("Create [C]", "Display [D]", "Quit [Q]")
        create_menu = ("Student [S]", "Teacher [T]", "Supervisor [SV]", "Quit [Q]")
        display_menu = ("Group [G]", "Student [S]", "Teacher [T]", "Supervisor [SV]", "Quit [Q]")

        print(*main_menu, sep="\n")
        option = input("Please choose an option: \n")

        if option == "C" or option == "c":
            print(*create_menu, sep="\n")
            option = input("Please choose what you want to create: \n")

            if option == "S" or option == "s":
                student = {}
                print("You're in the student creation mode.\n")
                name = input("Please type in student's first name: \n")
                surname = input("Please type in student's last name: \n")
                group_name = input("Please type in student's group: \n")
                student["name"] = name
                student["surname"] = surname
                student["group"] = group_name
                school["students_in_school"].append(student)
                if group_name not in school["groups_in_school"]:
                    group = {}
                    group["name"] = group_name
                    group["members"] = [student]
                    group["supervisor"] = None
                    group["teachers"] = []
                    school["groups_in_school"].append(group)            
                else:
                    school["groups_in_school"][group_name]["members"].append(student)

            elif option == "T" or option == "t":
                teacher = {}
                print("You're in the teacher creation mode.\n")
                name = input("Please type in teacher's first name: \n")
                surname = input("Please type in teacher's last name: \n")
                subject = input("Please type in teacher's subject: \n")
                group = input("Please type in teacher's groups: \n")
                teacher["name"] = name
                teacher["surname"] = surname
                teacher["subject"] = subject
                teacher["groups"] = [group] # how to handle multiple groups
                school["teachers_in_school"].append(teacher)
                if group not in school["groups_in_school"]:
                    group = {}
                    group["name"] = group
                    group["members"] = [teacher]
                    group["supervisor"] = None
                    group["teachers"] = []
                    school["groups_in_school"].append(group)
                else:
                    school["groups_in_school"][group]["teachers"].append(teacher)
                
            elif option == "SV" or option == "sv":
                supervisor = {}
                print("You're in the supervisor creation mode.\n")
                name = input("Please type in supervisor's first name: \n")
                surname = input("Please type in supervisor's last name: \n")
                group = input("Please type in supervisor's group: \n")
                supervisor["name"] = name
                supervisor["surname"] = surname
                supervisor["group"] = group
                school["supervisors_in_school"].append(supervisor)
                if group not in school["groups_in_school"]:
                    group = {}
                    group["name"] = group
                    group["supervisor"] = supervisor
                    school["groups_in_school"].append(group)

                json.dump(school, open("school.json", "a"))

        elif option == "Q" or option == "q":
                quit("Thanks, see you later.")

        elif option == "D" or option == "d":
            print(*display_menu, sep="\n")
            option = input("Please choose what you want to display: \n")
            if option == "G" or option == "g":
                print("You're in the group display mode.\n")
                print(school["groups_in_school"])
            elif option == "S" or option == "s":
                print("You're in the student display mode.\n")
                print(school["students_in_school"]["name"])
            elif option == "T" or option == "t":
                print("You're in the teacher display mode.\n")
            elif option == "SV" or option == "sv":
                print("You're in the supervisor display mode.\n")
            elif option == "Q" or option == "q":
                quit("Thanks, see you later.")
        elif option == "Q" or option == "q":
            quit("Thanks, see you later.")

        else:
            print("Invalid option. Please try again.\n")
