import turtle

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

col=('red','yellow','green','cyan','pink',
'white')

t=turtle.Turtle()

screen=turtle.Screen()
screen.bgcolor('black')
t.speed(25)

for i in range (150):

    t.color(col[i%6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)