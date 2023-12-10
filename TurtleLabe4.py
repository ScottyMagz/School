##Created on Mon Nov 06 15:10:30 2023
##Author:     Paralee Robinson, Matthew Sarns, Scott McAllister
##Program Name:   Rock, Paper, Scissors
##Description:    Rock, Paper, Scissors; winner wins best out of three games.
##Updates:

# import modules needed for operation
import random
import turtle
import time

def win():# Displays Win screen
    turtle.penup()
    turtle.hideturtle()
    turtle.bgcolor("royalblue")
    turtle.goto(-170,-0)
    turtle.write("You Win !",font=("Ariel",70))
    

def lose(): # Displays Lose screen
    turtle.penup()
    turtle.hideturtle()
    turtle.bgcolor("purple")
    turtle.goto(-190,0)
    turtle.write("You Lose !",font=("Ariel",70))


# Controls Background graphics
def backgorund():
    # CPU Side
    turtle.speed(800)
    turtle.goto(0,0)
    turtle.pendown()
    turtle.fillcolor("purple")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(410)
    turtle.left(90)
    turtle.forward(480)
    turtle.left(90)
    turtle.forward(840)
    turtle.left(90)
    turtle.forward(480)
    turtle.left(90)
    turtle.forward(440)
    turtle.end_fill()

    # Player Side
    turtle.goto(0,0)
    turtle.pendown()
    turtle.fillcolor("royalblue")
    turtle.begin_fill()
    turtle.forward(410)
    turtle.right(90)
    turtle.forward(480)
    turtle.right(90)
    turtle.forward(840)
    turtle.right(90)
    turtle.forward(480)
    turtle.right(90)
    turtle.forward(440)
    turtle.end_fill()

# Controls Game Scoring
def scoring (plyrscore,computer_score):

    # Handles Updating User Score
    turtle.speed(800)
    turtle.goto(0,0)
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(-300,270)
    turtle.write("Player Score",font=("Ariel",20))
    turtle.goto(-230,230)
    turtle.write(plyrscore,font=("Ariel",20))

    # Handles Computer Scores
    turtle.goto(0,0)
    turtle.penup()
    turtle.goto(160,270)
    turtle.write("CPU Score",font=("Ariel",20))
    turtle.goto(220,230)
    turtle.write(computer_score,font=("Ariel",20))
    

# Creates Rock Image
def rock():
    turtle.pendown()
    turtle.fillcolor("Grey")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()

# Creates Paper Image
def paper():
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(170)
    turtle.left(90)
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(170)
    turtle.end_fill()
    turtle.penup()

# Creates intro Scissors Image
def scissors():
    turtle.write("X",font=("Ariel",100))
    turtle.penup()
    turtle.goto(210,-260)  
    turtle.pendown()
    turtle.pensize(10)
    turtle.circle(35)
    turtle.penup()
    turtle.goto(290,-260)
    turtle.pendown()
    turtle.circle(35)
# usersside scissors
def usrscissors(): #Userside scissors
    turtle.write("X",font=("Ariel",100))
    turtle.penup()
    turtle.goto(-250,-0)   
    turtle.pendown()
    turtle.pensize(10)
    turtle.circle(35)
    turtle.penup()
    turtle.goto(-170,0)
    turtle.pendown()
    turtle.circle(35)
    turtle.penup()
    turtle.pensize(1)
# Userside scissors
def comscissors():#computerside scissors
    turtle.write("X",font=("Ariel",100))
    turtle.penup()
    turtle.goto(170,0)   
    turtle.pendown()
    turtle.pensize(10)
    turtle.circle(35)
    turtle.penup()
    turtle.goto(250,0)
    turtle.pendown()
    turtle.circle(35)
    turtle.penup()
    turtle.pensize(1)

 

# Intro Slide 
def intro():
    turtle.bgcolor("royal blue")
    turtle.speed(200)
    turtle.penup()
    turtle.hideturtle()
    # Rock Text and Image
    turtle.goto(-350,150)
    turtle.write("Rock",font=("Ariel",100))
    turtle.goto(150,150)
    rock()
    # Paoer Text an Image

    turtle.goto(0,-50)
    turtle.write("Paper",font=("Ariel",100))
    turtle.goto(-250,-50)   
    paper()

    # Scissors IMage and Text
    turtle.goto(-300,-250)
    turtle.write("Scissors",font=("Ariel",100))
    turtle.goto(250,-260)
    scissors()
    time.sleep(2)

# Handles Logic
def UserMakeChoice():
    turtle.clearscreen()
    user_selection = ["rock", "paper", "scissors"]

    # Variables
    user_score = 0
    computer_score = 0
    userside = (-220, 0)  # Coordinates for user's choice
    comside = (200, 0)    # Coordinates for computer's choice
    backgorund()


    scoring(user_score, computer_score)
    
    while user_score < 2 and computer_score < 2:  # Each game in the series
        computer_choice = random.choice(user_selection)
        user_choice = turtle.textinput("Rock, Paper, Scissors", "Enter a choice (rock, paper, scissors): ").lower()

        turtle.clearscreen()
        backgorund()
        scoring(user_score, computer_score)

        # Display user's choice
        turtle.goto(userside)
        if user_choice == "rock":
            rock()
        elif user_choice == "paper":
            turtle.left(90)
            paper()
        elif user_choice == "scissors":
            usrscissors()

        # Display computer's choice
        turtle.goto(comside)
        if computer_choice == "rock":
            rock()
        elif computer_choice == "paper":
            turtle.left(90)
            paper()
        elif computer_choice == "scissors":
            comscissors()

        # Handle game logic
        if user_choice == computer_choice:  # Handles Ties
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") \
                or (user_choice == "paper" and computer_choice == "rock") \
                or (user_choice == "scissors" and computer_choice == "paper"):
            print(f"{user_choice.capitalize()} beats {computer_choice}! You won!")
            user_score += 1
        else:  # If not classified as a Win From Above Section
            print(f"{computer_choice.capitalize()} beats {user_choice}! You lost.")
            computer_score += 1
        
        time.sleep(2)  # Pause to view choices
        turtle.clearscreen()
        backgorund()
        scoring(user_score, computer_score)

        # Handle game end
        if user_score == 2:
            turtle.clearscreen()  # Starts the Game Reset Loop
            win()
            user_score = 0
            computer_score = 0
            time.sleep(5)
            answer = turtle.textinput("Continue","Press Q to quit: ").lower()
            if answer == "q": # Asks if you want to continue
                turtle.bye()
            else:
                backgorund()
                scoring(user_score, computer_score)
        elif computer_score == 2:
            turtle.clearscreen()  # Starts the Game Reset Loop
            lose()
            user_score = 0
            computer_score = 0
            time.sleep(5)
            answer = turtle.textinput("Continue","Press Q to quit: ")
            if answer == "q": # Asks if you want to continue 
                turtle.bye()
            else:
                backgorund()
                scoring(user_score, computer_score)

    return user_score, computer_score

#Main Loop
def main():
    turtle.Screen().title("Rock, Paper, Scissors Game")
    intro()
    user_score, computer_score = UserMakeChoice()

#Calling Main Loop 
main()
