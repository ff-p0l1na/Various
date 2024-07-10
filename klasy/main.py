# This is the e-register application for a school. It allows you to create students, teachers, supervisors.
# It has the following features: create, edit, view.
# It saves the data in the json file. It reads the data from the json file.
# It's operated by the terminal and takes the input from the user.

import json
class School:
    def __init__(self):
        self.groups = {}
        self.teachers = {}
        self.students = {}
        self.supervisors = {}
    
    def addNewGroup(self, group):
        if group not in self.groups.keys():
            self.groups[group] = group
    
    def addNewStudent(self, student):
        if student not in self.students.keys():
            self.students[student.name + " " + student.surname] = student

class Student:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group
        self.teachers = []

    def createStudent():
        name = input("Please type in student's first name: \n")
        surname = input("Please type in student's last name: \n")
        group = input("Please type in student's group: \n")
        school.addNewGroup(group)

        student = Student(name=name, surname=surname, group=group)
        return student

class Teacher:
    def __init__(self, name, surname, subject, groups):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.groups = groups

    def createTeacher():
        name = input("Please type in teacher's first name: \n")
        surname = input("Please type in teacher's last name: \n")
        subject = input("Please type in teacher's subject: \n")
        groups = []
        while True:
            group = input("Please type in teacher's groups. Press enter to finish: \n")
            if group == "":
                break
            groups.append(group)
        teacher = Teacher(name=name, surname=surname, subject=subject, groups=groups)

        return teacher

class Supervisor:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group

    def createSupervisor():
        name = input("Please type in supervisor's first name: \n")
        surname = input("Please type in supervisor's last name: \n")
        group = input("Please type in supervisor's group: \n")
        supervisor = Supervisor(name=name, surname=surname, group=group)

        return supervisor

# menu options:
main_menu = ("Create [C]", "Display [D]", "Quit [Q]")
create_menu = ("Student [S]", "Teacher [T]", "Supervisor [SV]", "Back [B]")
display_menu = ("Group [G]", "Student [S]", "Teacher [T]", "Supervisor [SV]", "Quit [Q]")


# Load school data from JSON file (if it exists)
try:
    with open("school.json", "r") as database_file:
        school_data = json.load(database_file)
        school = School()
        school.__dict__.update(school_data)
except FileNotFoundError:
    school = School()

while True:
    print(*main_menu, sep="\n")
    option = input("Please choose an option: \n")

    if option == "Q" or option == "q":
        with open ("school.json", "w") as database_file:
            json.dump(school.__dict__, database_file)
            quit("Thanks, see you later.")

    elif option == "C" or option == "c":
        print(*create_menu, sep="\n")
        option = input("Please choose what you want to create: \n")

        if option == "B" or option == "b":
            continue

        elif option == "S" or option == "s":
            print("You're in the student creation mode.\n")
            student = Student.createStudent()
            school.addNewStudent(student)

        elif option == "T" or option == "t":
            print("You're in the teacher creation mode.\n")
            teacher = Teacher.createTeacher()
            
        elif option == "SV" or option == "sv":
            print("You're in the supervisor creation mode.\n")
            supervisor = Supervisor.createSupervisor()

    elif option == "D" or option == "d":
        print(*display_menu, sep="\n")
        option = input("Please choose what you want to display: \n")

        if option == "G" or option == "g":
            print("You're in the group display mode.\n")
            
        elif option == "S" or option == "s":
            print("You're in the student display mode.\n")
            
        elif option == "T" or option == "t":
            print("You're in the teacher display mode.\n")

        elif option == "SV" or option == "sv":
            print("You're in the supervisor display mode.\n")

        elif option == "Q" or option == "q":
            quit("Thanks, see you later.")

    elif option == "E" or option == "e":
        pass #TODO

    else:
        print("Invalid option. Please try again.\n")
