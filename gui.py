import csv
from tkinter import *

import Shape
from Shape import *

class GUI:
    def __init__(self, window):

        self.window = window

        self.frame_number = Frame(self.window)
        self.label_number = Label(self.frame_number, text='num1')
        self.entry_number = Entry(self.frame_number)
        self.label_number.pack(padx=5, side='left')
        self.entry_number.pack(padx=5, side='left')
        self.frame_number.pack(anchor='w', pady=10)

        self.Aframe_number = Frame(self.window)
        self.Alabel_number = Label(self.Aframe_number, text='num2')
        self.Aentry_number = Entry(self.Aframe_number)
        self.Alabel_number.pack(padx=5, side='left')
        self.Aentry_number.pack(padx=5, side='left')
        self.Aframe_number.pack(anchor='w', pady=10)


        self.Sframe_number = Frame(self.window)
        self.Slabel_number = Label(self.Sframe_number, text='Shape')
        self.Slabel_number.pack(padx=5, side='left')
        self.Sframe_number.place(x=0,y=85)
        self.V = IntVar()
        self.V2 = IntVar()
        self.Rs = Radiobutton(self.window, text='Triangle', variable=self.V, value=1)
        self.Rt = Radiobutton(self.window, text='Square', variable=self.V, value=2)
        self.Rb = Radiobutton(self.window, text='Rectangle', variable=self.V, value=3)
        self.Area = Radiobutton(self.window, text='Area', variable=self.V2, value=1)
        self.Perimiter = Radiobutton(self.window, text='Perimiter', variable=self.V2, value=2)
        self.Rs.place(x=75, y=80)
        self.Rt.place(x=180, y=80)
        self.Rb.place(x=275, y=80)
        self.Area.place(x=185, y=50)
        self.Perimiter.place(x=275, y=50)

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(anchor='s',pady=50)
        self.frame_result.pack()

        button = Button(self.window, text='Calculate', command=self.clicked)
        button.place(x=160, y=165)
    def clicked(self):
        first_num = int(self.entry_number.get())
        second_num = int(self.Aentry_number.get())
        var = self.V.get()
        var2 = self.V2.get()
        if var == 1 and var2 ==1:
            self.label_result.config(text=f'{Shape.triangle_area(first_num,second_num)}')
        elif var == 1 and var2 ==2:
            self.label_result.config(text=f'{Shape.triangle_perimeter(first_num,second_num,0)}')
        elif var == 2 and var2 ==1:
            self.label_result.config(text=f'{Shape.triangle_area(first_num,second_num)}')
        if var == 1 and var2 ==1:
            self.label_result.config(text=f'{Shape.triangle_area(first_num,second_num)}')
        if var == 1 and var2 ==1:
            self.label_result.config(text=f'{Shape.triangle_area(first_num,second_num)}')



