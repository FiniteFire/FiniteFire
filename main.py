from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue", "purple", "yellow"]
lane_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=lane_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

number_winners = 0
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if number_winners == 0:
                winning_color_1 = turtle.pencolor()
                number_winners += 1
                # remove this winning turtle from the list
                all_turtles.remove(turtle)
            elif number_winners == 1:
                winning_color_2 = turtle.pencolor()
                number_winners  += 1
                
            if number_winners == 2:
                is_race_on = False

                if winning_color_1 == user_bet or winning_color_2 == user_bet:
                    print(f"You've won! The {winning_color_1} turtle and the {winning_color_2} turtle are the winners!")
                else:
                    print(f"You've lost! The {winning_color_1} turtle and the {winning_color_2} turtle are the winners!")


                
        rand_distance = random.randint(-20, 50)
        turtle.forward(rand_distance)

screen.exitonclick()
