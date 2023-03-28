from TrainController import TrainController

class Train:
    trainCounter = 0

    def __init__(self, auth, speed, ID, line, power, actSpeed):
        super().__init__()
        
        self.trainController = TrainController()
        # id
        self.ID = ID

        # authority and speeds
        self.authority = auth
        self.currentSpeed = 0
        self.suggSpeed = speed
        self.commandedSpeed = 0
        self.commandedPower = power
        self.actSpeed = actSpeed



        # location attributes
        self.line = line
        self.location = 63
