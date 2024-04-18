from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
  
  @abstractstaticmethod
  def person_method():
    ""

class Person(IPerson):
  def person_method(self):
    print("I'm a person!")
    
class proxyPerson(IPerson):
  
  def __init__(self):
    self.person = Person()
  
  def person_method(self):
    print("I'm the proxy funcionality!")
    self.person.person_method()
    
p1 = Person()
p1.person_method()

p2 = proxyPerson()
p2.person_method()