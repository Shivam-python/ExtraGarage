from parking_slots import ParkingSlot


class Level:
    def __init__(self, floor: int, num_spots: int):
        self.floor = floor
        self.parking_spots = [ParkingSlot(i) for i in range(num_spots)]

    def park_vehicle(self, vehicle):
        for spot in self.parking_spots:
            if spot.is_available() and spot.vehicle_type == vehicle.vehicle_type:
                spot.park_vehicle(vehicle)
                return spot.slot_number
        return -1

    def unpark_vehicle(self, slot_number, vehicle):
        for spot in self.parking_spots:
            if spot.slot_number == slot_number and spot.parked_vehicle == vehicle:
                spot.unpark_vehicle()
                return True
        return False

    def display_availability(self):
        for spot in self.parking_spots:
            print("slot : {}, status : {}".format(spot.slot_number, "Available" if spot.is_available() else "Occupied"))
