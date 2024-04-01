# Helping-the-blind

This program simulates a traffic light using the tkinter library for creating the GUI and pyttsx3 for text-to-speech functionality.
Installation
    Make sure you have Python installed on your system.
    Install the required packages by running the following command:

    pip install tk pyttsx3

        

How to Run
    Clone or download the repository to your local machine.
    Navigate to the directory where the files are located.
    Run the following command to start the program:

          

    python traffic_light_simulation.py

        

Usage

    The program will display a window with a simulated traffic light.
    The lights will change from red to yellow to green and back to red in a loop.
    The program will also announce the current light using text-to-speech.

Code Overview

    The program uses tkinter to create the GUI window and draw the traffic light.
    The change_light function handles the logic for changing the lights and announcing the current light.
    The program continuously runs the change_light function using the root.after method to create a loop.

Feel free to explore and modify the code to customize the simulation to your liking. Enjoy simulating traffic lights!
