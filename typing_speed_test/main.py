#follow us at instagram www.instagram.com/python_coderz_ and ask if you have any query related to project 
#importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random
from tkinter import font


# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/


# creating window using gui
window = Tk()
window.title("typing speed test - @python_coderz_")

# the size of the window is defined
window.geometry("450x200")

x = 0

# defining the function for the test
def game():
	global x

	# loop for destroying the window
	# after on test
	if x == 0:
		window.destroy()
		x = x+1

	# defining function for results of test
	def check_result():
		if entry.get() == words[word]:

			# here start time is when the window
			# is opened and end time is when
			# window is destroyed
			end = timer()

			# we deduct the start time from end
			# time and calculate results using
			# timeit function
			print(end-start)
		else:
			print("Wrong Input")

	words = ['Follow', 'python_coderz_', 'at instagram',
			'for', 'getting latest', 'programs and tips']

	# Give random words for testing the speed of user
	word = random.randint(0, (len(words)-1))

	# start timer using timeit function
	start = timer()
	windows = Tk()
	windows.geometry("450x200")

	# use label method of tkinter for labeling in window
	x2 = Label(windows, text=words[word], font="times 20")

	# place of labeling in window
	x2.place(x=150, y=10)
	x3 = Label(windows, text="Start Typing", font="times 20")
	x3.place(x=10, y=50)

	entry = Entry(windows)
	entry.place(x=280, y=55)

	# buttons to submit output and check results
	b2 = Button(windows, text="Done",
				command=check_result, width=12, bg='#686de0', fg="white")
	b2.place(x=150, y=100)

	b3 = Button(windows, text="Try Again",
				command=game, width=12, bg='#6ab04c', fg="white")
	b3.place(x=250, y=100)
	windows.mainloop()


x1 = Label(window, text="Lets start playing..", font="times 20")
x1.place(x=10, y=50)

b1 = Button(window, text="Go", command=game, width=15,height=1, bg='#f0932b', fg="white", font="popins 20 bold")
b1.place(x=150, y=100)

# calling window
window.mainloop()
