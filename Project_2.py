#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:20:45 2022

'''This is the main python file to run the program to calculate just one iceberg. It pulls files from the source folder
and writes to an export file. It creates the GUI, calculates ice presence, thickness then the volume of the iceberg.
The output file contains the iceberg number, total mass then mass above sea level. Version 1.0. MIT Licenced''

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


def icemasscalc(thickness):  # Function to calculate the mass of the iceberg above water for each pixel

    mass = thickness * 900  ''' Mass of ice (kg) = thickness (m) x 1 x 1 (Pixel size is 1x1m) x 900 (density per m3) x 1 is redundant
    mass = volume (same as thickness in this case) x density'''

    Ice.append(mass)  # Makes a list of ice masses for each pxiel


def run():
    print("Run Initiated")

    global IceSum
    global IceBergVol
    global outputdata
    global count

    for r in range(len(Radar)):  # First loop takes calls row individually

        # print(Radar(r))

        # print(Radar[r])

        data = Radar[r]  # Reads in the row of radar data

        # print(data)

        y = r  # Sets y equal to the row number - not necessarily needed but useful for clarity

        for i in range(len(data)):  # Second loop iterates through each element of the first list (row)

            # print(i)

            if data[i] >= str(100):  # Finds if there is ice from the radar value (greaater than 100)

                x = i  # Sets x equal to the element number - not necessarily needed but useful for clarity

                # print(x, y) - Used for testing to ensure it had the correct x and y value

                thickness = int((Lidar[y][x])) / 10  # Gets thickness in metres at that coordinate from the lidar

                print(thickness)  # Prints the thickness value

                icemasscalc(thickness)  # Calls the icemasscalc function passing in the thickness

    for i in range(len(Ice)):
        IceSum += Ice[i]

    # SeaLevelText = tkinter.Label(IceSum)
    # "Mass of Ice above sea level: " + "{:,}".format(IceSum) + "kg")

    # SeaLevelText.pack()

    # https://www.tutorialspoint.com/python/tk_label.htm

    IceBergVol = IceSum * 9  # Multiples by 9 to get total mass as only 10% above water

    if IceBergVol < 36000000:  # Can only be towed if mass is less than 36m kg

        outputtext = "Yes"

    else:

        outputtext = "No"

    Text = tkinter.StringVar()  # Set up to display a text box on the GUI

    label = tkinter.Label(gui, textvariable=Text, background="White", foreground="Black", relief=RAISED, width=75,
                          height=10)

    Text.set("Total Mass of Iceberg: " + str("{:,}".format(IceBergVol)) + "kg" + '\n' "Mass of Ice above sea level: "
             + str("{:,}".format(IceSum)) + "kg" + '\n' "Able to be moved = " + outputtext)

    label.pack() # Displays the text label

    outputdata = ['1', IceSum, IceBergVol, outputtext]  # Generates the output variable with iceberg number, above sea mass and total mass plus movability

    writer.writerow(outputdata)

    output.close()

    print("Results Displayed")


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

# Imports radar and lidar data from csv files

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

#  Sets up a column with 2 rows to display both radar and lidar picture

rows = 2

columns = 1

fig.add_subplot(rows, columns, 1)

matplotlib.pyplot.xlim(0, len(Radar[0]))

matplotlib.pyplot.ylim(0, len(Radar))

matplotlib.pyplot.imshow(Radar)  # Shows the radar plot

matplotlib.pyplot.title("Radar")

fig.add_subplot(rows, columns, 2)

matplotlib.pyplot.xlim(0, len(Lidar[0]))

matplotlib.pyplot.ylim(0, len(Lidar))

matplotlib.pyplot.imshow(Lidar)  # Shows the lidar plot

matplotlib.pyplot.title("Lidar")

matplotlib.pyplot.show()

gui.mainloop()
