
from datetime import date

class Family:
    """Introducing my family"""

    def __init__(self, name):
        """The first name of the family member"""
        self.name = name

    def __str__(self):
        return 'Hello, my name is {} Martin.'.format(self.name)
    
    def city(self, city):
        """City of residence"""
        print('{} is living in {}'. format(self.name, city))
    
    def age(self, year, month, day):
        """The age in years of each family member"""
        birthday = date(year, month, day)
        today = date.today()
        age = today.year - birthday.year -((today.month, today.day) < (birthday.month, birthday.day))
        print("{} is {} years old".format(self.name, age))


class Mother(Family):
    def WhoIAm(self):
        print("{} is an archaeologist.".format(self.name))


class Father(Family):
    def WhoIAm(self):
        print("{} is a doctor.".format(self.name))

class Baby(Family):
    def __str__(self):
        return "This is {} Martin, he can't speak yet".format(self.name)
        super.__str__(self)
    
    def WhoIAm(self):
        print("{} is a sweet baby.".format(self.name))
    

yana=Mother('Yana')
mario=Father('Mario')
thiago=Baby('Thiago')

print(yana)
yana.age(1991, 12, 26)
yana.WhoIAm()

print(mario)
mario.age(1974, 12, 19)
mario.WhoIAm()

print(thiago)
thiago.age(2021, 7, 19)
thiago.WhoIAm()   


martin=[Mother('Yana'), Father('Mario'), Baby('Thiago')]

for person in martin:
    Family.city(person, 'Vienna')
    


    
