import csv  
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.student import Student

def read_student_data(file_path):
    student_list = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            student = Student(student_code=row['student_code'], name=row['name'], age=row['age'], student_class=row['student_class'], address=row['address'])
            student_list.append(student)
    return student_list

def write_student_list(file_path, student_list):
    data = [student.to_dict() for student in student_list]
    field_names = data[0].keys()

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)