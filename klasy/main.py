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
        return empty_group
    
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

    def createStudent():
        name = input("Please enter student's first name: \n")
        surname = input("Please enter student's last name: \n")
        group = input("Please enter student's group: \n")
        student = Student(name=name, surname=surname, group=group)        
        return student
    
    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "group": self.group,
            "teachers": self.teachers
        }
    def from_dict(data):
        student = Student(data["name"], data["surname"], data["group"])
        student.teachers = data["teachers"]
        return student

class Teacher:
    def __init__(self, name, surname, subject, groups):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.groups = groups

    def createTeacher():
        name = input("Please enter teacher's first name: \n")
        surname = input("Please enter teacher's last name: \n")
        subject = input("Please enter teacher's subject: \n")
        groups = []
        while True:
            group = input("Please enter teacher's groups. Press enter to finish: \n")
            if group == "":
                break
            groups.append(group)
        teacher = Teacher(name=name, surname=surname, subject=subject, groups=groups)
        return teacher
    
    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "subject": self.subject,
            "groups": self.groups
        }
    
    def from_dict(data):
        teacher = Teacher(data["name"], data["surname"], data["subject"], data["groups"])
        return teacher

class Supervisor:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group

    def createSupervisor():
        name = input("Please enter supervisor's first name: \n")
        surname = input("Please enter supervisor's last name: \n")
        group = input("Please enter supervisor's group: \n")
        supervisor = Supervisor(name=name, surname=surname, group=group)
        return supervisor

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "group": self.group
        }

    def from_dict(data):
        supervisor = Supervisor(data["name"], data["surname"], data["group"])
        return supervisor

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
            json.dump(school.groups, database_file)
            quit("Thanks, see you later.")

    elif option == "c":
        printSubMenu(option)
        option = input("Please choose what you want to create: \n")
        if option == "b":
            continue

        elif option == "s":
            print("You're in the student creation mode.\n")
            student = Student.createStudent()

            student_group = student.group
            school.createEmptyGroup(student_group)
            if student_group not in school.groups.keys():
                empty_group = school.createEmptyGroup(student_group)
                school.groups[student_group] = empty_group
                school.groups[student_group]["name"] = student_group
                school.groups[student_group]["students"].append(student)
            else:
                school.groups[student_group]["students"].append(student)

            print(f"{student.name} {student.surname} has been added to {student.group}.\n")

        elif option == "t":
            print("You're in the teacher creation mode.\n")
            teacher = Teacher.createTeacher()
            
        elif option == "v":
            print("You're in the supervisor creation mode.\n")
            supervisor = Supervisor.createSupervisor()

            supervisor_group = str(supervisor.group)
            school.createGroup(supervisor_group)
            if supervisor_group not in school.groups.keys():
                school.groups[supervisor_group]["name"] = supervisor_group
                school.groups[supervisor_group]["supervisor"] = supervisor
            else:
                school.groups[supervisor_group]["supervisor"] = supervisor

    elif option == "d":
        printSubMenu(option)
        option = input("Please choose what you want to display: \n")

        if option == "g":
            print("You're in the group display mode.\n")
            
        elif option == "s":
            print("You're in the student display mode.\n")
            
        elif option == "t":
            print("You're in the teacher display mode.\n")

        elif option == "v":
            print("You're in the supervisor display mode.\n")

        elif option == "Q" or option == "q":
            quit("Thanks, see you later.")

    elif option == "E" or option == "e":
        printSubMenu(option)
        pass #TODO

    else:
        print("Invalid option. Please try again.\n")
