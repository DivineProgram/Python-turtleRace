
import turtle
from random import *
import time

def pause(t):
    time.sleep(t)

typer = turtle.Turtle()
typer.hideturtle()
typer.color("white")
typer.speed(0)
typer.penup()
def gPrint(msg,size,locX,locY):
    typer.goto(locX-(size*0.5),locY-(size*0.85))
    typer.write(msg,False,"center",("Ariel",size,"bold"))
def gClear():
    typer.clear()

wn = turtle.Screen()
wn = turtle.bgcolor("black")
wn = turtle.colormode(255)

colors = ["red","orange","yellow","green","aqua","blue","purple","pink"]
turtles = [turtle.Turtle() for i in range(8)]

for i in range(len(turtles)):
    turtles[i].penup()
    turtles[i].turtlesize(0.75)
    
    if colors[i] == "red":
        turtles[i].color(255,0,0)
    elif colors[i] == "orange":
        turtles[i].color(255,111,0)
    elif colors[i] == "yellow":
        turtles[i].color(255,255,0)
    elif colors[i] == "green":
        turtles[i].color(0,255,17)
    elif colors[i] == "aqua":
        turtles[i].color(0,209,255)
    elif colors[i] == "blue":
        turtles[i].color(0,100,255)
    elif colors[i] == "purple":
        turtles[i].color(191,24,255)
    elif colors[i] == "pink":
        turtles[i].color(255,138,200)
        
    turtles[i].shape("turtle")
    turtles[i].goto(-300,(175-50*i))
    turtles[i].speed(0)
    turtles[i].pendown()
    gPrint(i+1,20,-330,(175-50*i))
    
finishline = turtle.Turtle()
finishline = turtle.hideturtle()
finishline = turtle.goto(300,-300)
finishline = turtle.color("white")
finishline = turtle.goto(300,300)

gPrint("Starting...",24,0,0)
pause(5)
gClear()
gPrint("3",20,0,0)
pause(1)
gClear()
gPrint("2",24,0,0)
pause(1)
gClear()
gPrint("1",28,0,0)
pause(1)
gClear()
gPrint("GO!",32,0,0)

racing = True
while racing == True:
    for i in range(len(turtles)):
        movef = randrange(0,750) / 100
        turtles[i].forward(movef)
        if turtles[i].xcor() >= 282:
            racing = False
            gClear()
            winner = i
            if colors[i] == "red":
                gPrint("Red won!",32,0,0)
            elif colors[i] == "orange":
                gPrint("Orange won!",32,0,0)
            elif colors[i] == "yellow":
                gPrint("Yellow won!",32,0,0)
            elif colors[i] == "green":
                gPrint("Green won!",32,0,0)
            elif colors[i] == "aqua":
                gPrint("Aqua won!",32,0,0)
            elif colors[i] == "blue":
                gPrint("Blue won!",32,0,0)
            elif colors[i] == "purple":
                gPrint("Purple won!",32,0,0)
            elif colors[i] == "pink":
                gPrint("Pink won!",32,0,0)
            else:
                gPrint("What???",32,0,0)
            pass
while True:
    turtles[winner].left(5)
