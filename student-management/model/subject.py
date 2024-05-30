class Subject:
  def __init__(self, subject_code, name, unit, description):
    self.subject_code = subject_code
    self.name = name
    self.unit = unit
    self.description = description
    
  def __str__(self):
    return f"Subject: subject_code({self.subject_code}), name({self.name}), unit({self.unit}), description({self.description})"