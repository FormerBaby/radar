#!/usr/bin/python

from classes import *


def display(numStates, pos_diff, vel_diff, accel_diff):
    
    pos_sum = 0
    vel_sum = 0
    accel_sum = 0
    
    print('')

    for j in range(numStates):
        pos_sum += pos_diff[j] 
        vel_sum += vel_diff[j] 
        accel_sum += accel_diff[j] 

    pos_mse = float(pos_sum / numStates)
    vel_mse = float(vel_sum / numStates)
    accel_mse = float(accel_sum / numStates)
    
    print('--------------------------------')
    print('')
    
    print('Your {0} MSE was {1}'.format(unicode('POSITION'), unicode(pos_mse)))
    print('Your {0} MSE was {1}'.format(unicode('VELOCITY'), unicode(vel_mse)))
    print('Your {0} MSE was {1}'.format(unicode('ACCELERATION'), unicode(accel_mse)))


def mse(count, states, numStates):

    count = 0
    print('')

    for name in names:
        
        if (count < numStates):
            print('%s' % states[name].measure.pos)
            print('%s' % states[name].measure.vel)
            print('%s' % states[name].measure.accel)
            count += 1

    pos_diff = []
    vel_diff = []
    accel_diff = []
    count = 0

    for name in names:

        if (count < numStates):

            print('')
            print('----------%s----------' % states[name].name)
            print('')

            for value in State.vals:

                if (value == 'POSITION'):
                    expect_pos = float(input('What was the expected position? '))
                    actual_pos = states[name].measure.pos
                    print('actual value of states[{0}]: {1}'.format(unicode(name), unicode(actual_pos)))
                    pos_diff.append((expect_pos - actual_pos)**2)
                    print('%s' % pos_diff)

                elif (value == 'VELOCITY'):
                    expect_vel = float(input('What was the expected velocity? '))
                    actual_vel = states[name].measure.vel 
                    print('actual value: %f' % actual_vel)
                    
                    vel_diff.append((expect_vel - actual_vel)**2)
                    print('%s' % vel_diff)

                else:
                    expect_accel = float(input('What was the expected acceleration? '))
                    actual_accel = states[name].measure.accel
                    print('actual value: %f' % actual_accel)
                    accel_diff.append((expect_accel - actual_accel)**2)
                    
                    print('%s' % accel_diff)
            
            count += 1
   
    display(numStates, pos_diff, vel_diff, accel_diff)


def populate():
 
    count = 0
    states = {}
    meases = {}

    for name in names:
        states[name] = State(name)
        meases[name] = Meas(name)

    numStates = int(input('How many states did you observe? '))
    
    if (numStates > len(names)):
        print('Please enter a value less than or equal to %s' % numStates)
        return

    for name in names:
        if (count == numStates):
            mse(count, states, numStates)
            return
        
        elif (count < numStates):
            print('')
            print('------------- %s ---------------' % states[name].name)
            print('')
            
            states[name].measure.pos = float(input('Target Position at State %i: ' % (count + 1)))
            states[name].measure.vel = float(input('Target Velocity (m / s) at State %i: ' % (count + 1)))
            states[name].measure.accel = float(input('Target Accel (m / s**2) at State %i: ' % (count + 1)))
            
            count += 1


def Main():
    populate()


if __name__ == '__main__':
    Main()
