import uuid

# -----------------------------------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.userid = uuid.uuid4()

    @classmethod
    def get_user_input(cls):
        fName = input("Enter your name: ")
        x = fName.isalpha()
        while not x:
            print("Value must be alpha: ")
            fName = input("Enter your name: ")
            x = fName.isalpha()
        yAge = input("Enter your Age: ")
        y = yAge.isnumeric()
        while not y:
            print("Value must be a number: ")
            yAge = input("Enter your Age: ")
            y = yAge.isnumeric()
        return cls(fName, yAge)


def gPrint(name, age, userid):
    print("My name is: " + name + " and I'm this old: " + str(age) + str(userid))


alist = list()
person1 = Person("Greg", 53)
alist.append(person1)
person2 = Person("Angie", 49)
alist.append(person2)
person6 = Person.get_user_input()
alist.append(person6)

for i in alist:
    gPrint(i.name, i.age, i.userid)

