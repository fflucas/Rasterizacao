# -*- coding: utf-8 -*-
import Tkinter as tk
from Tkinter import *
import rasterizacao as rast
import os

class GUI_main(object):
	def __init__(self, master=None):
		#Define formato fonte
		self.fontePadrao = ("Arial", "11")
		#Define estruturas
		self.primeiroContainer = Frame(master)
		self.primeiroContainer.pack()

		self.segundoContainer = Frame(master)
		self.segundoContainer["padx"] = 30
		self.segundoContainer["pady"] = 18
		self.segundoContainer.pack()

		#Define titulo da janela
		self.titulo = Label(self.primeiroContainer, text="Rasterização")
		self.titulo["font"] = ("Arial", "12", "bold")
		self.titulo.pack()
		#Escrita "Escolha uma opção" 
		self.escrita = Label(self.segundoContainer,text="Escolha uma opção", font=self.fontePadrao)
		self.escrita.pack()
		self.escrita["height"] = 2
		#Define buttons para opçoes
		self.analitico = Button(self.segundoContainer)
		self.analitico["text"] = "Reta Método Analítico"
		self.analitico["font"] = ("Calibri", "9")
		self.analitico["width"] = 18
		self.analitico["command"] = lambda: self.create_window(1)
		self.analitico.pack()

		self.dda = Button(self.segundoContainer)
		self.dda["text"] = "Reta Método DDA"
		self.dda["font"] = ("Calibri", "9")
		self.dda["width"] = 18
		self.dda["command"] = lambda: self.create_window(2)
		self.dda.pack()

		self.bresenham = Button(self.segundoContainer)
		self.bresenham["text"] = "Reta Método Bresenham"
		self.bresenham["font"] = ("Calibri", "9")
		self.bresenham["width"] = 18
		self.bresenham["command"] = lambda: self.create_window(3)
		self.bresenham.pack()

		self.circulo = Button(self.segundoContainer)
		self.circulo["text"] = "Circulo Método Bresenham"
		self.circulo["font"] = ("Calibri", "9")
		self.circulo["width"] = 18
		self.circulo["command"] = lambda: self.create_window(4)
		self.circulo.pack()

		self.elipse = Button(self.segundoContainer)
		self.elipse["text"] = "Elípse Mét. Trigonométrico"
		self.elipse["font"] = ("Calibri", "9")
		self.elipse["width"] = 18
		self.elipse["command"] = lambda: self.create_window(5)
		self.elipse.pack()

	#Cria nova janela
	def create_window(self, id):
		window = tk.Toplevel(root)
		GUI_sec(id, window)

