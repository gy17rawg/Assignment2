#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:20:45 2022

'''This is the extra python file to run the program to calculate just multiple iceberg. It pulls files from the source
folder and writes to an export file. It creates the GUI, calculates ice presence, thickness then the volume of the
icebergs and displays on the GUI. The output file contains the iceberg number, total mass then mass above sea level.
Version 1.0. MIT Licenced''

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


def icemasscalc(thickness):  # Function to calculate iceberg mass (Same as base project)

    mass = thickness * 900

    Ice2.append(mass)


def calciceberg(startx, data):  # Function to calculate each iceberg individually then makes them 'disappear'

    global IceSum
    global Ice2
    elementnumber = 0
    completeiceberg = False
    global foundiceberg
    global y
    global x
    global iceberg
    global line

    while completeiceberg is False:  # Ensures it runs until the entire iceberg is calculated

        i = startx  # starting position is the left most element of the iceberg

        # print("Line: " + str(y))

        while int(data[i]) >= 100:  # Counts the width of the iceberg as long as the next element contains ice
            elementnumber += 1
            i += 1

        # print(elementnumber)

        if elementnumber > 0:  # Runs as long as there is an iceberg width

            x = startx

            for j in range(elementnumber):  # Loops through each element just of the iceberg
                # print(x, y)

                # print(Lidar[y][x])  # Does y then x as it retrieves by the array then the element position

                thickness = int((Lidar[y][x])) / 10  # Gets thickness in metres at that coordinate

                # print(thickness)
                Radar[y][x] = 0

                # Sets the value of ice at that point to 0, to ensure it isnt counted on the next run for other icebergs
                # - ie makes it disappear

                # print(Radar[y][x]) # To test that it is changing the element to 0

                icemasscalc(thickness)

                x += 1

            if int(Lidar[y + 1][startx]) == 0:  # Checking if the next line is 0 (No more iceberg)

                completeiceberg = True  # If the next line doesnt contain any ice, the ice berg is complete

                for k in range(len(Ice2)):  # Sums ice mass of each pixel from list 'ice2' using loop
                    IceSum += Ice2[k]

                Ice2 = []  # Resets list of ice masses

                IceBergVol = IceSum * 9  # Multiples by 9 to get total mass as only 10% above water

                if IceBergVol < 36000000:  # Can only be towed if mass is less than 36m kg

                    outputtext = "Yes"

                else:

                    outputtext = "No"

                # Sets up text to be displayed

                TextDisp = tkinter.StringVar()

                label = tkinter.Label(gui, textvariable=TextDisp, background="White", foreground="Black",
                                      relief=RAISED, width=75,
                                      height=5)

                TextDisp.set(str(iceberg) + '\n'
                                            "Total Mass of Iceberg: " + str(
                    "{:,}".format(IceBergVol)) + "kg" + '\n' "Mass of Ice above sea level: "
                             + str("{:,}".format(IceSum)) + "kg" + '\n' "Able to be moved = " + outputtext)

                label.pack()

                print("Results Displayed")

                # Save to list for saving to file

                outputdata.append([iceberg, IceSum, IceBergVol, outputtext])

                # Resets variables

                line = -1  # -1 as the function will finish and y+1 will occur so to start reading the radar file again,
                # searching for more icebergs

                startx = 0

                foundiceberg = False

                elementnumber = 0

                x = 0

            y += 1  # Adds 1 to the y variable to move to next line of the iceberg, as long as it isnt complete


def run():
    print("Run Initiated")

    global startx
    global IceBergVol
    global outputdata
    global line
    global Ice2
    global foundiceberg
    i = 0
    global iceberg
    global x
    global y
    calccomplete = False

    iceberg = 0

    line = 0

    foundiceberg = False

    print("Running")

    # print(Lidar[197][33])

    # This runs through the radar environment

    while line < len(Radar):  # First loop takes calls row individually

        # print(Radar(r))

        # print(Radar[r])

        data = Radar[line]  # Data variable is filled with the radar data from the current line

        i = 0

        calccomplete = False

        y = line

        # print(line)  # Used for testing it reads the correct line

        while (calccomplete is False) & (i < len(data)):  # Loops through each element of the row

            x = i

            if int(data[i]) >= 100 and foundiceberg is False:  # If it hasnt found an iceberg and the data is ice:

                iceberg += 1  # Adds one to iceberg count

                print("Iceberg: " + str(iceberg))

                startx = i  # Left most x position of iceberg

                foundiceberg = True  # Set found iceberg to true

                # print(x, y)

                # print(Lidar[y][x])

            if foundiceberg is True:
                # If there is an iceberg already found, call calculation function passing in starting x and the row of data

                calciceberg(startx, data)

                calccomplete = True  # Stops the loop and restarts looking for icebergs

            i += 1  # Moves to the next element

        line += 1  # Loops to next line


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

print("Building Menu")

gui = tkinter.Tk()

gui.wm_title("Model")

gui.config(background="White")

gui.geometry("500x600")

menu_bar = tkinter.Menu(gui)

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

# Outputs to file

header = ['Iceberg', 'Ice above Sea Level', 'Total Iceberg Mass', 'Tugability']
output = open('Output_multi.csv', 'w', newline='')
writer = csv.writer(output)
writer.writerow(header)
writer.writerows(outputdata)

output.close()

gui.mainloop()
