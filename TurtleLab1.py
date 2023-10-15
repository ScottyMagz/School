#Importing the Turtle Library 
import turtle 

#initilizes Turtle
turtle.shape("turtle")
turtle.color("green")

#Creating the Yello Circle
turtle.pencolor("yellow")
turtle.penup()
turtle.goto(200,100)
turtle.pensize(10)
turtle.fillcolor("purple")
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()

#Changes Turtle Back to Green
turtle.color("green")


#Creating Square 
turtle.pensize(5)
turtle.goto(-200,-200)
turtle.pencolor("purple")
turtle.fillcolor("Yellow")
turtle.begin_fill()
turtle.pendown()
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.end_fill()
turtle.penup()

#Changes Turtle Back to Green 
turtle.color("Green")

#Creates Last Shape 
turtle.pensize(15)
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.goto(1, 100)
turtle.begin_fill()
turtle.pendown()
turtle.goto(-100, 1)
turtle.goto(1, 1)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
turtle.penup()


#Changes Turtle once again back to Green 
turtle.color("Green")

#Puts Turtle Back To 0
turtle.goto(0,0)
