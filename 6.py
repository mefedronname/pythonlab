import random

def random_number():
    return random.randint(1, 100)

print("Случайное число:", random_number())
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привет, {self.name}!")

obj = MyClass("Андрей")
obj.greet()
class ParentClass:
    def __init__(self, attribute):
        self.attribute = attribute

    def display(self):
        print("Атрибут родителя:", self.attribute)

class ChildClass(ParentClass):
    def __init__(self, attribute, child_attribute):
        super().__init__(attribute)
        self.child_attribute = child_attribute

    def display_child(self):
        print("Атрибут ребенка:", self.child_attribute)

child = ChildClass("Атрибут родителя", "Атрибут ребенка")
child.display()
child.display_child()
