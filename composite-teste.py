from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartement(metaclass=ABCMeta):
  
  @abstractmethod
  def __init__(self, employees):
    """Implement in child class"""
  
  @abstractstaticmethod
  def print_department():
    """Implement in child class"""
    
class Accounting(IDepartement):
  def __init__(self, employees):
    self.employees = employees
    
  def print_department(self):
    print(f"Accounting departament: {self.employees}")
    

class Development(IDepartement):
  def __init__(self, employees):
    self.employees = employees
    
  def print_department(self):
    print(f"Development departament: {self.employees}")
    
class ParentDepartament(IDepartement):
  def __init__(self, employees):
    self.employees = employees
    self.base_employees = employees
    self.sub_depst = []
    
  def add(self, dept):
    self.sub_depst.append(dept)
    self.employees += dept.employees
    
  def print_department(self):
    print(f"Parent departement")
    print(f"Parent departement Base employees: {self.base_employees}")
    for dept in self.sub_depst:
      dept.print_department()
    print(f"Total number of employees: {self.employees}")
    
dept1 = Accounting(200)
dept2 = Development(170)
parent_dept = ParentDepartament(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

dept1.print_department()
dept2.print_department()
parent_dept.print_department()