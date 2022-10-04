import os
import tkinter

main_window = tkinter.Tk()
main_window.title("Grid Demo")
main_window.geometry("640x480+8+200")

# Add Padding
main_window["padx"] = 8

label = tkinter.Label(main_window, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

main_window.columnconfigure(0, weight=100)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1000)
main_window.columnconfigure(3, weight=600)
main_window.columnconfigure(4, weight=1000)

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

# Widget to display results
resultLabel = tkinter.Label(main_window, text="Result")
resultLabel.grid(row=2, column=2, sticky="nw")
result = tkinter.Entry(main_window)
result.grid(row=2, column=2, sticky="sw")

# Frame for the time spinners
timeFrame = tkinter.LabelFrame(main_window, text="Time")
timeFrame.grid(row=3, column=0, sticky="new")
# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=":").grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=":").grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame["padx"] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(main_window)
dateFrame.grid(row=4, column=0, sticky="new")
# Date Labels
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
dayLabel.grid(row=0, column=0, sticky="w")
monthLabel.grid(row=0, column=1, sticky="w")
yearLabel.grid(row=0, column=2, sticky="w")

# Date Spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=0, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5,
							values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# Add OK and Cancer buttons
okButton = tkinter.Button(main_window, text="OK")
# main_window.destroy will close it
cancelButton = tkinter.Button(main_window, text="Cancel", command=main_window.destroy)
okButton.grid(row=4, column=4, sticky="w")
cancelButton.grid(row=4, column=4, sticky="e")

main_window.mainloop()

print(rbValue.get())
