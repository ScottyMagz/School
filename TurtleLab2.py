# Imports Libraries
import turtle
import random
import math
import time

def play_game():
    turtle.clearscreen()  # Clear the screen for a new game
    turtle.speed(300)
    turtle.hideturtle()
    turtle.penup()
    
    # Sets Color Scheme 
    turtle.color("White")
    turtle.bgcolor("black")

    # Stores Possible Choices in an Array
    shapeSelection = ["classic","arrow","circle","square","triangle","turtle"]

    circSize = random.randrange(70,90)
    cir_x = random.randint(-200,200)
    cir_y = random.randint(-200,200)

    while -100 <= cir_x <= 100 or -100 <= cir_y <= 100:
        cir_x = random.randint(-200,200)
        cir_y = random.randint(-200,200)

    turtle.goto(cir_x, cir_y)
    # Creates The Circle
    turtle.penup()
    turtle.circle(circSize)
    turtle.pendown()
    turtle.circle(circSize)
    # Starts Player in Center
    turtle.penup()
    turtle.goto(0,0)
    turtle.showturtle()
    turtle.speed(1)
    # Asks User What Shape and User Input Validation
    user_shape = turtle.textinput("Choose Turtle Shape", "Enter a shape (classic, arrow, turtle, circle, square, or triangle):")
    user_shape = user_shape.lower()
    while user_shape not in shapeSelection:
        user_shape = turtle.textinput("Choose Turtle Shape", "Enter a shape (classic, arrow, turtle, circle, square, or triangle):")
    else:
        print(f"You Chose {user_shape}")

    turtle.shape(user_shape)

    # Estimate turtle shape size for detection accuracy
    turtle_shape_size = 25  # Adjust this value based on the shape of the turtle
    detection_radius = circSize + turtle_shape_size / 2

    # Sets Number of tries
    for counter in range(1,10):
        # Prompts User to Input Direction
        directionSelection = ["up","down","left","right"]
        user_direction = turtle.textinput("Choose a Direction","Do you Want to go (Left, Right, Up, or Down ?):")
        user_direction = user_direction.lower()
        while user_direction not in directionSelection:
            user_direction = turtle.textinput("Do you Want to go Left, Right, Up, or Down ?")
            user_direction = user_direction.lower() 
        else:
            print(f"You Chose {user_direction}")

        # Assigns Angle to Worded Direction
        if user_direction == "right":
            turtle.setheading(0)
        elif user_direction == "left":
            turtle.setheading(180)
        elif user_direction == "up":
            turtle.setheading(90)
        elif user_direction == "down":
            turtle.setheading(270)

        # Sets Movement Distances
        user_movement = turtle.numinput("How Far would You Like to Move","How Far Would You Like to Move ?:")
        math.floor(user_movement)

        turtle.forward(user_movement)
        
        # If statement to Determine if Turtle is in Circle
        distance = math.sqrt((turtle.xcor() - cir_x) ** 2 + (turtle.ycor() - cir_y) ** 2)
        if distance <= detection_radius:
            print("Turtle is inside the circle.")
            turtle.hideturtle()
            turtle.goto(0,0)
            turtle.showturtle()
            turtle.write("You Win !", align="center", font=('Arial', '16', 'bold'))
            time.sleep(5)
            turtle.clearscreen()
            # Restart the game
            play_game()  
            # Exit the current game
            return  

        else:
            print("Turtle is outside the circle.")

    turtle.hideturtle()
    turtle.goto(0,0)
    turtle.showturtle()
    time.sleep(5)
    turtle.write("Sorry You Lost", align="center", font=('Arial', '16', 'bold'))

play_game()
turtle.exitonclick()
