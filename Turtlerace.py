from turtle import Turtle
from random import randint

## FINISH LINE

fline=Turtle()
fline.penup()
fline.goto(160,200)
fline.pendown()
fline.goto(160,-150)
fline.write('Finish line')

### TURTLES 

kunal=Turtle()          # turtle object

kunal.color('red')
kunal.shape('turtle')       #attributes of object

kunal.penup()                   # before goto penup is needed so line is drawn while locating our turtle
kunal.goto(-160,120)            #centre of screen is 0,0
kunal.pendown()                 #after going pen down because now movements will be displayed or maybe not if we want
    

atharva=Turtle()          # turtle object

atharva.color('blue')
atharva.shape('turtle')

atharva.penup()
atharva.goto(-160,90)
atharva.pendown()


manas=Turtle()          # turtle object

manas.color('pink')
manas.shape('turtle')

manas.penup()
manas.goto(-160,60)
manas.pendown()


push=Turtle()          # turtle object

push.color('brown')
push.shape('turtle')

push.penup()
push.goto(-160,30)
push.pendown()


abhi=Turtle()          # turtle object

abhi.color('yellow')
abhi.shape('turtle')

abhi.penup()
abhi.goto(-160,0)
abhi.pendown()


for speed in range(60) :
    kunal.forward(randint(1,10))
    manas.forward(randint(1,10))
    atharva.forward(randint(1,10))
    push.forward(randint(1,10))
    abhi.forward(randint(1,10))
    

