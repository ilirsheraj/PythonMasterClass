try:
	import tkinter
except ImportError: # For Python 2
	import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# # tkinter._test()

# Another way to get the window, this time customized
main_window = tkinter.Tk()
main_window.title("Hello World")
main_window.geometry("640x480+8+400") # Pass a string, not int or float

label = tkinter.Label(main_window, text="Hello World")
label.pack(side="top")

# canvas = tkinter.Canvas(main_window, relief="raised", borderwidth=1)
# canvas.pack(side="top")
# canvas.pack(side="left", fill=tkinter.X, expand=True)
# canvas.pack(side="top", fill=tkinter.Y, expand=True)
# canvas.pack(side="top", fill=tkinter.BOTH, expand=True)
# button1 = tkinter.Button(main_window, text="button1")
# button2 = tkinter.Button(main_window, text="button2")
# button3 = tkinter.Button(main_window, text="button3")
# button1.pack(side="top", anchor="n")
# button2.pack(side="top", anchor="s")
# button3.pack(side="top", anchor="e")

# Add left frame
left_frame = tkinter.Frame(main_window)
left_frame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")

# Add right frame
right_frame = tkinter.Frame(main_window)
right_frame.pack(side="right", anchor="n", expand=True)

# Add buttons
button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")

# This runs the code
main_window.mainloop()
