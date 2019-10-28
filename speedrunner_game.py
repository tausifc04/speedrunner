# Speed Runner
# By: Tausif Chowdhury & Danell Cespedes
# https://github.com/tausifc04/speedrunner

# import dependencies
import subprocess
import sys
import importlib.util
import os
from time import sleep
from turtle import Turtle, Screen
from random import randint, choice

# function for clearing Command Line Interface
def clearCLI():
    subprocess.call("cls" if sys.platform == "win32" else "clear")

clearCLI()

# check if module wget is installed and import, otherwise install
if importlib.util.find_spec("wget") is None:
    print("wget not found, installing...")
    subprocess.call([sys.executable, "-m", "pip", "install", "wget"])
    import wget
    sleep(1)
else: import wget

# check if speedrunner_lb.py is present and import, otherwise download
if os.path.isfile("speedrunner_lb.py") == False:
    print("speedrunner_lb module not found, downloading...")
    wget.download("https://raw.githubusercontent.com/tausifc04/speedrunner/master/speedrunner_lb.py")
    import speedrunner_lb as lb
    sleep(1)
else:
    import speedrunner_lb as lb

clearCLI()

# player variables
name = input("Enter your name: ") # player inputs their name for leaderboard
score = 0 # initialize score variable

# leaderboard variables
lb_file_name = "speedrunner_leaderboard.txt" # file name of text file containing leaderboard data
leader_names_list = [] # list for containing names of players on leaderboard
leader_scores_list = [] # list for containing scores of players on leaderboard

# Python Turtle Graphics Window configuration
wn = Screen() # initialize screen
wn.title("Speed Runner - By: Tausif Chowdhury & Danell Cespedes") # title of Python Turtle Graphics window
wn.setup(width = 1200, height = 400) # dimensions of Python Turtle Graphics window (in pixels)

# tuple for font setup
font_setup = ("Arial", 20, "normal")

# defining class for Python turtle objects to derive from, allows for cleaner and simpler initialization of turtle objects
class trtl(Turtle):
    def __init__(self, size, color, speed):
        Turtle.__init__(self)
        self.pensize(size)
        self.color(color)
        self.speed(speed)

# initialize turtle writer for "Press F to start"
starter = trtl(1, "red", 0)
starter.hideturtle()
starter.penup()
starter.setx(-65)
starter.write("Press F to start", font = font_setup)

