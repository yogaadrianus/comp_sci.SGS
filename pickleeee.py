class CarRecord:
# declaring a class without other methods
    def __init__(self):
# constructor
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00
ThisCar = CarRecord() # instantiates a car record
ThisCar.EngineSize = 2500 # assign a value to a field
Car = [CarRecord() for i in range(100)] # make a list of 100 car records
Car[1].EngineSize = 2500 # assign value to a field of the 2nd car in list

import pickle # this library is required to create binary files
Car = [CarRecord() for i in range(100)]
CarFile = open('CarFile.DAT', 'wb') # open file for binary write
for i in range(100): # loop for each array element
    pickle.dump(Car[i], CarFile) # write a whole record to the binary file
CarFile.close() # close file
CarFile = open('CarFile.DAT', 'rb') # open file for binary read
Car = [] # start with empty list
while True: # check for end of file
    Car.append(pickle.load(CarFile)) # append record from file to end of list
CarFile.close()