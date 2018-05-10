
import turtle

def draw_square(who):
    for i in range(0,4):
        who.forward(100)
        who.right(90)

def draw_trangle(name):
    for i in range(0,3):
        name.backward(100)
        name.left(120)

def draw_three():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)

    for i in range(0,120):
        draw_square(brad)
        brad.right(3)

    windows.exitonclick

draw_three
    
    
    
    
