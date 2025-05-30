import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial
import time

dataList = []
fig = plt.figure()
ax = fig.add_subplot(111)

COMPort = 'COM4'
Baudrate = 9600
ser = serial.Serial(COMPort, Baudrate)

def animateData(i, dataList, ser):
    ser.write(b'g')
    arduinoData_string = ser.readline().decode('ascii')
    print(arduinoData_string)

    try:
        arduinoData_float = float(arduinoData_string)
        dataList.append(arduinoData_float)

    except:
        pass

    dataList = dataList[-50:]

    ax.clear()
    ax.plot(dataList, label = 'Data ADC', color='blue')

    ax.legend(loc= 'upper right')

    ax.set_ylim([0, 4200])
    ax.set_title("Analog Data")
    ax.set_ylabel("Value")

myAnimation = animation.FuncAnimation(fig, animateData, frames=100, fargs=(dataList, ser), interval=100)

plt.show()
ser.close()