# Assignment 2 - White Star Line

# BACKGROUND

This assignment is designed to test the python knowledge developed through the course following on from the submission of our practical assessments. In this instance the program is designed to determine whether ice bergs are capable of being moved by a tug boat. The radar and lidar data are displayed on a canvas using

The criteria for the model are:

- Pull in the data files (Lidar and Radar data)
- Determine which areas are ice. Radar determines if there is ice, with values 100-255 being ice. Lidar determines thickness with one unit being 10cm oof thickness
- Assess ice mass above sea level, assuming 900kg/m3 density
- Calculate total ice mass if 90% of the ice is below the sea level
- If the total volume is less than 36m kg then it can be towed out of the ships path
- Display total mass, total volume and if the iceberg can be towed
- Save the information to a filel

The program is run through command prompt (PC) or terminal (Mac). It should be noted this program has been developed and tested on a Mac through terminal, hence instructions will primarily focus on Mac use but with additional details on Windows use, although there may be some unexpected differences.

# CONTENTS

- Licence - This program is licenced with an MIT licence and can be accessed in the GitHub library
- Project_2.py - The main model file where the lists are set up, libraries imported, GUI created, files imported and exported. This processes the files with a single ice bergs
- Project_2_Extra.py - The extension model file where the lists are set up, libraries imported, GUI created, calculations performed and files imported and exported. This processes the files with multiple ice bergs
- README.md
- Lidar.csv - The file containing LIDAR data, values 0 to 255
- Radar.csv - The file containing radar data, values 0 to 255
- Lidar2.csv - The file containing LIDAR data of multiple ice bergs, values 0 to 255
- Radar2.csv - The file containing radar data of multiple ice bergs, values 0 to 255

# RUNNING THE PROGRAM & EXPECTATIONS

1) Download all code from the Assignment 2 GitHub repository then extract. Code > Download Zip > Extract All
2) Open terminal with the extracted folder as directory (Mac > 'New Terminal at Folder' ¦ Windows > Type cmd then enter into address bar while in the chosen folder)
3) Type 'python' then either 'Project_2.py' or 'Project_2_Extra'
4) The matplootlib pyplot of the radar and lidar files will display in the GUI
5) The model window will open, select Model > Run Model
6) The model will run (it will say so in command prompt)
7) The figures for the ice berg(s) will be displated in the GUI
8) When the program has finished running, the final plot will be output as a PDF into the original folder where extraction occurred in step 1 and saved to a csv file - either output.csv for the single ice berg program ro output2.csv for the multiple ice berg program.

# TESTING

Testing was conducted throughout using PyCharm CE's debugger, variable watcher and simple print statements. Some statements remain in the code commented out but others remain for user guidance such as the iteration step, variables inputted, when functions are called and the end of the program.

# KNOWN ISSUES/FURTHER DEVELOPMENT

-
-
-

# WEBSITE

See https://gy17rawg.github.io/
