class ParkingLot:

    def __init__(self):
        self.levels = []

    def add_level(self, level):
        self.levels.append(level)

    def park_vehicle(self, vehicle):
        for level in self.levels:
            slot_number = level.park_vehicle(vehicle)
            if slot_number != -1:
                return slot_number, level.floor
        return -1

    def unpark_vehicle(self, slot_number, vehicle):
        for level in self.levels:
            if level.unpark_vehicle(slot_number=slot_number, vehicle=vehicle):
                return True
        return False

    def display_availability(self) -> None:
        for level in self.levels:
            level.display_availability()
