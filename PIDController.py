#!/usr/bin/python

#title           :PIDController.py
#description     :python pid controller test
#author          :Lim Xuan Zheng
#date            :200515
#version         :0.1
#notes           :Adapted from Caner Durmusoglu's implementation at https://github.com/ivmech/ivPID
#python_version  :2.7
#dependencies    : matplotlib, numpy, scipy
#==============================================================================

import PID
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import BSpline, make_interp_spline

print("Welcome to PID Controller Test. Please input the PID values accordingly")
print("Input P value")
p = input()
print("Input I value")
i = input()
print("Input D value")
d = input()


def test_pid(P = p,  I = i, D=d, L=100):
    """Self-test PID class
    .. note::
        ...
        for i in range(1, END):
            pid.update(feedback)
            output = pid.output
            if pid.SetPoint > 0:
                feedback += (output - (1/i))
            if i>9:
                pid.SetPoint = 1
            time.sleep(0.02)
        ---
    """1
    pid = PID.PID(P, I, D)

    pid.SetPoint=0.0
    pid.setSampleTime(0.01)

    END = L
    feedback = 0

    feedback_list = []
    time_list = []
    setpoint_list = []

    for i in range(1, END):
        pid.update(feedback)
        output = pid.output
        if pid.SetPoint > 0:
            feedback += (output - (1/i))
        if i>9:
            pid.SetPoint = 1
        time.sleep(0.02)

        feedback_list.append(feedback)
        setpoint_list.append(pid.SetPoint)
        time_list.append(i)

    time_sm = np.array(time_list)
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)

    # feedback_smooth = spline(time_list, feedback_list, time_smooth)
    # Using make_interp_spline to create BSpline
    helper_x3 = make_interp_spline(time_list, feedback_list)
    feedback_smooth = helper_x3(time_smooth)

    plt.plot(time_smooth, feedback_smooth)
    plt.plot(time_list, setpoint_list)
    plt.xlim((0, L))
    plt.ylim((min(feedback_list)-0.5, max(feedback_list)+0.5))
    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.title('TEST PID')

    plt.ylim((1-0.5, 1+0.5))

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_pid(1.2, 1, 0.001, L=50)
#    test_pid(0.8, L=50)