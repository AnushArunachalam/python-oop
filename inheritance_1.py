# inheritance is nothing but using features from already derived class or an 
# existing class.


# example

class Employee():

    def __init__(self, first, last, salary):

        self.first = first
        self.last = last
        self.salary = salary

    def first(self):
        return self.first

    def last(self):
        return self.last
    
    def salary(self):
        return self.salary


class Developer(Employee):

    def __init__(self, programming_language):
        # super().__init__(first, last, salary)
        self.programming_language = programming_language

dev = Developer("anush", "arunachalam", 9000000, "Python")

print(dev.first)