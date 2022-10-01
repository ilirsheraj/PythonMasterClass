# # import turtle
# # import time
#
# # Import only some methods and remove turtle.
# from turtle import forward, right, done
# # Or you can combine both :)
# import turtle

# A third way to import is importing everything with star
# Generally its good practice to avoid this approach
from turtle import *

# # noinspection PyUnresolvedReferences
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
#
# # # With this we give time to the figure to stay on the screen for 4 seconds
# # time.sleep(4)
#
# # Another way to see the same effects is to use turtle done
# # It will not close unless we close it ourselves
# turtle.done()

forward(150)
right(250)
# turtle.circle(75)
circle(75)
forward(150)
done()
