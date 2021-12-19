import turtle

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

j = 1
t = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("Black")
t.pencolor("Yellow")
t.speed(0)
for i in range(300):
    t.forward(j)
    t.left(120)
    t.left(1)
    j += 1

turtle.done()
