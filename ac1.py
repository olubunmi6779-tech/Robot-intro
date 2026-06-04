#  Introduce My Robot MAX

class Robotmax:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello! My name is", self.name)
        print("My model is", self.model)
        print("My purpose is", self.purpose)


# Creating an object
my_robot = Robotmax(" Max", " 2.0", " to provide assitance")

# Calling the method
my_robot.introduce()