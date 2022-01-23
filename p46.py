from operator import le
import turtle
wn = turtle.Screen()
wn.setup(500,500)
turtle = turtle.Turtle()
turtle.speed("fastest")

def draw_square(length,angle):
    if length == 1:
        return
    draw_square(length-1,angle)
    for b in range(0,4):
        turtle.forward(100+length)
        turtle.right(angle+b)
    return

'''
step = 100
def draw_square(length,angle):
    for i in range (0,step):
        for b in range (0,4):
            turtle.forward(length+i)
            turtle.right(angle+b)
'''
draw_square(100,90)
                    

'''import turtle
wn = turtle.Screen()
wn.setup(500,500)
turtle = turtle.Turtle()
turtle.speed("fastest")

def draw_square(length,angle):
    if length == 1:
        return
    for b in range(0,4):
        turtle.forward(100)
        turtle.right(angle+b)
    return draw_square(length-1,angle)

draw_square(100,90)
                        '''