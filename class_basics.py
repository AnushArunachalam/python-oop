# class myclass():

#     def __init__(self, age, lastname): # by default, this method will be called first.

#         self.age = age
#         self.lastname = lastname        

#     def age(self):

#         return self.age

#     def lastname(self):

#         return self.lastname


# # self is also known as class instance

# my = myclass(20, "sharma") # it can be anything.

# print(my.age)
# print(my.lastname)


# online trascation

# create a class.
# create __init__ method(self, username, acc_number)
# create 2 different methods that just return username and user_account number.

class Transaction: # scroll up and see

    def __init__(self, username, acc_number):

        self.username = username
        self.acc_number = acc_number

    def username(self):

        return self.username

    def acc_number(self):

        return self.acc_number
    
    def deposit(self):
        
        self.deposit_input_amount = input("please deposit an amount :::: ")
        
        
        print(f"the deposited amount is Rs. {self.deposit_input_amount} only/-")
        
        return self.deposit_input_amount
    
    def withdraw(self):

        self.withdraw_input_amount = input("please choose an amount to withdraw :::: ")

        print(f"the amount that you have withdrawed is Rs. {self.withdraw_input_amount} only/-")

        return self.withdraw_input_amount

    def available_balance(self):

        available_balance_amount = int(self.deposit_input_amount) - int(self.withdraw_input_amount)

        print(f"the amount that you have in your account is Rs. {available_balance_amount} only/-")

details = Transaction("abishiek", 111222333999)
print(details.username)           
print(details.acc_number)
details.deposit()
details.withdraw()
details.available_balance()

