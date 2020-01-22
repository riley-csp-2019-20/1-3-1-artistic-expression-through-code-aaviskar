#imports
import turtle as trtl 
import random 

#creating turtles
player = trtl.Turtle(shape= "turtle", )     #turtle for the player
player.up()
player.sety(-300)
player.setheading(90)
#turtles for cars that cross the road
car1 = trtl.Turtle(shape= "circle")
car2= trtl.Turtle()
car1.turtlesize(10)
car2.turtlesize(10)
car1.ht()
car2.ht()

#turtle that draws stoplight
stoplight= trtl.Turtle()
stoplight.up()
stoplight.ht()
stoplight.speed(0)
stoplight.goto(-475,300)
stoplight.down()
stoplight.pensize(5)
stoplight.fillcolor("gray")
stoplight.begin_fill()
stoplight.forward(300)
stoplight.setheading(90)
stoplight.forward(100)
stoplight.setheading(180)
stoplight.forward(300)
stoplight.setheading(270)
stoplight.forward(100)
stoplight.end_fill()
stoplight.up()
stoplight.goto(-375, 350)
stoplight.down()
stoplight.circle(45)

#lists and variables for the game
colors = ["red", "yellow", "green"]
road= "crookedroad.png"
    # stoplight= "stoplight.png"

#screen 
wn= trtl.Screen()
wn.bgpic(road)
    # trtl.register_shape("stoplight.gif")

#random choice of color for the game
game_color = "red"  #defines the color for the stoplight

light_color= random.choice(colors) # starts the stoplight with a random color

#functions and loops

#functions for player movement
def player_forward():
    #if (light_color == game_color):
    player.setheading(90)
    player.forward(10)
    # failure()
    change_color()
    check_red()
def player_down():
    #if (light_color == game_color):
    player.setheading(270)
    player.forward(10)
    # failure()
    change_color()
    check_red()
def player_right():
    #if (light_color == game_color):
    player.setheading(0)
    player.forward(10)
    # failure()
    change_color()
    check_red()
def player_left():
    #if (light_color == game_color):
    player.setheading(180)
    player.forward(10)     
    # failure()
    change_color()
    check_red()
    
#function that checks if color is red
# def failure():
#     light_color= random.choice(colors)
#     if (light_color == game_color):
#         player.goto(0,-300)

#functions that change color of stoplight
def draw_stoplight():
    global light_color
    light_color= random.choice(colors)
    stoplight.up()
    stoplight.goto(-375, 350)
    stoplight.down()
    stoplight.fillcolor(light_color)
    stoplight.begin_fill()
    stoplight.circle(45)
    stoplight.end_fill()   
draw_stoplight()

count = 1
def change_color():
    global count
    if count % 5 == 0:
        draw_stoplight()
    count -=1

red_light= 0
#checks if the stoplight is red and moves the cars
def check_red():
    if game_color == light_color:
        red_light == 1
    else:
        red_light == 0
    print(red_light)
if  red_light == 1:
    car1.goto(100,100) 
    car1.st()

#keybindings
wn.onkeypress(player_forward, "Up")
wn.onkeypress(player_down,"Down")
wn.onkeypress(player_right,"Right")
wn.onkeypress(player_left,"Left")

    # wn.onkeypress(change_color, "space")

#listen and mainloop
wn.listen()
wn.mainloop()