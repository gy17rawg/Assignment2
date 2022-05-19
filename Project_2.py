#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:20:45 2022

@author: rorygrindey
"""

import matplotlib.pyplot
import tkinter
import csv
from tkinter import *
import matplotlib

matplotlib.use('TkAgg')

Lidar = []
Radar = []
Ice = []
IceSum = 0
IceBergVol = 0
Move = False
outputdata = []
count = 0

# Save to file

header = ['Iceberg', 'Ice above Sea Level', 'Total Iceberg Mass', 'Tugability']

output = open('Output.csv', 'w', newline='')

writer = csv.writer(output)

writer.writerow(header)


def icemasscalc(thickness):
    mass = thickness * 1 * 900

    Ice.append(mass)


def run():
    print("Run Initiated")

    global IceSum
    global IceBergVol
    global outputdata
    global count

    for r in range(len(Radar)):  # First loop takes calls row individually

        # print(Radar(r))

        # print(Radar[r])

        data = Radar[r]

        # print(data)

        y = r

        for i in range(len(data)):  # Second loop iterates through each element of the first list (row)

            # print(i)

            if data[i] >= 100:
                x = i

                print(x, y)

                thickness = (Lidar[y][x]) / 10  # Gets thickness in metres at that coordinate

                print(thickness)

                icemasscalc(thickness)

    for i in range(len(Ice)):
        IceSum += Ice[i]

    # SeaLevelText = tkinter.Label(IceSum)
    # "Mass of Ice above sea level: " + "{:,}".format(IceSum) + "kg")

    # SeaLevelText.pack()

    # https://www.tutorialspoint.com/python/tk_label.htm

    IceBergVol = IceSum * 10

    if IceBergVol < 36000000:
        move = True

    else:

        move = False

    # Text = ("Total Mass of Iceberg: " + str("{:,}".format(IceBergVol)) + "kg" + "Mass of Ice above sea level: "
    # + str("{:,}".format(IceSum)) + "kg" + "Move = " + str(move))

    Text = tkinter.StringVar()

    label = tkinter.Label(gui, textvariable=Text, background="White", foreground="Black", relief=RAISED, width=75,
                          height=10)

    Text.set("Total Mass of Iceberg: " + str("{:,}".format(IceBergVol)) + "kg" + '\n' "Mass of Ice above sea level: "
             + str("{:,}".format(IceSum)) + "kg" + '\n' "Move = " + str(move))

    label.pack()

    outputdata = ['1', IceSum, IceBergVol, Move]

    writer.writerow(outputdata)

    output.close()

    print("Results Displayed")

    # canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=gui)

    # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    # canvas.draw()

    # canvas.pack()


# Builds main menu window

gui = tkinter.Tk()

gui.wm_title("Model")

gui.config(background="White")

gui.geometry("500x600")

menu_bar = tkinter.Menu(gui)

print("Building Menu")

gui.config(menu=menu_bar)

model_menu = tkinter.Menu(menu_bar)

menu_bar.add_cascade(label="Model", menu=model_menu)

model_menu.add_command(label="Run Model", command=run)

# Imports radar and lidar data

lidar = open("Lidar.csv")

reader = csv.reader(lidar, quoting=csv.QUOTE_NONNUMERIC)
# Can use delimiter= if delimiter isnt a comma. Nonnumeric converts number to float

for row in reader:  # For each row read in

    rowlist = []  # Blank list for the reading of each row (y direction)

    for value in row:  # list of values, x direction

        rowlist.append(value)  # makes a list of the values

    Lidar.append(rowlist)  # adds the rows/values to lidar list to re-create the matrix in python

lidar.close()  # Close file

radar = open("Radar.csv")

reader = csv.reader(radar, quoting=csv.QUOTE_NONNUMERIC)
# Can use delimiter= if delimiter isnt a comma. Nonnumeric converts number to float

for row in reader:  # For each row read in

    rowlist = []  # Blank list for the reading of each row (y direction)

    for value in row:  # list of values, x direction

        rowlist.append(value)  # makes a list of the values

    Radar.append(rowlist)  # adds the rows/values to lidar list to re-create the matrix in python

radar.close()  # Close file

# Display Radar and Lidar https://www.geeksforgeeks.org/how-to-display-multiple-images-in-one-figure-correctly-in-matplotlib/

fig = matplotlib.pyplot.figure(figsize=(7, 7), dpi=100)

fig.canvas.set_window_title('Lidar and Radar images') # https://www.geeksforgeeks.org/how-to-display-multiple-images-in-one-figure-correctly-in-matplotlib/

rows = 2

columns = 1

fig.add_subplot(rows, columns, 1)

matplotlib.pyplot.xlim(0, len(Radar[0]))

matplotlib.pyplot.ylim(0, len(Radar))

matplotlib.pyplot.imshow(Radar)

matplotlib.pyplot.title("Radar")

fig.add_subplot(rows, columns, 2)

matplotlib.pyplot.xlim(0, len(Lidar[0]))

matplotlib.pyplot.ylim(0, len(Lidar))

matplotlib.pyplot.imshow(Lidar)

matplotlib.pyplot.title("Lidar")

matplotlib.pyplot.show()

gui.mainloop()
