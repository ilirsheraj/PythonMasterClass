import os
import tkinter

main_window = tkinter.Tk()
main_window.title("Grid Demo")
main_window.geometry("640x480+8+200")

label = tkinter.Label(main_window, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=3)
main_window.columnconfigure(3, weight=3)
main_window.columnconfigure(4, weight=3)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(main_window)
fileList.grid(row=1, column=0, sticky="nsew", rowspan=2)
fileList.config(border=2, relief="sunken")

# Populate the list box
for zone in os.listdir("/usr/bin"):
	fileList.insert(tkinter.END, zone)

# Add a scrollbar
listScroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
fileList["yscrollcommand"] = listScroll.set

# Create a frame for radio buttons
optionFrame = tkinter.LabelFrame(main_window, text="File Details")
optionFrame.grid(row=1, column=2, sticky="ne")

rbValue = tkinter.IntVar()
rbValue.set(3)

# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky="w")
radio2.grid(row=2, column=0, sticky="w")
radio3.grid(row=3, column=0, sticky="w")

main_window.mainloop()

print(rbValue.get())
