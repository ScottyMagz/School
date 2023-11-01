imporrt random 
import time #Import Time Library For The 2 Second Delay After Calculation to Seem More Life Like




# Generates a Random Number Then Based on That Number Assigns a Color
def colorgenerator()
    color = int()
    color = random.randint(1,9)
    if color == 1:
        color = str()
        color = "red"
    elif color == 2:
        color = str()
        color = "blue"
    elif color == 3:
        color = str()
        color = "green"
    elif color == 4:
        color = str()
        color = "yellow"
    elif color == 5:
        color = str()
        color = "purple"
    elif color == 6:
        color = str()
        color = "white"
    else:
        color = str()
        color = "black"

    return color






#Determines If You Win or Lose
def calculation(usercolor,comcolor):

    if usercolor == comcolor:
        print(f"Your color is {comcolor}")
        time.sleep(2) # 2 second Delay
        print("I Win!!")
    else:
        print(f"Is Your Color {comcolor}")
        time.sleep(2)
        print("I Guess You Win !"





#The Main Function 
def main():
    usercolor = str()
    comcolor = str()
    print("Hello I Bet I Can Guess Your Favorite Color")
    usercolor = print("What Is Your Favorite Color ? ")
    usercolor = usercolor.lower() # Forces Lower Case
    comcolor = colorgenerator() 
    calculation(usercolor,comcolor)

main()