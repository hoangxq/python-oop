import sys
import os
from utils import data

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.student import Student

STUDENT_FILE = 'students.csv'

def add_new_student(student):
    students = data.read_student_data(STUDENT_FILE)
    student_find = [item for item in students if item.student_code == student.student_code]
    if len(student_find) > 0:
        return "Sinh viên đã tồn tại!! Vui lòng nhập lại thông tin"
    # check valid student_code 
    # check valid class 
    students.append(student)
    data.write_student_list(STUDENT_FILE, students)
    return True

def update_student(student_edit):
    students = data.read_student_data(STUDENT_FILE)
    
    index = -1
    for idx, student in enumerate(students):
        if student.student_code == student_edit.student_code:
            index = idx
            break
    if index == -1:
        return "Sinh viên không tồn tại trong hệ thống!! Vui lòng thử lại"
    # check valid student_code 
    # check valid class
    students[index] = student_edit
    data.write_student_list(STUDENT_FILE, students)
    return True

def remove_student(student_code):
    students = data.read_student_data(STUDENT_FILE)
    
    student_find = [item for item in students if item.student_code == student_code]
    if len(student_find) == 0:
        return "Sinh viên không tồn tại trong hệ thống!! Vui lòng thử lại"
    
    students = [item for item in students if item.student_code != student_code]
    data.write_student_list(STUDENT_FILE, students)
    return True

def get_list_student():
    return data.read_student_data(STUDENT_FILE)