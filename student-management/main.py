from model.student import Student
from model.subject import Subject
from model.student_subject import StudentSubject
from utils import student_utils

def display_student_list(students):
    print("---------------------------------")
    print("Danh sách sinh viên: ")
    print(f"{'STT':<5} | {'Mã sv':<10} | {'Tên sv':<10} | {'Lớp':<10} | {'Tuổi':<5} | {'Địa chỉ':<10} |")
    print("-" * 40)

    for idx, student in enumerate(students, start=1):
        print(f"{idx:<5} | {student.student_code:<10} | {student.name:<10} | {student.student_class:<10} | {student.age:<5} | {student.address:<10} |")

while True:
    print("""
----------------------------------
Welcome!!!!

Các chức năng trong hệ thống:
1. Quản lý sinh viên (Thêm, sửa, xóa)
2. Quản lý môn học (Thêm, sửa, xóa)
3. Thêm môn học cho sinh viên
4. Nhập điểm cho sinh viên
0. Dừng chương trình
""")
    
    option = input("Chọn chức năng bạn muốn (0->4): ")
    
    if option == "1":
        while True:
            display_student_list(student_utils.get_list_student())
            print("""
Quản lý sv:
1. Thêm mới sinh viên
2. Sửa thông tin sinh viên
3. Xóa sinh viên
0. Dừng chương trình
""")
            option_student_util = input("Chọn chức năng bạn muốn (0->3): ")
            if option_student_util == "1":
                print("-----------------------------------------------------")
                print("Thêm mới sv - Nhập các thông tin của sinh viên mới:")
                student_code = input("Mã sv: ")
                student_name = input("Tên sv: ")
                student_class = input("Lớp sv: ")
                student_age = input("Tuổi sv: ")
                student_address = input("Địa chỉ sv: ")
                
                student = Student(student_code, student_name, student_age, student_class, student_address)
                response = student_utils.add_new_student(student)
                if response == True:
                    print("Thêm sinh viên thành công!!!!")
                else: print(response)
            elif option_student_util == "2":
                print("-----------------------------------------------------")
                print("Cập nhật sv")
                student_code = input("Mã sv cần cập nhật: ")
                
                print("Nhập thông tin sv cần cập nhật:")
                student_name = input("Tên sv: ")
                student_class = input("Lớp sv: ")
                student_age = input("Tuổi sv: ")
                student_address = input("Địa chỉ sv: ")
                
                student = Student(student_code, student_name, student_age, student_class, student_address)
                response = student_utils.update_student(student)
                if response == True:
                    print("Cập nhật sinh viên thành công!!!!")
                else: print(response)
            elif option_student_util == "3": 
                print("-----------------------------------------------------")
                print("Xóa sv")
                student_code = input("Mã sv cần xóa: ")
                
                response = student_utils.remove_student(student_code)
                if response == True:
                    print(f"Xóa sinh viên {student_code} thành công!!!!")
                else: print(response)
            elif option_student_util == "0":
                print("Good bye!!!!")
                break
    elif option == "2":
        print(1)
    elif option == "3":
        print(1)
    elif option == "4":
        print(1)
    elif option == "0":
        print("Good bye!!!!")
        break
    else: print("""
----------------------------------------
Vui lòng nhập đúng giá trị!!!""")