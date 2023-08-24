import tkinter as tk
import  ttkbootstrap as ttk

# window
window = ttk.Window(themename="darkly")
window.title("Edinbo")
window.geometry("300x150")

def convert():
    output_string.set(str(float(entryint.get())*1.61))

title_label = ttk.Label(master=window, text="Kilometers To Miles", font="Calibri 24 bold" )
title_label.pack()


entry_frame = ttk.Frame(master=window)
entryint = tk.IntVar()
entry = ttk.Entry(master=entry_frame, textvariable=entryint)
button = ttk.Button(master=entry_frame,  text="Convert", command=convert)
entry_frame.pack(pady=10)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")

output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="output", font="Calibri 24", textvariable= output_string)
output_label.pack()

window.mainloop()
