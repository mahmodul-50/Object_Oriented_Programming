class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, stu):
        cls.student_list.append(stu)


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self._student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = is_enrolled

    def enroll_student(self):
        if self._is_enrolled:
            raise Exception("Student is already enrolled.")
        self._is_enrolled = True
        print("Student enrolled successfully.")

    def drop_student(self):
        if not self._is_enrolled:
            raise Exception("Student is not enrolled.")
        self._is_enrolled = False
        print("Student dropped successfully.")

    def view_student_info(self):
        status = "Enrolled" if self._is_enrolled else "Not Enrolled"
        print(f"ID: {self._student_id}")
        print(f"Name: {self._name}")
        print(f"Department: {self._department}")
        print(f"Status: {status}")
        print("-" * 30)


s1 = Student(101, "Rahim Uddin", "CSE")
s2 = Student(102, "Karim Ahmed", "EEE")

StudentDatabase.add_student(s1)
StudentDatabase.add_student(s2)

while True:
    print("\n1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            if not StudentDatabase.student_list:
                print("No students available.")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()

        elif choice == "2":
            sid = int(input("Enter student ID: "))
            for student in StudentDatabase.student_list:
                if student._student_id == sid:
                    student.enroll_student()
                    break
            else:
                raise ValueError("Invalid student ID.")

        elif choice == "3":
            sid = int(input("Enter student ID: "))
            for student in StudentDatabase.student_list:
                if student._student_id == sid:
                    student.drop_student()
                    break
            else:
                raise ValueError("Invalid student ID.")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1-4.")

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Error:", e)
