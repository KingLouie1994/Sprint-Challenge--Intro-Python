# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# The vehicle class will be the parent class, also called the base class:

class Vehicle:
    pass

class GroundVehicle(Vehicle): # Subclass of Vehicle
    pass

class Car(GroundVehicle): # Subclass of Groundvehicle
    pass

class Motorcycle(GroundVehicle): # Subclass of Groundvehicle
    pass

class FlightVehicle(Vehicle): # Subclass of Vehicle
    pass

class Starship(FlightVehicle): # Subclass of FlightVehicle
    pass

class Airplane(FlightVehicle): # Subclass of FlightVehicle
    pass