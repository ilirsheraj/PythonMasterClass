import tkinter

main_window = tkinter.Tk()
main_window.title("Hello World")
main_window.geometry("640x480+8+200")  # Pass a string, not int or float

label = tkinter.Label(main_window, text="Hello World")
label.grid(row=0, column=0)

# Add left frame
left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

# Add right frame
right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky="n")

# Add buttons
button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configure the columns
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

left_frame.config(relief="sunken", borderwidth=1)
right_frame.config(relief="sunken", borderwidth=1)
left_frame.grid(sticky="ns")
right_frame.grid(sticky="new")

right_frame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")

# This runs the code
main_window.mainloop()
