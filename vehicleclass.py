class Vehicle:
    def __init__(self, mileage, maxspeed):
        self.mileage = mileage
        self.maxspeed = maxspeed
    
ob = Vehicle(20, 240)
print("Mileage", ob.mileage)
print("Maximum speed", ob.maxspeed)