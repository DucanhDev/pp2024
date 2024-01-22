class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name


class MarkSheet:
    def __init__(self):
        self.students_list = []
        self.courses_list = []
        self.marks = {}

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_info(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        return Student(student_id, name, dob)

    def input_students(self):
        num_students = self.input_number_of_students()
        for i in range(num_students):
            student = self.input_student_info()
            self.students_list.append(student)
            print()

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_info(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        return Course(course_id, name)

    def input_courses(self):
        num_courses = self.input_number_of_courses()
        for i in range(num_courses):
            course = self.input_course_info()
            self.courses_list.append(course)
            print()

    def input_marks(self):
        course_id = input("Enter the course ID for which you want to input marks: ")
        for student in self.students_list:
            student_id = student.id
            self.marks[student_id] = self.marks.get(student_id, {})
            self.marks[student_id][course_id] = float(input(f"Enter marks for {student.name} in course {course_id}: "))

    def list_students(self):
        print("\nList of Students:")
        for student in self.students_list:
            print(f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}")

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses_list:
            print(f"ID: {course.id}, Name: {course.name}")

    def show_student_marks(self):
        course_id = input("Enter the course ID to show student marks: ")
        print(f"\nStudent Marks for Course {course_id}:")
        for student in self.students_list:
            student_id = student.id
            if course_id in self.marks.get(student_id, {}):
                print(f"{student.name}: {self.marks[student_id][course_id]}")


# Main program
mark_sheet = MarkSheet()
mark_sheet.input_students()
mark_sheet.input_courses()
mark_sheet.input_marks()

mark_sheet.list_students()
mark_sheet.list_courses()
mark_sheet.show_student_marks()
