import turtle
import math

def draw_tree(t, branch_len, level):
    if level == 0:
        return

    # main branch
    print(level)
    t.forward(branch_len)

    # save the current state
    position = t.position()
    heading = t.heading()

    # left branch
    t.left(45)
    draw_tree(t, branch_len * math.sqrt(2) / 2, level - 1)

    # restore state
    t.setposition(position)
    t.setheading(heading)

    # right branch
    t.right(45)
    draw_tree(t, branch_len * math.sqrt(2) / 2, level - 1)

    # return
    t.setposition(position)
    t.setheading(heading)

# turtle window
window = turtle.Screen()
window.bgcolor("white")
window.title("Pythagoras Tree Fractal")

# setup turtle
t = turtle.Turtle()
t.color("green")
t.speed(0)
t.pensize(2)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

depth = int(input("Enter the recursion depth: "))

draw_tree(t, 100, depth)

turtle.done()