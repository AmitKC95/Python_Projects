import random

class Store:
    def __init__(self,value):
        self.value = []
    
    def insert(self,value):
        if value not in self.value:
            return self.value.append(value)
        else return False
    
    def remove(self,value):
        if value in self.value:
            return value
        else return False
    
    def ran_choice(self,value):
        if value in self.value:
            return random.choice(self.value)
        else return false