# csv
#path = "./google_stock.csv"
#file = open(path)

#for line in file:
#    print(line)

#a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
#b = set(a)
#print(b)# {1, 2, 3, 4}
#b.add(5)
#a.pop()
#print(len(a) - len(b))# 6

#thingy = {"one": 1,"two":2}
#print(thingy["three"])
#print(thingy)

#animals = {'dogs': [20, 10, 15, 8, 32, 15], 
#    'cats': [3,4,2,8,2,4], 
#    'rabbits': [2, 3, 3], 
#    'fish': [0.3, 0.5, 0.8, 0.3, 1]}

#print(animals['dogs'])
#print(animals['dogs'][3])
#print(animals[3])
#print(animals['fish'])

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print(helium)
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
print(hydrogen_weight) 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)