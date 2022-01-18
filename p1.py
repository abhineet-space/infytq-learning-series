import turtle
wn = turtle.Screen()       
wn.setup(540,508)       

alex = turtle.Turtle()      
alex.shape("turtle")        
alex.color("red")          
i=1
symbol="hexagon"
if(symbol == "plus"):
    while(1): 
        alex.forward(200)
        alex.backward(400)
        alex.forward(200)
        alex.right(90)
        alex.forward(200)
        alex.backward(400)
        alex.forward(200)

if(symbol == 'triangle'):
    while(1):
        alex.forward(200)
        alex.left(120)
        alex.forward(200)
        alex.left(120)
        alex.forward(200)
        alex.left(120)

if(symbol == "hexagon"):
    while(1):
        alex.forward(50)
        alex.left(60)
   
