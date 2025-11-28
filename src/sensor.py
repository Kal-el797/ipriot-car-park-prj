class sensor:
    def __init__(self,id,is_active,car_park):
        self.id=id
        self.is_active=is_active
        self.car_park=car_park

class entery_sensor(sensor):
    pass

class exit_sensor(sensor):
    pass