# pip install turtle
import turtle

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/


obj = turtle.Turtle()
list = ["red", "green", "blue", "orange", "yellow", "light green"]
obj.speed(0) #fastest speed
obj_ = turtle.Screen()
obj_.title("NEXT CODERS")
obj_.bgcolor("black")
for i in range(300):
    obj.pensize(i/100+1)
    obj.color(list[i % 6])
    obj.forward(i)
    obj.left(59)

turtle.done()
