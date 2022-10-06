# Create a parabola function
import math
import tkinter


def parabola(page, size):
	"""
	Takes a bunch of numbers and returns result
	"""
	for x in range(size):
		y = x * x / size
		plot(page, x, y)
		plot(page, -x, y)


# def circle(page, radius, g, h):
# 	"""
# 	Draw circle in more efficient manner than the original code (commented out)
# 	Uses optimized code
# 	"""
# 	page.create_oval(g + radius, h + radius, g - radius, h - radius, outline="red", width=2)
	# for x in range(g * 100, (g + radius)*100):
	# 	x /= 100
	# 	y = h + (math.sqrt(radius**2 - ((x - g)**2)))
	# 	plot(page, x, y)
	# 	plot(page, x, 2 * h - y)
	# 	plot(page, 2 * g -x, y)
	# 	plot(page, 2 * g -x, 2 * h - y)


# Modify the circle function to allow the color to be specified. red is the default one
def circle(page, radius, g, h, col="red"):
	"""
	Draw circle in more efficient manner than the original code (commented out)
	Uses optimized code
	"""
	page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=col, width=2)


def draw_axis(page):
	"""
	It will divide the canvas into 4 regions
	"""
	page.update()
	x_origin = page.winfo_width() / 2
	y_origin = page.winfo_height() / 2
	page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
	page.create_line(-x_origin, 0, x_origin, 0, fill="black")
	page.create_line(0, y_origin, 0, -y_origin, fill="black")
	print(locals())


def plot(page, x, y):
	page.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
# circle(canvas, 100, 100, 100)
# circle(canvas, 100, 100, -100)
# circle(canvas, 100, -100, 100)
# circle(canvas, 100, -100, -100)
# circle(canvas, 10, 30, 30)
# circle(canvas, 10, 30, -30)
# circle(canvas, 10, -30, 30)
# circle(canvas, 10, -30, -30)
# circle(canvas, 30, 0, 0)

circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100, col="blue")
circle(canvas, 100, -100, 100, col="green")
circle(canvas, 100, -100, -100, col="yellow")
circle(canvas, 10, 30, 30, col="black")
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()
