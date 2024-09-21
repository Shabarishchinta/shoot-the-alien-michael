import pgzrun
from random import randint
title="Alien Game"

Width=500
Height=500
message=" "
Alien=Actor("alien")

def draw():
    screen.fill(color=(255,255,255))
    Alien.draw()
    screen.draw.text(message,center=(400,20), fontsize=30)
def alienplace():
    Alien.x=randint(50,Width-50)
    Alien.y=randint(50,Width-50)
def  on_mouse_down(pos):
    global message
    if Alien.collidepoint(pos):
        message="good shot"
        alienplace()
    else:
        message="you missed"
alienplace()
pgzrun.go()