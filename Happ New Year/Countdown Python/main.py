from turtle import *
import pygame
bgcolor("#222"), setup(600,400)
hideturtle(), tracer(0), penup()
def Text(txt, col:tuple, x, y, shader:bool, size):
    font = ("Consolas",size,"bold")
    for i in range(shader + 1):
        goto(-2*i+x, 4*i+y)
        color(col) if i|(not shader) else color(0,0,0)
        write (txt, font=font, align="center" )

pygame.init()
pygame.mixer.init()
file_path = 'E:\Project Visual Studio Code\HTML,CSS,JS\Happ New Year\Countdown Python\HAPPY.mp3' # If you have a fireworks sound file, put it in ' '
if file_path.strip() == '':
	pass
else:	
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

from math import sin, cos
from datetime import datetime
def _Oneo_Kuu():
    update(), clear()
    c = datetime(2024,2,10) - datetime.today() # Edit the number of years you want to countdown to here
    TITLE = ["day", "hour", "minute", "second"]
    COUNTDOWN = [ c.days, c.seconds//3600,
        (c.seconds%3600)//60, c.seconds%60]
    if not any(COUNTDOWN) or COUNTDOWN[0]<0:
        COUNTDOWN = [2,0,2,4] # Fix this line again when the counting appears the new year
        TITLE = ["HAPPY", "NEW", "YEAR", "!"]
    Text ("COUNTDOWN TO LUNAR NEW YEAR 2024", (0,0,0), 0, 80, False, 25) # Fix the new year display line
    for i in range(len(COUNTDOWN)) :
        color = (cos(i-2)/2+.5,.5,cos(i+2)/2+.5)
        Text (COUNTDOWN[i], color, -150+120*i-30, -25, True, 54)
        Text (TITLE[i], color, -150+120*i-30, -50, False,18)
    ontimer(_Oneo_Kuu, 200)
_Oneo_Kuu()
mainloop( )