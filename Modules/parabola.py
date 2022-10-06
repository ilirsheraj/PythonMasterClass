# Create a parabola function
import tkinter


def parabola(x):
	"""
	Takes a bunch of numbers and returns result
	:param x: integers or floats
	:return: integers or float
	"""
	y = x * x / 100
	return y


def draw_axis(canvas):
	"""
	It will divide the canvas into 4 regions
	"""
	canvas.update()
	x_origin = canvas.winfo_width() / 2
	y_origin = canvas.winfo_height() / 2
	canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
	canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
	canvas.create_line(0, y_origin, 0, -y_origin, fill="black")
	print(locals())


def plot(canvas, x, y):
	canvas.create_line(x, y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)

for x in range(-100, 101):
	y = parabola(x)
	plot(canvas, x, -y)

mainWindow.mainloop()
