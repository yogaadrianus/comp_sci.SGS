
import pickle

class CarRecord:
    # declaring a class without other methods
    def __init__(self):
        # constructor
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00


ThisCar = CarRecord()  # instantiates a car record
ThisCar.EngineSize = 2500  # assign a value to a field

Car = [CarRecord() for i in range(100)]  # make a list of 100 car records
Car[1].EngineSize = 2500  # assign value to a field of the 2nd car in list


# Write records to a binary file
CarFile = open('CarFile.DAT', 'wb')

for i in range(100):
    pickle.dump(Car[i], CarFile)

CarFile.close()


# Read records from the binary file
CarFile = open('CarFile.DAT', 'rb')

Car = []

for i in range(100):
    Car.append(pickle.load(CarFile))

CarFile.close()


# Display the result
print("Total records:", len(Car))
print("Engine size of the second car:", Car[1].EngineSize)
