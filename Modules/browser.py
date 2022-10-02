# The webBrowser module
import webbrowser

# # To automatically open Python's web browser
# new = 1, a new browser window will be opened
# webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)

## This version does not work on linux
# chrome = webbrowser.get(using="google-chrome")
# webbrowser.open_new("https://www.python.org/")

# This version works on linux
chrome = webbrowser.get("google-chrome %s").open("https://www.python.org/")

# for i in range(10):
#     print(1,2,3,4,5,6,7,8,9, sep=';', end=' ')
