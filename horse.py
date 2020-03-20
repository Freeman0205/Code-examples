class Horse():
    def __init__(self, name, breed, owner):
        self.name=name
        self.breed=breed
        self.owner=owner
        

class Rider():
    def __init__(self, age, name):
        self.age=age
        self.name=name


vas=Rider(25, "Вася")
horse=Horse("Маруся","Орловская",vas)
print(  horse.name, horse.breed, horse.owner.name) 
