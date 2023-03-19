
class Cars:
    def __init__(self):
        self.careModel = {"hatchback": 30, "sedan": 50, "SUV": 100}

    def dennaCenaZobrazenie(self):
        print("Cost per day: ")
        print("hatchback: ", self.careModel['hatchback'])
        print("sedan: ", self.careModel['sedan'])
        print("SUV: ", self.careModel['SUV'])

    def vypocetZapozicania(self, carType, numberOfDays):
        return self.careModel[carType] * numberOfDays


car = Cars()
while True:
    print("Hit 1. if you wanna display the fare display")
    print("Hit 2. if you wanna rent a car")
    print("Hit 3. if you wanna exit")
    userChoice = (int(input()))
    if userChoice == 1:
        car.dennaCenaZobrazenie()
    elif userChoice == 2:
        print("Enter type of car you wanna borrow: ")
        carType = (input())
        print("Enter number of days: ")
        numberOfDays = (int(input()))
        fare = car.vypocetZapozicania(carType, numberOfDays)
        print("total price: ", fare)
    elif userChoice == 3:
        quit()
