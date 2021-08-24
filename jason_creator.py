import json

slow_cars = [{'brand': 'dacia', 'model': 'logan', 'HorsePower': 75, 'price': 7000},
            {'brand': 'mazda', 'model': 'rx8', 'HorsePower': 90, 'price': 10000},
            {'brand': 'opel', 'model': 'astra', 'HorsePower': 113, 'price': 18000}]

with open("slow_cars.json" , "w") as scars:
    json.dump(slow_cars,scars)

fast_cars = [{'brand': 'ford', 'model': 'focus', 'HorsePower': 130,"price": 14000},
             {'brand': 'bmw', 'model': 'm3', 'HorsePower': 144, 'price': 22000}]


with open("fast_cars.json" , "w") as fcars:
    json.dump(fast_cars,fcars)


sport_cars = [{'brand': 'ferrari','model': 'laferrari',"HorsePower": 210,'price': 20000},
              {'brand': 'lambo','model': 'diablo',"HorsePower": 220,'price': 23000}]

with open("sport_cars.json", "w") as lcars:
    json.dump(sport_cars, lcars)

cheap_cars = [{'brand': 'mazda', 'model': 'rx8', 'HorsePower': 90, 'price': 10000},
              {'brand': 'dacia', 'model': 'logan', 'HorsePower': 75, 'price': 7000}]

with open("cheap_cars.json", "w") as ccars:
    json.dump(cheap_cars, ccars)


medium_cars = [{'brand': 'audi', 'model': 'a4', 'HorsePower': 120, 'price': 12000},
               {'brand': 'ford', 'model': 'focus', 'HorsePower': 130, 'price': 14000},
               {'brand': 'mazda', 'model': 'rx8', 'HorsePower': 90, 'price': 10000}]
with open("medium_cars.json", "w") as mcars:
    json.dump(medium_cars,mcars)

expensive_cars = [{'brand': 'bmw', 'model': 'm3', 'HorsePower': 144, 'price': 22000},
                  {'brand': 'opel', 'model': 'astra', 'HorsePower': 113, 'price': 18000},
                  {'brand': 'ferrari', 'model': 'laferrari', 'HorsePower': 210, 'price': 20000},
                  {'brand': 'lambo', 'model': 'diablo', 'HorsePower': 220, 'price': 23000}]

with open("expensive_cars.json","w") as ecars:
    json.dump(expensive_cars, ecars)
