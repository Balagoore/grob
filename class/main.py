  class Person:
   count = 3

   def __init__(self, name):
     print('INIT!!')
     self.name = name
   def __str__(self):
     return f'Person<name={self.name}>' \
            f''
   def greet(self):
       print(f'Hi {self.name}!')
   def __eq__(self, other):
       return self.name == other.name

me = Person('Nick')
clone = Person('Nick')
you = Person('Vasja')
print(me, you)
print(me == clone)
me.greet()
you.greet()


print(me.name, you.name)