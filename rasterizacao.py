# -*- coding: utf-8 -*-
import turtle as tt
import math

def analitico(Xorig, Yorig, Xdest, Ydest): #mudar os print para a funcao set_pixel()
	if (Xorig == Xdest):
		if (Yorig < Ydest):
			for Y in range(Yorig, Ydest+1):
				set_pixel(Xdest, Y)
		else:
			for Y in range(Yorig, Ydest-1, -1):
				set_pixel(Xdest, Y)
	else:
		m = (Ydest-Yorig)/(Xdest-Xorig)
		b = Ydest-m*Xdest
		if (Xorig < Xdest):
			for X in range(Xorig, Xdest+1):
				Y = m*X+b
				set_pixel(X, Y)
		else:
			for X in range(Xorig, Xdest-1, -1):
				Y = m*X+b
				set_pixel(X, Y)

def dda(Xorig, Yorig, Xdest, Ydest):
	dx = Xdest - Xorig
	dy = Ydest - Yorig

	if(abs(dx)>abs(dy)):
		step = abs(dx)
	else:
		step = abs(dy)
	X_inc = 0 if (step == 0) else dx / float(step)
	Y_inc = 0 if (step == 0) else dy / float(step)
	X = Xorig
	Y = Yorig
	set_pixel(round(X),round(Y))
	for K in range(step):
		X= X+X_inc
		Y= Y+Y_inc
		set_pixel(round(X),round(Y))
def bresenham(Xorig, Yorig, Xdest, Ydest):
	if (Xorig > Xdest):
		return bresenham (Xdest, Ydest, Xorig, Yorig)
	a = Ydest - Yorig
	b = Xdest - Xorig
	x = Xorig
	y = Yorig
	inc = 1
	if (a < 0):
		a = abs(a)
		inc = -1
	if (abs(b) >= abs(a)):
		v = 2*a-b
		while (x <= Xdest):
			set_pixel(x, y)
			x = x+1
			if(v <= 0):
				v = v+2*a
			else:
				v = v+2*(a-b)
				y = y+inc
	else:
		v = 2*b-a
		while (x <= Xdest and y != Ydest):
			set_pixel(x, y)
			y = y+inc
			if (v <= 0):
				v = v+2*b
			else:
				v = v+2*(b-a)
				x = x+1

def circuferencia (Xcentro, Ycentro, Raio):
	if (Raio >= 9):
		tt.speed(5)
	x = Xcentro
	y = Raio + Ycentro
	d = 1 - Raio
	addPixelCicle(x, y, Xcentro, Ycentro)
	while(y-Ycentro > x-Xcentro):
		if(d<0):
			d = d + 2 *(x - Xcentro)+3
		else:
			d = d + 2 *((x-Xcentro) - (y - Ycentro))+5
			y=y-1
		x=x+1
		addPixelCicle(x, y, Xcentro, Ycentro)
def addPixelCicle (X, Y, Xcentro, Ycentro): #repete nos oito octante
	set_pixel(X,Y)
	set_pixel(X, 2*Ycentro-Y)
	set_pixel(2*Xcentro-X, Y)
	set_pixel(2*Xcentro-X, 2*Ycentro-Y)
	if(abs(Xcentro) > abs(Ycentro)):
		inc = Xcentro-Ycentro
		set_pixel(Y+inc, X-inc)
		set_pixel(2*Ycentro-Y+inc, X-inc)
		set_pixel(Y+inc, 2*Xcentro-X-inc)
		set_pixel(2*Ycentro+inc, 2*Xcentro-X-inc)
	else:
		inc = Xcentro - Ycentro
		set_pixel(Y-inc, X+inc)
		set_pixel(2*Ycentro-Y-inc, X+inc)
		set_pixel(Y-inc, 2*Xcentro-X+inc)
		set_pixel(2*Ycentro-Y-inc, 2*Xcentro-X+inc)

def elipse_trig(Xcentro, Ycentro, eixoX, eixoY):
	x = Xcentro
	y = eixoY+Ycentro
	ang = math.pi/2
	if (eixoX > eixoY):
		inc = ang-math.acos(1/float(eixoX))
	else:
		inc = ang-math.acos(1/float(eixoY))
	addPixelElipse(x, y, Xcentro, Ycentro)
	while (ang > 0):
		ang = ang-inc
		x = round(eixoX*math.cos(ang)+Xcentro)
		y = round(eixoY*math.sin(ang)+Ycentro)
		addPixelElipse(x, y, Xcentro, Ycentro)

def addPixelElipse(x, y, Xcentro, Ycentro):
	set_pixel(x, y)
	set_pixel(x, 2*Ycentro-y)
	set_pixel(2*Xcentro-x, y)
	set_pixel(2*Xcentro-x, 2*Ycentro-y)

def set_pixel(X,Y):
	print("Ativa pixel X: "+str(X)+" Y:"+str(Y))
	tt.goto(X*20, Y*20)
	tt.stamp()

def inicializaTT():
	tt.shape("square")
	tt.turtlesize(1)
	tt.penup()

def finalizaTT():
	tt.exitonclick()

def resetTT():
	tt.reset()