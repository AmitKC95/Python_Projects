# mymodule.py file

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def generate_full_name(self):
        return self.firstname + ' ' + self.lastname

def sum_two_nums(x, y):
    return x + y

def gravity():
    return 9.8
