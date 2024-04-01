import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

root = tk.Tk()
root.title("Traffic Light Simulation")

canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()

# Create the red light
red_light = canvas.create_oval(25, 25, 75, 75, fill="gray")
# Create the yellow light
yellow_light = canvas.create_oval(25, 100, 75, 150, fill="gray")
# Create the green light
green_light = canvas.create_oval(25, 175, 75, 225, fill="gray")

def change_light():
    current_color_red = canvas.itemcget(red_light, 'fill')
    current_color_yellow = canvas.itemcget(yellow_light, 'fill')
    current_color_green = canvas.itemcget(green_light, 'fill')
    
    if current_color_red == "gray" and current_color_yellow == "gray" and current_color_green == "gray":
        canvas.itemconfig(red_light, fill="red")
        engine.say("Red")
        engine.runAndWait()
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="gray")
        
    elif current_color_red == "red":
        engine.say("Yellow")
        engine.runAndWait()
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="yellow")
        canvas.itemconfig(green_light, fill="gray")
        
    elif current_color_yellow == "yellow":
        engine.say("Green")
        engine.runAndWait()
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="green")
        
    elif current_color_green == "green":
        engine.say("Red")
        engine.runAndWait()
        canvas.itemconfig(red_light, fill="red")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="gray")
    
    root.after(2000, change_light)

change_light()

root.mainloop()