import csv
cars = [
    {'brand': 'audi', "model": 'a4', "HorsePower": 120,"price": 12000},
    {'brand': 'ford', 'model': 'focus', "HorsePower": 130,"price": 14000},
    {'brand': 'bmw', 'model': "m3", "HorsePower": 144, 'price': 22000},
    {'brand': 'mazda', 'model': 'rx8', "HorsePower": 90, 'price': 10000},
    {'brand': 'dacia', 'model': 'logan', "HorsePower": 75, 'price': 7000},
    {'brand': 'opel', 'model': 'astra', "HorsePower": 113, 'price': 18000},
    {'brand': 'ferrari','model': 'laferrari',"HorsePower": 210,'price': 20000},
    {'brand': 'lambo','model': 'diablo',"HorsePower": 220,'price': 23000}

]
slow_cars = list(filter(lambda cars: cars['HorsePower'] < 120, cars))
print(slow_cars)

fast_cars = list(filter(lambda cars: 180 > cars['HorsePower'] > 120 , cars))
print(fast_cars)

sport_cars = list(filter(lambda cars: cars['HorsePower'] > 180, cars))
print(sport_cars)

cheap_cars = list(filter(lambda cars: cars['price'] < 11000, cars))
print(cheap_cars)

medium_cars = list(filter(lambda cars: 10000 <= cars['price'] < 18000, cars))
print(medium_cars)


expensive_cars = list(filter(lambda cars: cars['price'] > 15000, cars))
print(expensive_cars)

with open('input.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['brand', 'model', 'HorsePower', 'price'])
    thewriter.writerow(['Audi', 'a4', 120, 12000])
    thewriter.writerow(['Ford', 'focus', 130, 14000])
    thewriter.writerow(['Bmw', 'm3', 144, 22000])
    thewriter.writerow(['Mazda', 'rx8', 90, 10000])
    thewriter.writerow(['Dacia', 'Logan', 75, 7000])
    thewriter.writerow(['Opel', 'Astra', 113, 18000])
    thewriter.writerow(['Ferrari', 'Laferrari', 210, 20000])
    thewriter.writerow(['Lambo', 'Diablo', 220, 23000])

with open('input.csv', 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for row in reader:
        brand = row[0]
        model = row[1]
        Horsepower = row[2]
        price = row[3]
        print(brand, model, Horsepower, price)

