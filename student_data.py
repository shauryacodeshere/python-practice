student_records = {"student1": {"name": "Alice", "grades": [85, 92, 78], "attendance": 20},
    "student2": {"name": "Bob", "grades": [88, 76, 95], "attendance": 18},
    "student3": {"name": "Charlie", "grades": [90, 88, 93], "attendance": 22},}
def add_or_update_student(student_id, name, grades, attendance):
    student_records[student_id] = {"name": name, "grades": grades, "attendance": attendance}


def display_records():
    for student_id, record in student_records.items():
        print(f"ID: {student_id}, Name: {record['name']}, Grades: {record['grades']}, Attendance: {record['attendance']}")

display_records()
print("\nAdding a new student...\n")
add_or_update_student("student4", "David", [89, 92, 85], 21)
display_records()
print("\nUpdating student2...\n")
add_or_update_student("student2", "Bob", [90, 80, 88], 19)
display_records()