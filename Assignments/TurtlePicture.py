'''
Created on Sep 15, 2017

@author: leahschwartz
'''
import turtle #lets us us turtles library
import random
from turtle import Screen
wn = turtle.Screen() #creates graphic window
wn.bgcolor("lightblue") #sets background color


def rectangle(length,height,color,sheldon):
    #This function creates a rectangle with adjustable height, length, and color
    sheldon.pendown()
    sheldon.fillcolor(color) #allows rectangle to be filled with color
    sheldon.begin_fill()
    sheldon.backward(-length)
    sheldon.right(90)
    sheldon.forward(height)
    sheldon.right(90)
    sheldon.backward(-length)
    sheldon.right(90)
    sheldon.backward(-height)
    sheldon.right(90)
    sheldon.end_fill()
  
def triangle(length,color,sheldon):
    #This function creates a triangle with adjustable side length and color
    sheldon.pendown()
    sheldon.fillcolor(color) #allows triangle to be filled with color
    sheldon.begin_fill()
    sheldon.right(300)
    sheldon.forward(length)
    sheldon.right(120)
    sheldon.forward(length)
    sheldon.right(120)
    sheldon.forward(length)
    sheldon.right(180)
    sheldon.end_fill()
    
def flowerSquare(size,sheldon):
    # draw a flower made out of squares
    sheldon.pendown()
    for i in range(12):      # repeat twelve times
        #select random color
        number = random.randint(1,4)
        if number == 1:
            sheldon.fillcolor("red")
        if number == 2:
            sheldon.fillcolor("purple")
        if number == 3:
            sheldon.fillcolor("pink")
        if number == 4:
            sheldon.fillcolor("yellow")
        #draw square
        sheldon.begin_fill()
        sheldon.forward(size)
        sheldon.left(90)
        sheldon.forward(size)
        sheldon.left(90)
        sheldon.forward(size)
        sheldon.left(90)
        sheldon.forward(size)
        sheldon.left(90) 
        sheldon.end_fill()
        sheldon.left(30)

def cloud(sheldon): 
    #creates a cloud
    sheldon.pendown()
    sheldon.fillcolor("white") #fills with white
    for c in range(7): #draws seven circles of different sizes
        sheldon.begin_fill()
        number = random.randint(20,50)
        sheldon.circle(number)
        sheldon.end_fill()
        sheldon.penup()
        sheldon.forward(number-(number/2)) 
        sheldon.pendown()
 
def sun(sheldon): 
    #creates a hexagon sun 
    sheldon.pendown()
    for n in range(8):#repeats 8 times
        sheldon.forward(80)
        sheldon.right(180)
        sheldon.forward(40)
        sheldon.right(180)
        sheldon.right(45)
    sheldon.fillcolor("yellow") #makes inside of sun yellow
    sheldon.begin_fill()    
    for l in range(8):
        sheldon.forward(40)
        sheldon.right(45)
    sheldon.end_fill()

def makePerson(sheldon):
    #draws person with arms
    sheldon.pendown()
    sheldon.fillcolor("yellow") #makes face yellow
    sheldon.begin_fill()
    sheldon.circle(30) #draw head
    sheldon.end_fill()
    sheldon.penup()
    sheldon.left(90)
    sheldon.forward(30)
    sheldon.right(90)
    sheldon.forward(30)
    sheldon.pendown()
    sheldon.forward(155) #draw torso
    sheldon.right(180)
    sheldon.forward(100)
    sheldon.right(45) #draw right arm
    sheldon.forward(65)
    sheldon.right(180)
    sheldon.forward(65)
    sheldon.left(270)
    sheldon.forward(65) #draw left arm
                   
def buildHouse(sheldon):
    #This function creates a house with a roof, two windows, and a door
    rectangle(300,300,"blue",sheldon) #base of house
    triangle(300,"red",sheldon) #roof of house
    
    sheldon.penup()
    sheldon.forward(35)
    sheldon.right(90)
    sheldon.forward(60)
    sheldon.left(90)
    rectangle(75,75,"yellow",sheldon) #first window
    
    sheldon.penup()
    sheldon.right(90)
    sheldon.forward(75)
    sheldon.left(90)
    sheldon.forward(150)
    sheldon.left(90)
    rectangle(75,75,"yellow",sheldon) #second window
   
    sheldon.penup()
    sheldon.right(180)
    sheldon.forward(15)
    rectangle(150, 75, "lightgreen", sheldon) #door  
         
def buildGarden(sheldon):
    #builds garden with three flowers
    flowerSquare(25,sheldon)
    sheldon.penup()
    sheldon.right(90)
    sheldon.forward(100)
    flowerSquare(35, sheldon)
    sheldon.penup()
    #sheldon.right(90)
    sheldon.forward(100)
    flowerSquare(25, sheldon)       
                   
def draw(): 
    #draws whole picture
    sheldon = turtle.Turtle() #creates turtle sheldon
    
    buildHouse(sheldon)
    
    sheldon.penup()
    sheldon.right(90)
    sheldon.forward(400)
    sheldon.left(90)
    sheldon.forward(150)
    sheldon.right(180)
    sheldon.forward(20)
    
    buildGarden(sheldon)
    
    sheldon.penup()
    sheldon.left(90)
    sheldon.forward(500)
    sheldon.left(90)
    
    cloud(sheldon)
    
    sheldon.penup()
    sheldon.left(90)
    sheldon.forward(100)
    sheldon.right(90)
    
    cloud(sheldon)
    
    sheldon.penup()
    sheldon.right(90)
    sheldon.forward(100)
    
    sun(sheldon)
    
    sheldon.left(180)
    sheldon.penup()
    sheldon.forward(300)
    
    makePerson(sheldon)
   
    
if __name__ == '__main__':
    draw()  # main function to have a turtle draw a picture 
    wn.exitonclick()   # must be last line in file                              