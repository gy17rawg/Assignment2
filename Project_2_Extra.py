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
Ice2 = []
IceSum = 0
IceBergVol = 0
Move = False
outputdata = []


def icemasscalc(thickness):
    mass = thickness * 1 * 900

    Ice2.append(mass)


def run():
    print("Run Initiated")

    global IceSum
    global IceBergVol
    global outputdata
    elementnumber = 0
    startx = 0
    starty = 0
    line = 0
    iceberg = 0
    global Ice2
    foundiceberg = False
    i = 0

    print("Running")

    # print(Lidar[197][33])

    while line <= len(Radar):  # First loop takes calls row individually

        # print(Radar(r))

        # print(Radar[r])

        data = Radar[line]

        y = line

        print(line)

        for i in range(len(data)):

            x = i

            if int(data[i]) >= 100 and foundiceberg is False:  # Second loop iterates through each element of the first list (row)

                iceberg += 1

                print("Iceberg: " + str(iceberg))

                startx = i  #Left most x position of iceberg

                foundiceberg = True # Set found iceberg to true

                # print(x, y)

                # print(Lidar[y][x])

            if foundiceberg is True:  #If there is an iceberg already found

                i = startx  #starting position is the left most element

                print("Line" + str(y))

                while int(data[i + 1]) >= 100:
                    elementnumber += 1
                    i += 1

                print(elementnumber)

                if elementnumber > 0:

                    for j in range(elementnumber):
                        # print(x, y)

                        # print(Lidar[y][x])  # Does y then x as it retrieves by the array then the element position

                        thickness = int((Lidar[y][x])) / 10  # Gets thickness in metres at that coordinate

                        # print(thickness)
                        Radar[y][x] = 0
                        
                        print(Radar[y][x])

                        icemasscalc(thickness)

                        x += 1

                    if int(Lidar[y + 1][startx]) == 0:  # Checking if the next line is 0

                        for k in range(len(Ice2)):
                            IceSum += Ice2[k]

                        Ice2 = []

                        IceBergVol = IceSum * 10

                        if IceBergVol < 36000000:
                            move = True

                        else:

                            move = False

                        # Save to file

                        header = ['Iceberg', 'Ice above Sea Level', 'Total Iceberg Mass', 'Tugability']
                        output = open('Output2.csv', 'w', newline='')
                        writer = csv.writer(output)
                        writer.writerow(header)

                        TextDisp = tkinter.StringVar()

                        label = tkinter.Label(gui, textvariable=TextDisp, background="White", foreground="Black",
                                              relief=RAISED, width=75,
                                              height=10)

                        TextDisp.set(str(iceberg) + '\n'
                                                    "Total Mass of Iceberg: " + str(
                            "{:,}".format(IceBergVol)) + "kg" + '\n' "Mass of Ice above sea level: "
                                     + str("{:,}".format(IceSum)) + "kg" + '\n' "Move = " + str(move))

                        label.pack()

                        print("Results Displayed")

                        outputdata = [iceberg, IceSum, IceBergVol, Move]

                        writer.writerow(outputdata)

                        output.close()

                        line = 0

                        startx = 0

                        foundiceberg = False

                        elementnumber = 0

                x = startx

                y += 1

        line += 1

    # SeaLevelText = tkinter.Label(IceSum)
    # "Mass of Ice above sea level: " + "{:,}".format(IceSum) + "kg")

    # SeaLevelText.pack()

    # https://www.tutorialspoint.com/python/tk_label.htm

    # Text = ("Total Mass of Iceberg: " + str("{:,}".format(IceBergVol)) + "kg" + "Mass of Ice above sea level: "
    # + str("{:,}".format(IceSum)) + "kg" + "Move = " + str(move))

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

lidar = open("Lidar2.csv")

reader = csv.reader(lidar, quoting=csv.QUOTE_NONNUMERIC)
# Can use delimiter= if delimiter isn't a comma. Non-numeric converts number to float

for row in reader:  # For each row read in

    rowlist = []  # Blank list for the reading of each row (y direction)

    for value in row:  # list of values, x direction

        rowlist.append(value)  # makes a list of the values

    Lidar.append(rowlist)  # adds the rows/values to lidar list to re-create the matrix in python

lidar.close()  # Close file

# print(Lidar[33][198])

radar = open("Radar2.csv")

reader2 = csv.reader(radar, quoting=csv.QUOTE_NONNUMERIC)
# Can use delimiter= if delimiter isn't a comma. Non-numeric converts number to float

for row in reader2:  # For each row read in

    rowlist = []  # Blank list for the reading of each row (y direction)

    for value in row:  # list of values, x direction

        rowlist.append(value)  # makes a list of the values

    Radar.append(rowlist)  # adds the rows/values to lidar list to re-create the matrix in python

radar.close()  # Close file

# Display Radar and Lidar
# https://www.geeksforgeeks.org/how-to-display-multiple-images-in-one-figure-correctly-in-matplotlib/

fig = matplotlib.pyplot.figure(figsize=(7, 7), dpi=100)

fig.canvas.set_window_title('Lidar and Radar images')
# https://www.geeksforgeeks.org/how-to-display-multiple-images-in-one-figure-correctly-in-matplotlib/

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
