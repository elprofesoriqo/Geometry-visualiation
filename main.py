from tkinter import *
import math
import matplotlib.pyplot as plt
import numpy as np

# Main window
window = Tk()
window.minsize(height=500, width=800)
window.title('Analytical Geometry Tasks')

# Function to check if a point is inside a circle
def kolko():
    p = int(promien.get())
    sr = [int(x) for x in srodek.get().split(",")]
    punkt = [int(x) for x in pu.get().split(",")]
    if math.sqrt(pow(punkt[0] - sr[0], 2) + pow(punkt[1] - sr[1], 2)) <= p:
        wynik = Label(text='Does the point belong to the circle? Yes', font=('Arial', 13))
    else:
        wynik = Label(text='Does the point belong to the circle? No', font=('Arial', 13))
    wynik.grid(column=0, row=11)

# Function to calculate if the point is on the line
class Zadanie1:
    def __init__(self, prosta, punkt):
        self.prosta = prosta
        self.punkt = punkt

    def odleglosc(self):
        d = abs(self.prosta[0] * self.punkt[0] + self.prosta[1] * self.punkt[1] + self.prosta[2]) / math.sqrt(pow(self.prosta[0], 2) + pow(self.prosta[1], 2))
        return d == 0

def dane():
    prosta = [int(x) for x in p.get().split(' ')]
    punkt = [int(x) for x in pu.get().split(",")]
    dane = Zadanie1(prosta, punkt)
    wynik = Label(text=f'Does the point belong to the line? {dane.odleglosc()}', font=('Arial', 16))
    wynik.grid(column=0, row=8)

# Function to draw the line
def f(x, pros):
    return (pros[0] * x + pros[2]) / pros[1]

def rys():
    pros = [int(x) for x in p.get().split(' ')]
    punk = [int(x) for x in pu.get().split(",")]
    xlist = np.linspace(-10, 10)
    ylist = f(xlist, pros)
    plt.plot(xlist, ylist)
    plt.title("Graph of the Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.scatter([punk[0]], [punk[1]], color="red")
    plt.show()

# Task selection
def show_task():
    selected_task = task_var.get()
    if selected_task == "Circle":
        circle_frame.pack(fill='both', expand=True)
        line_frame.pack_forget()
    elif selected_task == "Line":
        line_frame.pack(fill='both', expand=True)
        circle_frame.pack_forget()

# Task selection UI
task_var = StringVar(value="Circle")
task_menu = OptionMenu(window, task_var, "Circle", "Line", command=lambda _: show_task())
task_menu.grid(column=0, row=0)

# Circle task UI
circle_frame = Frame(window)
srodek_l = Label(circle_frame, text='Enter the center value: (x,y)').grid(column=0, row=0)
srodek = Entry(circle_frame, width=30)
srodek.grid(column=0, row=1)
punkt_l = Label(circle_frame, text='Enter the coordinates of the point: (x,y)').grid(column=0, row=2)
pu = Entry(circle_frame, width=30)
pu.grid(column=0, row=3)
promien_l = Label(circle_frame, text='Enter the radius value:').grid(column=0, row=4)
promien = Entry(circle_frame, width=30)
promien.grid(column=0, row=5)
button = Button(circle_frame, text='Check', command=kolko)
button.grid(column=0, row=6)

# Line task UI
line_frame = Frame(window)
prosta_wyg = Label(line_frame, text='The line is represented as: Ax + By + C = 0', font=('Arial', 24)).grid(column=0, row=0)
prosta_l = Label(line_frame, text='Enter values for A B C separated by spaces:').grid(column=0, row=1)
p = Entry(line_frame, width=30)
p.grid(column=0, row=2)
punkt_l = Label(line_frame, text='Enter the coordinates of the point: (x,y)').grid(column=0, row=3)
pu = Entry(line_frame, width=30)
pu.grid(column=0, row=4)
button = Button(line_frame, text='Check', command=dane)
button.grid(column=0, row=5)
button_graph = Button(line_frame, text='Draw', command=rys)
button_graph.grid(column=1, row=5)

# Show the default task (circle)
show_task()

window.mainloop()
