from tkinter import *

root = Tk()
root.geometry("500x500")
root.config(bg="lightblue")
root.title("C to F Converter")

#content 👇🏼

a = IntVar()
b = IntVar()

Scale(from_= -12000, to=12000, font=("Impact", 25), bg="lightblue", fg="black", orient="horizontal", variable=a).pack()

Radiobutton(text="Celsius to Fahrenheit", font=("Impact", 15), bg="lightblue", fg="black", variable=b, value=1).pack()

Radiobutton(text="Fahrenheit to Celsius", font=("Impact", 15), bg="lightblue", fg="black", variable=b, value=2).pack()

def convert():
    if b.get() == 1:
        Label(text=f"{(a.get() * 1.8) + 32}°F", font=("Impact", 15), bg="lightblue", fg="black").pack()
    elif b.get() == 2:
        Label(text=f"{(b.get() / 1.8) - 32}°F", font=("Impact", 15), bg="lightblue", fg="black").pack() 

Button(text="convert", font=("Impact", 25), bg="yellow", fg="black", command=convert).pack()

#content ☝🏼

root.mainloop()