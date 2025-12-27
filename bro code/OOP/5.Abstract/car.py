from vehicle import Vehicle

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

    # inherits from Vehicle
    #
    # Implements go() and stop() in its own way