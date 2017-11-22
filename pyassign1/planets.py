#!/usr/bin/env python3

"""planets.py: to descrlbe the orbit of some planets in the Solar System.

__author__ = "XiongJie"
__pkuid__  = "1700011827"
__email__  = "xiongjie1999@pku.edu.cn"
"""


import turtle
import math
wn = turtle.Screen()
wn.screensize(9600,7200)
turtle.hideturtle()
turtle.bgcolor("black")


def sun(t):
    """to draw the sun in the middle"""
    t.hideturtle()
    t.penup()
    t.goto(0,-10)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.speed(0)
    t.circle(10)
    t.end_fill()


def solarsystem(t, Me, Ve, Ea, Ma, Ju, Sa, a_one, e_one,
                a_two, e_two, a_thr, e_thr, a_fo, e_fo,
                a_fiv, e_fiv, a_six, e_six):
    """to describe the whole system"""
    sun(t)
    Me.hideturtle()
    Me.color("green")
    Me.shape("circle")
    Me.shapesize(0.25, 0.25)
    Me.penup()
    Me.goto(a_one+a_one*e_one, 0)
    Me.showturtle()
    Me.pendown()
    Ve.hideturtle()
    Ve.color("brown")
    Ve.shape("circle")
    Ve.shapesize(0.625, 0.625)
    Ve.penup()
    Ve.goto(-a_two+a_two*e_two, 0)
    Ve.showturtle()
    Ve.pendown()
    Ea.hideturtle()
    Ea.color("blue")
    Ea.shape("circle")
    Ea.shapesize(0.65, 0.65)
    Ea.penup()
    Ea.goto(a_thr+a_thr*e_thr, 0)
    Ea.showturtle()
    Ea.pendown()
    Ma.hideturtle()
    Ma.color("red")
    Ma.shape("circle")
    Ma.shapesize(0.35, 0.35)
    Ma.penup()
    Ma.goto(a_fo+a_fo*e_fo, 0)
    Ma.showturtle()
    Ma.pendown()
    Ju.hideturtle()
    Ju.color("yellow")
    Ju.shape("circle")
    Ve.shapesize(0.95, 0.95)
    Ju.penup()
    Ju.goto(a_fiv+a_fiv*e_fiv, 0)
    Ju.showturtle()
    Ju.pendown()
    Sa.hideturtle()
    Sa.color("purple")
    Sa.shape("circle")
    Ve.shapesize(0.85, 0.85)
    Sa.penup()
    Sa.goto(a_six+a_six*e_six, 0)
    Sa.showturtle()
    Sa.pendown()
    for i in range(5000):
        thita_one = (122.5*i/1800)*math.pi
        thita_two = (48*i/1800)*math.pi
        thita_thr = (29.5*i/1800)*math.pi
        thita_fo = (15.7*i/1800)*math.pi
        thita_fiv = (2.5*i/1800)*math.pi
        thita_six = (i/1800)*math.pi
        x_one = a_one*e_one+a_one*math.cos(thita_one)
        y_one = (a_one*math.sqrt(1-e_one**2))*math.sin(thita_one)
        Me.goto(x_one,y_one)
        x_two = a_two*e_two+a_two*math.cos(math.pi+thita_two)
        y_two = (a_two*math.sqrt(1-e_two**2))*math.sin(thita_two)
        Ve.goto(x_two,y_two)
        x_thr = a_thr*e_thr+a_thr*math.cos(thita_thr)
        y_thr = (a_thr*math.sqrt(1-e_thr**2))*math.sin(thita_thr)
        Ea.goto(x_thr,y_thr)
        x_fo = a_fo*e_fo+a_fo*math.cos(thita_fo)
        y_fo = (a_fo*math.sqrt(1-e_fo**2))*math.sin(thita_fo)
        Ma.goto(x_fo,y_fo)
        x_fiv = a_fiv*e_fiv+a_fiv*math.cos(thita_fiv)
        y_fiv = (a_fiv*math.sqrt(1-e_fiv**2))*math.sin(thita_fiv)
        Ju.goto(x_fiv,y_fiv)
        x_six = a_six*e_six+a_six*math.cos(thita_six)
        y_six = (a_six*math.sqrt(1-e_six**2))*math.sin(thita_six)
        Sa.goto(x_six,y_six)


def main():
    """main module"""
    t = turtle.Turtle()
    Me = turtle.Turtle()
    Ve = turtle.Turtle()
    Ea = turtle.Turtle()
    Ma = turtle.Turtle()
    Ju = turtle.Turtle()
    Sa = turtle.Turtle()
    solarsystem(t, Me, Ve, Ea, Ma, Ju, Sa, 25, 0.205,
                46.75, 0.007, 64.5, 0.017, 98.5, 0.093,
                336/2, 0.048, 618.75/2, 0.055)


if __name__ == "__main__":
    main()
