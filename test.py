import uuid


# -----------------------------------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.userid = uuid.uuid4()

    def printFunction(self):
        print("My name is: " + self.name + "and I am: " + str(self.age))

    @classmethod
    def get_user_input(self):
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
        return self(fName, yAge)


def gPrint(name, age):
    print("My name is: " + name + " and I'm this old: " + age)


alist = list()
print(str(len(alist)))
person1 = Person("Greg", 53)
alist.append(person1)
person2 = Person("Angie", 49)
alist.append(person2)
person6 = Person.get_user_input()
alist.append(person6)
gPrint(person6.name, person6.age)
print("Now the list is: " + str(len(alist)) + " long.")

for i in alist:
    print(i.name + " " + str(i.age) + " UserId = " + str(i.userid))

