class vehicle:

    def __init__(self,max_speed,mileage):

        self.max_speed = max_speed
        self.mileage = mileage

ModelX = vehicle(250, 20)

print("Max speed of model: ", ModelX.max_speed)
print("Mileage of model: ", ModelX.mileage)