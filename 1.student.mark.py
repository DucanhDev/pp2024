students_list = []
courses_list = []
marks = {}

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    return {"id": student_id, "name": name, "dob": dob}


def input_students():
    num_students = input_number_of_students()
    for i in range(num_students):
        student = input_student_info()
        students_list.append(student)
        print()

def input_number_of_courses():
    return int(input("Enter the number of courses: "))


def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return {"id": course_id, "name": name}


def input_courses():
    num_courses = input_number_of_courses()
    for i in range(num_courses):
        course = input_course_info()
        courses_list.append(course)
        print()

def input_marks():
    course_id = input("Enter the course ID for which you want to input marks: ")
    for student in students_list:
        student_id = student["id"]
        marks[student_id] = marks.get(student_id, {})
        marks[student_id][course_id] = float(input(f"Enter marks for {student['name']} in course {course_id}: "))


def list_students():
    print("\nList of Students:")
    for student in students_list:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")


def list_courses():
    print("\nList of Courses:")
    for course in courses_list:
        print(f"ID: {course['id']}, Name: {course['name']}")


def show_student_marks():
    course_id = input("Enter the course ID to show student marks: ")
    print(f"\nStudent Marks for Course {course_id}:")
    for student in students_list:
        student_id = student["id"]
        if course_id in marks.get(student_id, {}):
            print(f"{student['name']}: {marks[student_id][course_id]}")


# Main program
input_students()
input_courses()
input_marks()

list_students()
list_courses()
show_student_marks()
