class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def get_disp_info(self):
        print(f"Vehicle Name:{self.name} \n speed:{self.max_speed}km/hr\n mileage:{self.mileage} ")


veh_1 = Vehicle("School Volvo", 180, 12)
veh_1.get_disp_info()
