import turtle
import time 




def trace ():
    #Retracing Steps

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    time.sleep(3)
    turtle.reset()











## For Drwaing Shapes I Need to implement a Decision Structure So User Input Validation 



def drawing_shapes():    
    #Variables 
    pen_color = str()
    fill_color = str()
    pen_size= int()
    colors = ["red","blue","yellow",""]
    size_range = range(0,16)



    #Prompting User For Inputs
    pen_color = turtle.textinput("Pick a Color","What Pen Color Red, Blue, or Yellow ?")
    pen_color.lower()
    if pen_color not in colors:
        print("Try Again")
        pen_color = turtle.textinput("Pick a Color","What Pen Color Red, Blue, or Yellow ?")
        pen_color.lower
    else:
        print(f"Your Color is {pen_color} ")




    fill_color = turtle.textinput("Pick a Color","What Fill Color Red, Blue, or Yellow ?")
    fill_color.lower()
    if fill_color not in colors:
        print("Try Again")
        fill_color = turtle.textinput("Pick a Color","What Fill Color Red, Blue, or Yellow ?")
        fill_color.lower()
    else:
        print(f"Your Color is {fill_color} ")


    pen_size = int(turtle.textinput("Pensize","What Pen Size 1-15 ?"))
    if pen_size not in  size_range:
        print("Try Again")
        pen_size = int(turtle.textinput("Pensize","What Pen Size 1-15 ?"))
    else:
        print(f"Your Pen Size is {pen_size}")




    #Moves The Turtle
    turtle.penup()
    turtle.goto(0,150)
    turtle.pendown()
    turtle.pensize(pen_size)
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    #Draws Circle
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    #Moves The Pen for Square
    turtle.penup()
    turtle.right(90)
    turtle.forward(150)

    #Makes Square
    pen_color = turtle.textinput("Pick a Color","What Pen Color Red, Blue, or Yellow ?")
    pen_color.lower()
    if pen_color not in colors:
        print("Try Again")
        pen_color = turtle.textinput("Pick a Color","What Pen Color Red, Blue, or Yellow ?")
        pen_color.lower()
    else:
        print(f"Your Color is {pen_color} ")
    turtle.pencolor(pen_color)

    fill_color = turtle.textinput("Pick a Color","What Fill Color Red, Blue, or Yellow ?")
    fill_color.lower()
    if fill_color not in colors:
        print("Try Again")
        fill_color = turtle.textinput("Pick a Color","What Fill Color Red, Blue, or Yellow ?")
        fill_color.lower()
    else:
        print(f"Your Color is {fill_color} ")

    turtle.fillcolor(fill_color)
    pen_size = int(turtle.textinput("Pensize","What Pen Size 1-15 ?"))
    if pen_size not in  size_range:
        print("Try Again")
        pen_size = int(turtle.textinput("Pensize","What Pen Size 1-15 ?"))
    else:
        print(f"Your Pen Size is {pen_size}")

    turtle.pensize(pen_size)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(150)


    pen_color = turtle.textinput("Pick a Color","What Pen Color Red, Blue, or Yellow ?")
    pen_color.lower()
    if pen_color not in colors:
        print("Try Again")
        pen_color = turtle.textinput("Pick a Color","What Pen Color Red, Blue, or Yellow ?")
        pen_color.lower()
    else:
        print(f"Your Color is {pen_color} ")


    fill_color = turtle.textinput("Pick a Color","What Fill Color Red, Blue, or Yellow ?")
    fill_color.lower()
    if fill_color not in colors:
        print("Try Again")
        fill_color = turtle.textinput("Pick a Color","What Fill Color Red, Blue, or Yellow ?")
        fill_color.lower()
    else:
        print(f"Your Color is {fill_color} ")

    pen_size = int(turtle.textinput("Pensize","What Pen Size 1-15 ?"))
    if pen_size not in  size_range:
        print("Try Again")
        pen_size = int(turtle.textinput("Pensize","What Pen Size 1-15 ?"))
    else:
        print(f"Your Pen Size is {pen_size}")
    turtle.pendown()
    turtle.pensize(pen_size)
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()

    #Drawing Triangle
    turtle.right(35)
    turtle.forward(125)
    turtle.right(235)
    turtle.forward(150)
    turtle.left(127)
    turtle.forward(130)
    turtle.end_fill()
    time.sleep(3)
    turtle.reset()

def drawing_circ():
    #Variables
    horizontal = int()
    radius = int()
    colors = ["red","blue","yellow","green"]
    pen_size = int()
    horizontal = -200
    radius = 25
    pen_size = 2

    #Starting Postion
    turtle.penup()
    turtle.goto(horizontal,0)
    turtle.pendown()

#Makes Circles 
    for count in range(0,4):
        turtle.fillcolor(colors[count])
        turtle.pensize(pen_size)
        turtle.begin_fill()
        #Draws circles
        turtle.circle(radius)
        #resets location radius and pen size
        horizontal = horizontal + 75
        radius = radius + 20
        pen_size = pen_size + 2
        #moving the turtle
        turtle.penup()
        turtle.goto(horizontal, 0)
        turtle.pendown()
        turtle.end_fill()
    time.sleep(3)
    turtle.reset()


#Function to Send Turtle to Middle of Screen And Print The End
def final():
    turtle.penup()
    turtle.goto(0,0)
    turtle.hideturtle()
    turtle.write("The End", align="center", font=('Arial', '16', 'bold'))
    time.sleep(3)
    turtle.reset()

#Main Function To Organize Execution 
def main():
    trace()
    drawing_shapes()
    drawing_circ()
    final()
#Calling Main Function 
main()