# This is the e-register application for a school. It allows you to create students, teachers, supervisors.
# It has the following features: create, edit, view.
# It saves the data in the json file. It reads the data from the json file.
# It's operated by the terminal and takes the input from the user.

import json
class School:
    def __init__(self):
        self.groups = {}
    
    def createEmptyGroup(self, name):
        empty_group = {
            "name": name, 
            "students": [], 
            "supervisor": None,
            "teachers": []
        }
        self.groups[name] = empty_group
    
    def to_dict(self):
        return {"groups": self.groups}

    def from_dict(self, data):
        self.groups = data["groups"]
class Student:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group
        self.teachers = []

    def create(self):
        self.name = input("Please enter student's first name: \n")
        self.surname = input("Please enter student's last name: \n")
        self.group = input("Please enter student's group: \n")

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "group": self.group,
            "teachers": self.teachers
        }
    def from_dict(self, data):
        self.name = data["name"]
        self.surname = data["surname"]
        self.group = data["group"]
        self.teachers = data["teachers"]

class Teacher:
    def __init__(self, name, surname, subject, groups):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.groups = groups

    def create(self):
        self.name = input("Please enter teacher's first name: \n")
        self.surname = input("Please enter teacher's last name: \n")
        self.subject = input("Please enter teacher's subject: \n")
        self.groups = []
        while True:
            group = input("Please enter teacher's groups. Press enter to finish: \n")
            if group == "":
                break
            self.groups.append(group)
    
    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "subject": self.subject,
            "groups": self.groups
        }
    
    def from_dict(self, data):
        self.name = data["name"]
        self.surname = data["surname"]
        self.subject = data["subject"]
        self.groups = data["groups"]

class Supervisor:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group

    def create(self):
        self.name = input("Please enter supervisor's first name: \n")
        self.surname = input("Please enter supervisor's last name: \n")
        self.group = input("Please enter supervisor's group: \n")

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "group": self.group
        }

    def from_dict(self, data):
        self.name = data["name"]
        self.surname = data["surname"]
        self.group = data["group"]


main_menu = ("Create [c]", "Display [d]", "Quit [q]")
def printSubMenu(option):
    create_menu = ("Student [s]", "Teacher [t]", "Supervisor [v]", "Back [b]")
    display_menu = ("Group [g]", "Student [s]", "Teacher [t]", "Supervisor [v]", "Back [b]")
    edit_menu = ("Student [s]", "Teacher [t]", "Supervisor [v]", "Back [b]")

    if option == "c":
        print(*create_menu, sep="\n")
    elif option == "d":
        print(*display_menu, sep="\n")
    elif option == "e":
        print(*edit_menu, sep="\n")

# Load school data from JSON file (if it exists)
try:
    with open("school.json", "r") as database_file:
        school_data = json.load(database_file)
        school = School()
        school.from_dict(school_data)
except FileNotFoundError:
    school = School()

while True:
    print(*main_menu, sep="\n")
    option = input("Please enter your choice: \n").lower()

    if option == "q":
        with open ("school.json", "w") as database_file:
            json.dump(school.to_dict(), database_file)
            quit("Thanks, see you later.")

    elif option == "c":
        printSubMenu(option)
        option = input("Please choose what you want to create: \n").lower()
        if option == "b":
            continue

        elif option == "s":
            print("You're in the student creation mode.\n")
            student = Student("", "", "")
            student.create()

            student_group = student.group
            if student_group not in school.groups:
                school.createEmptyGroup(student_group)
            school.groups[student_group]["students"].append(student.to_dict())

            print(f"{student.name} {student.surname} has been added to {student.group}.\n")

        elif option == "t":
            print("You're in the teacher creation mode.\n")
            teacher = Teacher("", "", "", [])
            teacher.create()

            for group in teacher.groups:
                if group not in school.groups:
                    school.createEmptyGroup(group)
                school.groups[group]["teachers"].append(teacher.to_dict())

            print(f"{teacher.name} {teacher.surname} has been added.\n")

        elif option == "v":
            print("You're in the supervisor creation mode.\n")
            supervisor = Supervisor("", "", "")
            supervisor.create()

            supervisor_group = supervisor.group
            if supervisor_group not in school.groups:
                school.createEmptyGroup(supervisor_group)
            school.groups[supervisor_group]["supervisor"] = supervisor.to_dict()

            print(f"{supervisor.name} {supervisor.surname} has been added as supervisor of {supervisor.group}.\n")

    elif option == "d":
        printSubMenu(option)
        option = input("Please choose what you want to display: \n").lower()

        if option == "g":
            print("You're in the group display mode.\n")
            for group_name, group in school.groups.items():
                print(f"Group: {group_name}")
                print(f"  Students: {[student['name'] + ' ' + student['surname'] for student in group['students']]}")
                if group["supervisor"]:
                    print(f"  Supervisor: {group['supervisor']['name']} {group['supervisor']['surname']}")
                print(f"  Teachers: {[teacher['name'] + ' ' + teacher['surname'] for teacher in group['teachers']]}")

        elif option == "s":
            print("You're in the student display mode.\n")
            for group in school.groups.values():
                for student in group["students"]:
                    print(f"{student['name']} {student['surname']} (Group: {student['group']})")

        elif option == "t":
            print("You're in the teacher display mode.\n")
            for group in school.groups.values():
                for teacher in group["teachers"]:
                    print(f"{teacher['name']} {teacher['surname']} (Group: {teacher['group']})")
    
        elif option == "v":
            print("You're in the supervisor display mode.\n")
            for group in school.groups.values():
                if group["supervisor"]:
                    print(f"{group['supervisor']['name']} {group['supervisor']['surname']} (Group: {group['supervisor']['group']})")
            
        elif option == "b":
            continue

    elif option == "e":
        printSubMenu(option)
        option = input("Please choose what you want to edit: \n").lower()
        # TODO add edit menu
    
    else:
        print("Invalid option. Please try again.\n")
