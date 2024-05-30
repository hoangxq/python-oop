class Student:
    def __init__(self, student_code, name, age, student_class, address):
      self.student_code = student_code
      self.name = name
      self.age = age
      self.student_class = student_class
      self.address = address
    
    def to_dict(self):
        return {
            'student_code': self.student_code,
            'name': self.name,
            'age': self.age,
            'student_class': self.student_class,
            'address': self.address
            }
    
    def __str__(self):
        return f"student: student_code({self.student_code}), name({self.name}), age({self.age}), student_class({self.student_class}), address({self.address})"