#Monta a segunda janela
class GUI_sec(Frame):
	def __init__(self, id, master=None):
		self.fontePadrao = ("Arial", "11")
		#Estrutura
		self.primeiroContainer = Frame(master)
		self.primeiroContainer.pack()
		self.primeiroContainer["padx"] = 30
		self.primeiroContainer["pady"] = 18
		if (id == 1):
			self.titulo = Label(self.primeiroContainer, text="Reta Método Analítico")
		elif(id == 2):
			self.titulo = Label(self.primeiroContainer, text="Reta Método DDA")
		elif(id == 3):
			self.titulo = Label(self.primeiroContainer, text="Reta Método Bresenham")
		elif(id == 4):
			self.titulo = Label(self.primeiroContainer, text="Circulo Método Bresenham")
		elif(id == 5):
			self.titulo = Label(self.primeiroContainer, text="Elípse Método Trigonométrico")
		self.titulo["font"] = ("Arial", "11", "bold")
		self.titulo.pack()
		
		self.segundoContainer = Frame(master)
		self.segundoContainer.pack()

		self.terceiroContainer = Frame(master)
		self.terceiroContainer.pack()

		self.quartoContainer = Frame(master)
		self.quartoContainer.pack()

		self.quintoContainer = Frame(master)
		self.quintoContainer.pack()

		self.sextoContainer = Frame(master)
		self.sextoContainer["padx"] = 30
		self.sextoContainer["pady"] = 18
		self.sextoContainer.pack()
		if (id == 1 or id == 2 or id == 3):
			#Entradas de valores
			self.Xorig = Entry(self.segundoContainer)
			self.Xorig["width"] = 3
			self.Xorig["font"] = self.fontePadrao
			self.Xorig.pack(side=LEFT)
			self.Yorig = Entry(self.segundoContainer)
			self.Yorig["width"] = 3
			self.Yorig["font"] = self.fontePadrao
			self.Yorig.pack(side=LEFT)

			self.nomeXorig = Label(self.terceiroContainer,text="Xorig", font=self.fontePadrao)
			self.nomeXorig.pack(side=LEFT)
			self.nomeYorig = Label(self.terceiroContainer,text="Yorig", font=self.fontePadrao)
			self.nomeYorig.pack(side=LEFT)

			self.Xdest = Entry(self.quartoContainer, text="X")
			self.Xdest["width"] = 3
			self.Xdest["font"] = self.fontePadrao
			self.Xdest.pack(side=LEFT)
			self.Ydest = Entry(self.quartoContainer)
			self.Ydest["width"] = 3
			self.Ydest["font"] = self.fontePadrao
			self.Ydest.pack(side=LEFT)
			
			self.nomeXdest = Label(self.quintoContainer,text="Xdest", font=self.fontePadrao)
			self.nomeXdest.pack(side=LEFT)
			self.nomeYdest = Label(self.quintoContainer,text="Ydest", font=self.fontePadrao)
			self.nomeYdest.pack(side=LEFT)
		elif (id == 4):
			self.Xcent = Entry(self.segundoContainer)
			self.Xcent["width"] = 3
			self.Xcent["font"] = self.fontePadrao
			self.Xcent.pack(side=LEFT)
			self.Ycent = Entry(self.segundoContainer)
			self.Ycent["width"] = 3
			self.Ycent["font"] = self.fontePadrao
			self.Ycent.pack(side=LEFT)

			self.nomeXcent = Label(self.terceiroContainer,text="Xcent", font=self.fontePadrao)
			self.nomeXcent.pack(side=LEFT)
			self.nomeYcent = Label(self.terceiroContainer,text="Ycent", font=self.fontePadrao)
			self.nomeYcent.pack(side=LEFT)

			self.raio = Entry(self.quartoContainer, text="X")
			self.raio["width"] = 3
			self.raio["font"] = self.fontePadrao
			self.raio.pack(side=LEFT)
			
			self.nomeraio = Label(self.quintoContainer,text="Raio", font=self.fontePadrao)
			self.nomeraio.pack(side=LEFT)
		else:
			self.XcentE = Entry(self.segundoContainer)
			self.XcentE["width"] = 3
			self.XcentE["font"] = self.fontePadrao
			self.XcentE.pack(side=LEFT)
			self.YcentE = Entry(self.segundoContainer)
			self.YcentE["width"] = 3
			self.YcentE["font"] = self.fontePadrao
			self.YcentE.pack(side=LEFT)

			self.nomeXcentE = Label(self.terceiroContainer,text="Xcent", font=self.fontePadrao)
			self.nomeXcentE.pack(side=LEFT)
			self.nomeYcentE = Label(self.terceiroContainer,text="Ycent", font=self.fontePadrao)
			self.nomeYcentE.pack(side=LEFT)

			self.eixoX = Entry(self.quartoContainer, text="X")
			self.eixoX["width"] = 3
			self.eixoX["font"] = self.fontePadrao
			self.eixoX.pack(side=LEFT)
			self.eixoY = Entry(self.quartoContainer)
			self.eixoY["width"] = 3
			self.eixoY["font"] = self.fontePadrao
			self.eixoY.pack(side=LEFT)
			
			self.nomeeixoX = Label(self.quintoContainer,text="EixoX", font=self.fontePadrao)
			self.nomeeixoX.pack(side=LEFT)
			self.nomeeixoY = Label(self.quintoContainer,text="EixoY", font=self.fontePadrao)
			self.nomeeixoY.pack(side=LEFT)

		#Botão Enviar
		self.enviar = Button (self.sextoContainer)
		self.enviar["text"] = "Enviar"
		self.enviar["font"] = ("Calibri", "9")
		self.enviar["width"] = 10
		self.enviar["height"] = 1
		self.enviar["command"] = lambda: self.control(id)
		self.enviar.pack()
		#Reseta o Turtle
		rast.resetTT()

	#Controle para determinar o que executar
	def control(self, id):
		#Incializa Turtle
		rast.inicializaTT()
		os.system("clear") #limpa console
		if (id == 1 or id == 2 or id == 3):
			Xori = int(self.Xorig.get())
			Yori = int(self.Yorig.get())
			Xdes = int(self.Xdest.get())
			Ydes = int(self.Ydest.get())
		if (id == 1):
			rast.analitico(Xori, Yori, Xdes, Ydes)
		elif(id == 2):
			rast.dda(Xori, Yori, Xdes, Ydes)
		elif(id == 3):
			rast.bresenham(Xori, Yori, Xdes, Ydes)
		elif(id == 4):
			Xcen = int(self.Xcent.get())
			Ycen = int(self.Ycent.get())
			Raio = int(self.raio.get())
			rast.circuferencia(Xcen, Ycen, Raio)
		elif(id == 5):
			XcenE = int(self.XcentE.get())
			YcenE = int(self.YcentE.get())
			eixX = int(self.eixoX.get())
			eixY = int(self.eixoY.get())
			rast.elipse_trig(XcenE, YcenE, eixX, eixY)
		#Finaliza Turtle
		rast.finalizaTT()
		
#Main
root = tk.Tk()
GUI_main(root)
root.mainloop()