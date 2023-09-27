class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self,other):
        diff = self.age - other.age
        print(abs(diff),"year differnence")

    def __str__(self):
        return "person" + str(self.name) + ":" + str(self.age)

people1 = Person( 'park', 24)
print("Person instance exec speak function")
people1.speak()
people2 = Student('kim', 20,  0.7)
print("Student instance exec speak function")
people2.speak()