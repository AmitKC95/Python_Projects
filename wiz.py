class Wiz:
    def __init__ (self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        


class Stud(Wiz):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
        
class Prof(Wiz):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
wiz = Wiz("Albus")
stud = Stud("Harry", "Gryffindor")
prof = Prof("Severus", "Defense Against Dark Arts")