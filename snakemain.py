from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square") # 20x20  
    new_segment.color("white") # 
    new_segment.penup() #  don't draw lines
    new_segment.goto(position) #   move to position
    segments.append(new_segment) #  add to list

game_is_on = True
while game_is_on:
    screen.update() # update the screen with the new positions of the segments i.e. the snake body so x and y coordinates
    #  
    time.sleep(0.1)

    for seg_num in range( len(segments)-1, 0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y) 
    segments[0].forward(20)
    
     
    










screen.exitonclick()
