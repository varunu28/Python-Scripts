import turtle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    #Initialize the drawing canvas
    window=turtle.Screen()
    window.bgcolor("red")

    #Initialize the square turtle
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    #Initialize the circle turtle4
    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #4angie.circle(100)

    window.exitonclick()

draw_art()
