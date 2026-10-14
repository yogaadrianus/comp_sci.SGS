
import pickle
import os


class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00


DATA_FILE = "CarFile.DAT"
INDEX_FILE = "CarIndex.DAT"


def save_car(ThisCar):
    # Load the existing index
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "rb") as IndexFile:
            Index = pickle.load(IndexFile)
    else:
        Index = {}

    # Open the data file and find its end
    with open(DATA_FILE, "ab") as CarFile:
        CarFile.seek(0, 2)
        Address = CarFile.tell()

        # Write the car record and save its address
        pickle.dump(ThisCar, CarFile)
        Index[ThisCar.VehicleID] = Address

    # Save the updated index
    with open(INDEX_FILE, "wb") as IndexFile:
        pickle.dump(Index, IndexFile)


def find_car(VehicleID):
    # Check whether the index exists
    if not os.path.exists(INDEX_FILE):
        print("No car records found.")
        return

    with open(INDEX_FILE, "rb") as IndexFile:
        Index = pickle.load(IndexFile)

    # Find the address of the requested car
    if VehicleID not in Index:
        print("Vehicle ID not found.")
        return

    Address = Index[VehicleID]

    # Read the record at the stored address
    with open(DATA_FILE, "rb") as CarFile:
        CarFile.seek(Address)
        ThisCar = pickle.load(CarFile)

    print("\nCar record found!")
    print("Vehicle ID:", ThisCar.VehicleID)
    print("Registration:", ThisCar.Registration)
    print("Date of Registration:", ThisCar.DateOfRegistration)
    print("Engine Size:", ThisCar.EngineSize)
    print("Purchase Price:", ThisCar.PurchasePrice)


# Create sample car records
Car1 = CarRecord()
Car1.VehicleID = "CAR001"
Car1.Registration = "B1234ABC"
Car1.DateOfRegistration = "14/10/2026"
Car1.EngineSize = 1500
Car1.PurchasePrice = 200000000

Car2 = CarRecord()
Car2.VehicleID = "CAR002"
Car2.Registration = "B5678XYZ"
Car2.DateOfRegistration = "01/09/2026"
Car2.EngineSize = 2500
Car2.PurchasePrice = 350000000


# Save the records
save_car(Car1)
save_car(Car2)

print("Sample records saved successfully.")

# Search for a car
SearchID = input("Enter Vehicle ID to search: ")
find_car(SearchID)
