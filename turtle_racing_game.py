
#import  modules

import turtle
import random
import time

#setting up screen for the game!
screen = turtle.Screen()
screen.bgcolor('lightblue') #background color 

#two players in this game. Whoever gets to the other side first wins

#Player One
player_one = turtle.Turtle()

#color of the player one
player_one.color('blue')

#make the player a turtle
player_one.shape('turtle')

#Player two setup 
player_two = player_one.clone()

#color of player two 
player_two.color('red')

#position the players 

#player_one position 
player_one.penup()
player_one.goto(-300, 200)

#player two position 
player_two.penup()
player_two.goto(-300, -200)

#draw a finish lin e
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish!', font = 40)


#allows player one to return to its starting position again 
player_one.penup()
player_one.color('blue')
player_one.goto(-300, 200)
player_one.right(90)


#make sure both players have their pens down 
player_one.pendown()
player_two.pendown()

#create values for the die
die = [1,2,3,4,5,6]

#create the game
for i in range (30):
    if player_one.position() >= (300, 250):
        print ("Player One Wins the Race!")
        break

    elif player_two.position() >= (300, -250):
        print ("Player Two Wins the Race!")
        break
    else: 
        die_roll = random.choice(die)
        player_one.forward(30 * die_roll) 
        
        time.sleep(1)

        die_roll2 = random.choice(die)
        player_two.forward(30 * die_roll2)
