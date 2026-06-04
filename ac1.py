#  Introduce My Robot TOM

class RobotTom:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello! My name is", self.name)
        print("My model is", self.model)
        print("My purpose is", self.purpose)


# Creating an object
my_robot = RobotTom(" Tom", " 1.0", " to provide assitance")

# Calling the method
my_robot.introduce()

#  Introduce My Robot Jerry

class RobotJerry:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hi there! My name is", self.name)
        print("My model is", self.model)
        print("My purpose is", self.purpose)


# Creating an object
my_robot = RobotJerry("Jerry", " 2.0", " to be a backup for Tom")

# Calling the method
my_robot.introduce()



