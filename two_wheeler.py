from vehicle import Vehicle
from vehicle_type import VehicleType


class TwoWheeler(Vehicle):
    def __init__(self, vehicle_number):
        super().__init__(vehicle_number=vehicle_number, vehicle_type=VehicleType.TWO_WHEELER)
