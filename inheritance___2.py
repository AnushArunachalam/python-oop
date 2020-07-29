class Student():


    # def __init__(self, first, last):

    #     self.first = first
    #     self.last = last

    # we don't need to create __init__ method, we will create only when required.

    def without_init_method(self, name): # this method is just a normal method. like normal function
    # takes name as first argument.
    # we need to store the name at some variable.
    # so,
        self.name = name # at this line we stored the name into self.name variable

        return self.name # when we call this function this return statement will return the name that
        # we pass during the execution



stu = Student() # we don't need to pass any argument because we are not using any __init__ method here.

# stu is our object

print(stu.without_init_method("anush"))

# class name Student() calls __init__ method calls first. This is very 
# so we should give only 2 arguements only at first ??? yes

