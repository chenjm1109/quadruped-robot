import numpy as np
import math

step_trip = 0.075
offset = 0.15
step_angle = math.pi / 12
turn_para = 2



def forward_gait():
    radio = 20
    gait_data = np.zeros((radio, 8))
    rate = 2
    for t in range(gait_data.shape[0]):
        yleg = step_angle * math.sin(2 * math.pi * t / radio)
        yfoot = step_trip * (-math.sin(2 * math.pi * t / radio)) + offset
        gait_data[t, 0] = -yleg
        gait_data[t, 1] = -yleg
        gait_data[t, 2] = yleg
        gait_data[t, 3] = yleg
        gait_data[t, 4] = -yfoot +  2 * offset
        gait_data[t, 5] = yfoot
        gait_data[t, 6] = yfoot
        gait_data[t, 7] = -yfoot +  2 * offset

    return rate, gait_data

def backward_gait():
    radio = 20
    gait_data = np.zeros((radio, 8))
    rate = 2
    for t in range(gait_data.shape[0]):
        yleg = step_angle * math.sin(2 * math.pi * t / radio )
        yfoot = step_trip * (-math.sin(2 * math.pi * t / radio)) + offset
        gait_data[t, 0] = -yleg
        gait_data[t, 1] = -yleg
        gait_data[t, 2] = yleg
        gait_data[t, 3] = yleg
        gait_data[t, 4] = yfoot
        gait_data[t, 5] = -yfoot +  2 * offset
        gait_data[t, 6] = -yfoot +  2 * offset
        gait_data[t, 7] = yfoot
    return rate, gait_data

def turnleft_gait():
    radio = 20
    gait_data = np.zeros((radio, 8))
    rate = 2.5
    for t in range(gait_data.shape[0]):
        yleg = step_angle * math.sin(2 * math.pi * t / radio)
        yfoot = step_trip * (-math.sin(2 * math.pi * t / radio)) + offset
        gait_data[t, 0] = -yleg
        gait_data[t, 1] = -yleg * turn_para
        gait_data[t, 2] = yleg
        gait_data[t, 3] = yleg * turn_para
        gait_data[t, 4] = -yfoot +  2 * offset
        gait_data[t, 5] = yfoot
        gait_data[t, 6] = yfoot
        gait_data[t, 7] = -yfoot +  2 * offset
    return rate, gait_data

def turnright_gait():
    radio = 20
    gait_data = np.zeros((radio, 8))
    rate = 2.5
    for t in range(gait_data.shape[0]):
        yleg = step_angle * math.sin(2 * math.pi * t / radio )
        yfoot = step_trip * (-math.sin(2 * math.pi * t / radio)) + offset
        gait_data[t, 0] = -yleg
        gait_data[t, 1] = -yleg /turn_para
        gait_data[t, 2] = yleg 
        gait_data[t, 3] = yleg /turn_para
        gait_data[t, 4] = -yfoot +  2 * offset
        gait_data[t, 5] = yfoot
        gait_data[t, 6] = yfoot
        gait_data[t, 7] = -yfoot +  2 * offset
    return rate, gait_data

def jump_gait():
    radio = 20
    gait_data = np.zeros((radio, 8))
    rate = 2
    for t in range(gait_data.shape[0]):
        yleg = 2.5 * step_angle * math.sin(2 * math.pi * t / radio )
        yfoot = 2.5 * step_trip * (-math.sin(2 * math.pi * t / radio)) + offset
        gait_data[t, 0] = -yleg
        gait_data[t, 1] = yleg
        gait_data[t, 2] = yleg
        gait_data[t, 3] = -yleg
        gait_data[t, 4] = -yfoot +  2 * offset
        gait_data[t, 5] = -yfoot +  2 * offset
        gait_data[t, 6] = yfoot
        gait_data[t, 7] = yfoot
    return rate, gait_data

def keep_gait():
    radio = 20
    gait_data = np.zeros((radio, 8))
    rate = 0.75
    for t in range(gait_data.shape[0]):
        gait_data[t, 0] = 0
        gait_data[t, 1] = 0
        gait_data[t, 2] = 0
        gait_data[t, 3] = 0
        gait_data[t, 4] = offset * t / radio
        gait_data[t, 5] = offset * t / radio
        gait_data[t, 6] = offset * t / radio
        gait_data[t, 7] = offset * t / radio
    return rate, gait_data