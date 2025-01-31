#inheritance

class Bike:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand

    def details(self):
        print(f"Bike top speed is {self.speed} & brand is {self.brand}.")

bike1 = Bike(300, "Suzuki")
bike2 = Bike(290, "Yamaha")
bike1.details()
bike2.details()

#inherit from Bike class
class Color(Bike):
    def __init__(self, speed, brand, color):
        super().__init__(brand,speed)
        self.color = color

    def disColor(self):
        print(f"Bike speed is {self.speed}, brand is {self.brand} & color is {self.color}")

bike1 = Color(300, "Suzuki", "black")
bike2 = Color(290, "Yamaha", "white")
bike1.disColor()
bike2.disColor()

#polymorphism

#overloading (same function but different parameters)
class First:
    def disinfo(self,name=''):
            print("Hello" +name)

a = First()
a.disinfo()
a.disinfo(' World!')

#overriding = inheritance