# define vehicle class
class Vehicle:
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

print(car1.description())
print(car2.description())
