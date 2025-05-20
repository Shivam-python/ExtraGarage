from vehicle import Vehicle
from vehicle_type import VehicleType


class ParkingSlot:
    def __init__(self, slot_number: int):
        self.slot_number = slot_number
        self.vehicle_type = VehicleType.CAR
        self.parked_vehicle = None

    def is_available(self):
        return self.parked_vehicle is None

    def park_vehicle(self, vehicle: Vehicle):
        if self.is_available() and vehicle.get_vehicle_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
            return True

        return False

    def unpark_vehicle(self):
        self.parked_vehicle = None

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_parked_vehicle(self):
        return self.parked_vehicle

    def get_slot_number(self):
        return self.slot_number
