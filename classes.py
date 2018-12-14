import numpy as np

x = 5

names = ['state1', 'state2', 'state3', 'state4', 'state5', 
        'state6', 'state7', 'state8', 'state9', 'state10',  
        'state11', 'state12', 'state13', 'state14', 'state15', 
        'state16', 'state17', 'state18', 'state19', 'state20']


class Meas():
        vals = ['POSITION', 'VELOCITY', 'ACCELERATION']

        def __init__(self, name):
            self.name = name
            self.pos = 0
            self.vel = 0
            self.accel = 0


class State():
        vals = ['POSITION', 'VELOCITY', 'ACCELERATION']

        def __init__(self, name):
            self.name = name
            self.measure = Meas(name)
            self.mean_vect = np.zeros(x)
            self.cov_matrix = np.zeros((x, x))

