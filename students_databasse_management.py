import json
import time


class Student:

    def __init__(self, name, roll_no, division, branch, fees_paid = 0, marks_details = {}, assignments = 16, project = {}):
        self.name = name
        self.roll_no = roll_no
        self.division = division
        self.branch = branch
        self.fees_paid = fees_paid
        self.marks_details = marks_details
        self.assignments = assignments
        self.project = project

    def update_fees(self):
        amount_paid = int(input("What is the amount paid? "))
        self.fees_paid = amount_paid

    def update_marks(self):
        print("Options: ")
        print("1.Midsem first semister")
        print("2.Midsem second semister")
        print("3.Endsem first semister")
        print("4.Endsem second semister")
        choice = input("Your choice: ")
        if choice not in ["1", "2", "3", "4"]:
            print("invalid input")
            return False
        temperory_dict = {}
        for _ in range(5):
            subject = input("Sunject Name: ")
            marks = input(f"marks obtained in {subject}: ")
            temperory_dict[f"{subject}"] = marks
        if choice == "1":
            self.marks_details["mid_sem_1"] = temperory_dict
        elif choice == "2":
            self.marks_details["mid_sem_2"] = temperory_dict
        elif choice == "3":
            self.marks_details["end_sem_1"] = temperory_dict
        elif choice == "4":
            self.marks_details["end_sem_2"] = temperory_dict

        print("Marks updated Successfully")
    
    def update_assignments(self):
        self.assignments = int(input("Assignments left: "))

    def update_project(self):
        title = int(input("Title of project: "))
        marks = int(input("Marks Obtained: "))
        self.project = {"title": title, "makrs": marks}

    
def add_student():
    name = input("Name of student: ")
    roll_no = int(input("Roll no: "))
    division = input("Division: ")
    branch = input("Branch: ")
    return Student(name=name, roll_no=roll_no, division=division, branch=branch)

def save_data(objects):
    db = []
    for object in objects:
        student = {
            "name" : object.name, 
            "roll_no" : object.roll_no, 
            "division" : object.divison, 
            "branch" : object.branch, 
            "fees" : object.fees_paid, 
            "marks" : object.marks_details, 
            "assignments" : object.assignments, 
            "project" : object.project
            }
        db.append(student)
        print(student)
    with open('student_data.json', 'w') as f:
        json.dump(db , f)

def load_previous_data():
    try:
        with open('student_data.json', "r") as read_file:
            data = json.load(read_file)
            students = []
            for student in data:
                students.append(Student
                (
                    name = student['name'], 
                    roll_no = student['roll_no'], 
                    division = student['division'], 
                    branch = student['branch'], 
                    fees_paid = student['fees'], 
                    marks_details = student['marks'], 
                    assignments = student['assignments'], 
                    project = student['project']
                )
            )
            return students

    except:
        return []

def main():
    students = load_previous_data()

    while True:
        print("Student Data Management System:")
        print("Options:")
        print("1.Add Student to system")
        print("2.View All Students")
        print("3.Search for specific student and edit his/her details")
        print("4.Save Changes and quit program")
        choice = input("Your Choice: ")

        if choice == "1":
            new_student = add_student()
            students.append(new_student)
            print("Added this student to the database")
            time.sleep(2)

        if choice == "2":
            print("This is the list of students in the system: ")
            for student in students:
                print(f"Name: {student.name}, Rollno: {student.roll_no}, Branch: {student.branch}")
            time.sleep(2)

        if choice == "3":
            name_num = input("Search Student by Name or Roll number ")
            for student in students:
                if student.name == name_num:
                    print(f"Name: {student.name}\nRollno: {student.roll_no}\nDivision: {student.division}\nBranch: {student.branch}\nFees Paid: {student.fees_paid}")
                    time.sleep(2)

                if student.roll_no == name_num:
                    print(f"Name: {student.name}\nRollno: {student.roll_no}\nDivision: {student.division}\nBranch: {student.branch}\nFees Paid: {student.fees_paid}")
                    time.sleep(2)
                break
            print("what do you want to do with this student? ")
            print("1.Update Fees")
            print("2.Update Marks")
            print("3.Update Assignments")
            print("4.Update Projects")
            print("5.Remove Student from database")
            choice = input("Your Choice: ")
            if choice == "1":
                student.update_fees()
                print("Updated successfully.")

            elif choice == "2":
                student.update_marks()
                print("Updated successfully.")

            elif choice == "3":
                student.update_assignments()
                print("Updated successfully.")

            elif choice == "4":
                student.update_project()
                print("Updated successfully.")
            
            elif choice == "5":
                students.remove(student)
                print("Student Removed from database")

            time.sleep(2)

        if choice == "4":
            save_data(students)
            print("Data saved.")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()