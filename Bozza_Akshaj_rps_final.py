# This file was created by Akshaj Bozza

# importing the necessary modules

import turtle
from turtle import *
from random import randint
choices = ["rock", "paper", "scissors"]
cpuchoice = choices[randint(0,2)]

 

# The os module allows us to access the current directory in order to access assets

import os

# setup the width and height for the window

WIDTH, HEIGHT = 1000, 400

 

#  using dimensions of the images to determine the length and width of the images

rock_w, rock_h = 256, 280
paper_w, paper_h = 256, 204
scissors_w, scissors_h = 256, 170

# setup the game folders using the os module

game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')


# setup the Screen class using the turtle module

screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="light green")

 

# setup the rock image using the os module as rock_image

rock_image = os.path.join(images_folder, 'rock.gif')
cpu_rock = os.path.join(images_folder, 'rock.gif')
paper_image = os.path.join(images_folder, 'paper.gif')
cpu_paper = os.path.join(images_folder, 'paper.gif')
scissors_image = os.path.join(images_folder, 'scissors.gif')
cpu_scissors = os.path.join(images_folder, 'scissors.gif')

# instantiate (create an instance of) the Turtle class for the rock, paper, and scissors.

rock_instance = turtle.Turtle()
cpu_rock_instance = turtle.Turtle() # creating a CPU turtle
cpu_rock_instance.hideturtle() # hiding it as the player hasn't chosen what they are, and the CPU chooses after the player
cpu_rock_instance.penup() #preventing a line from forming upon moving the CPU
paper_instance = turtle.Turtle()
cpu_paper_instance = turtle.Turtle()
cpu_paper_instance.hideturtle() # hiding the CPU instance since player isn't confirmed yet
scissors_instance = turtle.Turtle()
cpu_scissors_instance = turtle.Turtle()
cpu_scissors_instance.hideturtle()

 

screen.addshape(rock_image)
screen.addshape(paper_image)
screen.addshape(scissors_image) #addign the images as the shape for the relevant instances
screen.addshape(cpu_rock)
screen.addshape(cpu_paper)
screen.addshape(cpu_scissors)

# attach the rock_image to the rock_instance

rock_instance.shape(rock_image)
paper_instance.shape(paper_image)
scissors_instance.shape(scissors_image)
cpu_rock_instance.shape(cpu_rock) #adding each image to the instance

 

cpu_paper_instance.shape(cpu_paper) #the turtle is invisble but has the image of paper

cpu_paper_instance.penup()

 

cpu_scissors_instance.shape(cpu_scissors)

cpu_scissors_instance.hideturtle()

cpu_scissors_instance.penup() #pen up prevents line from forming upon movement

 

#defining the position of rock, paper, and scissors when running first.

rock_pos_x, rock_pos_y = -300, 0
paper_pos_x, paper_pos_y = 0,0
scissors_pos_x, scissors_pos_y = 300, 0
rock_instance.penup()
paper_instance.penup()
scissors_instance.penup()

 

#setting nthe positions of rock, paper, and scissors and moving them to the location when running.

rock_instance.setpos(rock_pos_x,rock_pos_y)
paper_instance.setpos(paper_pos_x, paper_pos_y)
scissors_instance.setpos(scissors_pos_x, scissors_pos_y)

 

#write text function - writes text in the window

def write_text(message, x, y):
    text = turtle.Turtle()
    text.color('green')
    text.penup()
    text.setpos(x,y)
    text.hideturtle()
    text.write(message, False, "center", ("Arial", 22, "bold"))
#opening text - welcome text

write_text("Click which option you want", 0, 150)

# remove the pen option from the rock_instance so it doesn't draw lines when moved

#defining when mouse collides with an image or not

def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True # if it's in this hitbox, it's true the click collided with one of the instances
    else:
        return False
 

# defining a function where if we click the image on the screen we send a message to terminal to correlate.

def mouse_pos(x, y):

    #when the mouse collides on rock

    if collide(x,y,rock_instance,rock_w,rock_h): #if it collided with the rock hitbox

        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        # hiding the options the player didn't choose

        if cpuchoice == "paper":
            cpu_paper_instance.showturtle() #showing the CPU choice
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You lose ", 0, 0) # paper beats rock

        elif cpuchoice == "rock":

            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y) #moving the images so they don't overlap on each other
            write_text("You tie!", 0, 0) #rock ties with rock

        elif cpuchoice == "scissors":
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y) #moving the images so they don't overlap with each other
            write_text("You Win", 0, 0)
    #the following code has the same comments and logic as the previous section, so they're getting a little more sparse
    elif collide(x,y,paper_instance,paper_w,paper_h):

        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        paper_instance.setpos(rock_pos_x, rock_pos_y)

        #depending on the cpu choice, it shows the cpu turtle accordingly. 

        if cpuchoice == "paper":

            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You tied", 0, 0)

        elif cpuchoice == "rock":

            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You win", 0, 0)

        elif cpuchoice == "scissors":

            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You lose", 0, 0)

    elif collide(x,y,scissors_instance,scissors_w,scissors_h):

        paper_instance.hideturtle()
        rock_instance.hideturtle()
        scissors_instance.setpos(rock_pos_x, rock_pos_y)

        #depending on the cpu choice, it shows the cpu turtle accordingly. WIN/LOSE/TIE

        if cpuchoice == "paper":

            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You win", 0, 0)

        elif cpuchoice == "rock":

            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You lose", 0, 0)

        elif cpuchoice == "scissors":

            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("You tied", 0, 0)

    else:
        print("Choose something fool")

#screen module onclick - action that will be triggered when the user clicks on the mouse

screen.onclick(mouse_pos)

turtle.done() #gives time for the program to finish, else the graphics shut down immediately upon finishing this program