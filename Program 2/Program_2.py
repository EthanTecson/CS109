#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 22:45:15 2022

@author: ethantecson
"""

""" This program is the bare bones of a "turtle graphic" program.

    Author/copyright: Duncan A. Buell.  All rights reserved.
    Used with permission and modified by: Jane Random Hacker
    Date: 29 August 2022
"""
import sys
import turtle

#123456789 123456789 123456789 123456789 123456789 123456789 123456789

######################################################################
george = turtle.Turtle()
print(george.position())
george.pencolor('green')
george.hideturtle()
george.speed(6)
#Loop creates hexagon
for count in range(6):
    george.forward(100.0)
    george.right(60.0)
#Makes fill color blue and creates two triangles in hexagon
george.fillcolor('blue')
george.begin_fill()
george.right(60.0)
george.forward(200.0)
george.right(120.0)
george.forward(100.0)
george.right(120.0)
george.forward(200.0)
george.end_fill()               
screen = george.getscreen()
screen.exitonclick()


        
