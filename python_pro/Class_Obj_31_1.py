#class & object

class Bike:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand

    def details(self):
        print(f"Bike top speed is {self.speed} & brand is {self.brand}.")

    def __str__(self):
        return f"Bike top speed is {self.speed} & brand is {self.brand}."

bike1 = Bike(300, "Suzuki")
bike2 = Bike(290, "Yamaha")

bike1.details()
bike2.details()

#using String Rep. method
print(bike1)