# main function containing the entirety of game
def main():
    global score

    wn.clear() # clear screen for game

    # initialize turtle for player-controlled runner
    runner = trtl(1, "black", "fastest")
    runner.hideturtle()
    runner.penup()
    runner.goto(-575, 0)
    runner.showturtle()

    # list containing colors for the walls/path to randomly choose from
    wall_color = ["red", "blue", "green", "pink", "purple", "orange", "yellow"]

    # initialize turtle drawers for walls/paths
    wall_drawer_1 = trtl(5, choice(wall_color), 0)
    wall_drawer_2 = trtl(5, choice(wall_color), 0)

    wall_drawer_1.hideturtle()
    wall_drawer_2.hideturtle()
    wall_drawer_1.penup()
    wall_drawer_2.penup()

    wall_drawer_1.goto(-650, 75)
    wall_drawer_2.goto(-650, -75)

    wall_drawer_1.pendown()
    wall_drawer_2.pendown()
    
    # initialize turtle writer for score at top-left of turtle window
    score_writer = trtl(1, "black", 0)
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.goto(-590, 175)
    score_writer.write("Score: " + str(score), font = font_setup)

    # function for drawing the walls/paths
    def path_drawer():
        bump_nums = randint(20,30)
        forward_1 = (1300 / bump_nums)
        wn.tracer(False) # disable tracer, allowing walls/paths to be drawn immediately, decreasing wait time
        for i in range(bump_nums):
            direction = [-90, 90]
            index = randint(0,1)
            pluss = randint(20, 50)
            if wall_drawer_1.ycor() >= 300:
                direction = [-90, 90]
                index = 0
                pluss = randint(20, 50)
                wall_drawer_1.forward(forward_1)
                wall_drawer_1.left(direction[index])
                wall_drawer_2.forward(forward_1)
                wall_drawer_2.left(direction[index])

                wall_drawer_1.forward(pluss)
                wall_drawer_1.right(direction)
                wall_drawer_2.forward(pluss)
                wall_drawer_2.right(direction)
                
                # if statement to prevent walls/paths from overlapping each others or going outside of window
                if wall_drawer_2.ycor() >= wall_drawer_1.ycor() or wall_drawer_1.ycor() <= wall_drawer_2.ycor() or wall_drawer_1.ycor() <= -195 or wall_drawer_1.ycor() >= 195 or wall_drawer_2.ycor() <= -195 or wall_drawer_2.ycor() >= 195:
                    wall_drawer_1.clear()
                    wall_drawer_2.clear()
                    wall_drawer_1.penup()
                    wall_drawer_1.goto(-600, 50)
                    wall_drawer_1.pendown()
                    wall_drawer_2.penup()
                    wall_drawer_2.goto(-600, -50)
                    wall_drawer_2.pendown()
                    path_drawer()

                # if statement to prevent walls/paths from continuing outside of window
                if wall_drawer_1.xcor() >= 590 and wall_drawer_2.xcor() >= 590: break
                
            elif wall_drawer_2.ycor() <= -300:
                direction = [-90, 90]
                index = 1
                pluss = randint(20, 50)
                wall_drawer_1.forward(forward_1)
                wall_drawer_1.left(direction[index])
                wall_drawer_2.forward(forward_1)
                wall_drawer_2.left(direction[index])
                
                wall_drawer_1.forward(pluss)
                wall_drawer_1.right(direction[index])
                wall_drawer_2.forward(pluss)
                wall_drawer_2.right(direction[index])
                
            wall_drawer_1.forward(forward_1)
            wall_drawer_1.left(direction[index])
            wall_drawer_2.forward(forward_1)
            wall_drawer_2.left(direction[index])
            
            wall_drawer_1.forward(pluss)
            wall_drawer_1.right(direction[index])
            wall_drawer_2.forward(pluss)
            wall_drawer_2.right(direction[index])
            
            # if statement to prevent walls/paths from overlapping each others or going outside of window
            if wall_drawer_2.ycor() >= wall_drawer_1.ycor() or wall_drawer_1.ycor() <= wall_drawer_2.ycor() or wall_drawer_1.ycor() <= -195 or wall_drawer_1.ycor() >= 195 or wall_drawer_2.ycor() <= -195 or wall_drawer_2.ycor() >= 195:
                wall_drawer_1.clear()
                wall_drawer_2.clear()
                wall_drawer_1.penup()
                wall_drawer_1.goto(-600, 50)
                wall_drawer_1.pendown()
                wall_drawer_2.penup()
                wall_drawer_2.goto(-600, -50)
                wall_drawer_2.pendown()
                path_drawer()

            # if statement to prevent walls/paths from continuing outside of window
            if wall_drawer_1.xcor() >= 590 and wall_drawer_2.xcor() >= 590: break
        wn.tracer(True) # re-enable tracer for runner
    
    path_drawer() # call function to run it

    # define functions to change direction of runner
    def up():
        runner.setheading(90)
    def down():
        runner.setheading(270)
    def right():
        runner.setheading(0)
    
    # calling above functions to change direction of runner based on W, S, and D keys
    wn.onkeypress(up, "w")
    wn.onkeypress(down, "s")
    wn.onkeypress(right, "d")
    wn.listen()

    # while loop to continuously make runner move forward
    runspeed = 2
    run = True
    while run:
        runner.forward(runspeed)
        # start of collision detection code
        xc, yc = runner.pos() # x and y variables for coordinates of runner
        margin = 1
        items = wn.getcanvas().find_overlapping(xc + margin, -yc + margin, xc - margin, -yc - margin) # applies a rectangle around runner in order to detect collisions
        if len(items) > 1: # when runner collides, length of list items is greater than 1
            runner.speed(0) # stop runner from moving
            wn.onkeypress(None, "w") # disable w key for up
            wn.onkeypress(None, "s") # disable s key for down
            wn.onkeypress(None, "d") # disable d key for right
            runner.color("red") # change runner color to red
            # start of code: makes runner blink
            sleep(0.5)
            runner.hideturtle()
            sleep(0.5)
            runner.showturtle()
            sleep(0.5)
            runner.hideturtle()
            sleep(0.5)
            break # break out of while loop
            # end of code: makes runner blink
        # end of collision detection code
        
        # if statement to put player into next level when completed current level
        if runner.xcor() >= 595:
            score += 1 # increment score
            score_writer.clear() # clear turtle writer for score
            score_writer.write("Score: " + str(score), font = font_setup) # update turtle writer for score
            runner.goto(-575, 0) # place runner back to beginning
            # clear current level (walls/paths) and move turtle drawers for walls/paths back to start
            wall_drawer_1.clear()
            wall_drawer_2.clear()
            wall_drawer_1.penup()
            wall_drawer_1.goto(-600, 50)
            wall_drawer_1.pendown()
            wall_drawer_2.penup()
            wall_drawer_2.goto(-600, -50)
            wall_drawer_2.pendown()
            wall_drawer_1.color(choice(wall_color)) # randomize color for wall_drawer_1
            wall_drawer_2.color(choice(wall_color)) # randomize color for wall_drawer_2
            path_drawer() # call path_drawer function to create new walls/paths
            runspeed += 1 # increase speed of runner (increase difficulty)
    wn.clear() # clear screen
    def manage_lb():
        lb.load_lb(lb_file_name, leader_names_list, leader_scores_list) # load leaderboard module with corresponding variables as parameters
        if len(leader_scores_list) < 5 or score > leader_scores_list[4]: # check if leaderboard has less than 5 players or if score of current player is higher than any leaderboard holders
            lb.update_lb(lb_file_name, leader_names_list, leader_scores_list, name, score) # update leaderboard text file
            lb.draw_lb(leader_names_list, leader_scores_list, True, runner, score) # draw updated leaderboard
        else:
            lb.draw_lb(leader_names_list, leader_scores_list, False, runner, score) # draw leaderboard
    if os.path.isfile(lb_file_name) == False: # if leaderboard text file is not found or does not exist
        lb_file = open(lb_file_name, "w") # create new leaderboard text file
        lb_file.close() # close new leardboard text file
        manage_lb() # call manage_lb function
    else: # if leaderboard text file does exist
        manage_lb() # call manage_lb function

wn.onkey(main, "f") # call main function when f key is pressed
wn.listen() # listen for key presses

wn.mainloop() # loop program to prevent it from ending without user intervention
