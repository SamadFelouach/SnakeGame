# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:43:06 2020

@author: Avicii
"""
import turtle
import time
delay =0.1
#set up the screen
window =turtle.Screen()
window.title("my amazing game by @Avicci")
window.bgcolor("green")
window.setup(width=600 , height =500)
window.tracer(0)#turn off the screen updates 




#snake head 
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction ="stop"


#functions
def go_up() :
    head.direction ="up"
def go_down():
    head.direction ="down"

def go_left():
    head.direction ="left"
    
def go_right():
    head.direction ="right"

def move():
    
    if head.direction=="up":
       y = head.ycor()
       head.sety(y+20)
      
    if head.direction =="down":
       y = head.ycor()
       head.sety(y-20) 
       
    if head.direction =="left":
       x = head.xcor()
       head.setx(x-20)
       
    if head.direction =="right":
       x = head.xcor()
       head.setx(x+20)
       
       
  #keyboard
  window.listen()
  window.onkeypress(go_up ,"u")
  window.onkeypress(go_down,"d")
  window.onkeypress(go_left,"l")
  window.onkeypress(go_right,"r")


#loop
  while True:
      window.update()
      move()
      time.sleep(delay)
window.mainloop()