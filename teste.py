from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
  
  @abstractstaticmethod
  def person_method():
    """ Interface Method """
    
class Student(IPerson):
  
  def __init__(self):
    self.name = "Basic student name"
  
  def person_method(self):
    print("I am a student")

class Teacher(IPerson):
  
  def __init__(self):
    self.name = "Basic student name"
  
  def person_method(self):
    print("I am a student")
    
class PersonFactory:
  
  @staticmethod
  def build_person(person_type):
    if person_type == "Student":
      return Student()
    if person_type == "Teacher":
      return Teacher
    print("Invalid type")
    return -1
  
if __name__ == "__main__":
  choice = input("What typo of person do you want?\n")
  person = PersonFactory.build_person(choice)
  person.person_method()