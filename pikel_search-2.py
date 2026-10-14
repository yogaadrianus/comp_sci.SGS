
import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.EngineSize = 0


# Create a car record
ThisCar = CarRecord()
ThisCar.VehicleID = "CAR001"
ThisCar.Registration = "B1234ABC"
ThisCar.EngineSize = 2500

# Write the record to a binary file
Address = 0

with open("CarFile.DAT", "wb") as CarFile:
    CarFile.seek(Address)
    pickle.dump(ThisCar, CarFile)

print("Car record saved.")


# Find a record using VehicleID
VehicleID = input("Enter Vehicle ID: ")

with open("CarFile.DAT", "rb") as CarFile:
    Address = 0
    CarFile.seek(Address)
    ThisCar = pickle.load(CarFile)

    if ThisCar.VehicleID == VehicleID:
        print("Record found!")
        print("Vehicle ID:", ThisCar.VehicleID)
        print("Registration:", ThisCar.Registration)
        print("Engine Size:", ThisCar.EngineSize)
    else:
        print("Record not found.")
