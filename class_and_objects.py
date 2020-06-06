
# define vehicle class
class Vehicle:
    """A vehicle class with method description"""
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth £%.2f." % \
                   (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

print(car1.description())
print(car2.description())

phonebook1 = {}

phonebook1["Paul"] = 789144992
phonebook1["Louise"] = 791883543
phonebook1["Melissa"] = 791456825
phonebook1["Kerrin"] = 791632573
print(phonebook1)

phonebook2 = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

print(phonebook2)

for name, number in phonebook1.items():
    print("Phone number for %s is %d" % (name, number))

del phonebook2["John"]
print(phonebook2)
phonebook2.pop("Jack")
print(phonebook2)

# Add "Jake" to the phonebook3 with the phone number 938273443,
# and remove Jill from the phonebook3
phonebook3 = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

# write your code here
phonebook3["Jake"] = 938273443
del phonebook3["Jill"]
# testing code
if "Jake" in phonebook3:
    print("Jake is listed in the phonebook3.")
if "Jill" not in phonebook3:
    print("Jill is not listed in the phonebook3.")






















