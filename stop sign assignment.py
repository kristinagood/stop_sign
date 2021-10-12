import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
animation_speed = 0
distance = 90
sides = 8
angle = 45

turtle.setup(WINDOW_WIDTH,WINDOW_HEIGHT)

turtle.penup()
turtle.goto(-60, 130)
turtle.pendown()

for i in range(sides):
   turtle.forward(distance)
   turtle.right(angle)
   
turtle.hideturtle()

turtle.penup()
turtle.right(87)
turtle.forward(130)
turtle.color('black')
turtle.write('STOP', font=("Arial", 30, "normal"))

