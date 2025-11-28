class car_park:
    def __init__(self,location,capacity,plates=None, displays=None):
        self.location= location
        self.displays = displays or []
        self.capacity=capacity
        self.plates=plates

    def print_carpark(self):
       location=self.location
       capacity=str(self.capacity)
       return print(f" Car park at {location}, with {capacity} bays left")
    


