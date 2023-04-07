import tkinter as tk

def convert():
    temp_c = float(input_c.get())
    temp_f = temp_c * 9/5 + 32
    label['text'] = temp_f

# window
window = tk.Tk()

input_c = tk.Entry(window)
input_c.grid(row=0, column=0)

button_covert = tk.Button(window, text="Convert", command=convert)
button_covert.grid(row=0, column=1)

label = tk.Label(window)
label.grid(row=1, column=0)

# run
window.mainloop()