"""
Christopher Craig
CSD-325, Module 8

student_list_cjc.py - loads a list of students from student.json,
prints the list, appends a new student record, prints the updated
list, and writes the updated list back to the .json file.
"""
import json


def print_students(students):
    """Print each student in the list as 'Last, First : ID = xxx , Email = xxx'."""
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , Email = {student['Email']}")


def main():
    # Load the class list from the JSON file
    with open("student.json", "r") as f:
        students = json.load(f)

    print("This is the original Student list:")
    print_students(students)

    # Add a new student record (fictional ID and email)
    new_student = {
        "F_Name": "Christopher",
        "L_Name": "Craig",
        "Student_ID": 99001,
        "Email": "ccraig99@fictionalmail.com",
    }
    students.append(new_student)

    print("\nThis is the updated Student list:")
    print_students(students)

    # Write the updated list back to the JSON file
    with open("student.json", "w") as f:
        json.dump(students, f, indent=4)

    print("\nThe .json file was updated.")


if __name__ == "__main__":
    main()
