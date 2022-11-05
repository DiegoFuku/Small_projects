

import random
import time
import os

def dibujo (jugada):
	if jugada == "Piedra":
		print("                 @@")
		print("                @@@")
	elif jugada == "Papel":
		print("                ===")
		print("                ===")

	elif jugada == "Tijeras":
		print("                |/")
		print("                OO")
		 
def comprobar_ganador(jugador,ordenador):
	''' Devuelve el ganador de la tirada entre el jugador humano y el ordenador'''
	
	if jugador == "Piedra":
		if ordenador == "piedra":
			ganador="Ninguno"
		elif ordenador== "Papel":
			ganador= "Ordenador"
		else:
			ganador="Humano"		
	elif jugador == "Papel":
		if ordenador == "Piedra":
			ganador = "Humano"
		elif ordenador == "Papel":
			ganador= "Ninguno"
		else:
			ganador= "Ordenador"
	elif jugador == "Tijeras":
		if ordenador == "Piedra":
			ganador = "Ordenador"
		elif ordenador == "Papel":
			ganador = "Humano"
		else:
			ganador = "Ninguno"
					
	return ganador
						

def movimiento_jugador():
	'''devuelve la jugada que hace el jugador humano'''
	
	opciones_humano = ["Piedra" , "Papel", "Tijeras"]
	jugada=""
	while jugada not in opciones_humano:
		jugada = input("          Haz tu jugada:   ").capitalize()	
	else:
		return jugada
					

def movimiento_ordenador_con_ia(jugadas_humano, ultimo_resultado):
	'''devuelve la jugada que hace el ordenador con IA'''
	
	if ultimo_resultado == 1:
		if jugadas_humano[-1] == "Piedra":
			jugada=random.choice(["Papel","Piedra"])
		elif jugadas_humano [-1] == "Papel":
			jugada=random.choice(["Tijeras", "Papel"])
		elif jugadas_humano[-1] == "Tijeras":
			jugada=random.choice(["Piedra","Tijeras"])
	elif ultimo_resultado == 0:
		if jugadas_humano[-1] == "Piedra":
			jugada=random.choice(["Tijeras","Piedra"])
		elif jugadas_humano [-1] == "Papel":
			jugada=random.choice(["Piedra", "Papel"])
		elif jugadas_humano[-1] == "Tijeras":
			jugada=random.choice(["Papel","Tijeras"])			


	return jugada

def panel_puntuacion(puntos_jugador,puntos_ordenador,numero_jugadas):
	
	os.system("cls")
	
	print()
	print("			PIEDRA,  PAPEL,  TIJERAS:  {} de 10".format(numero_jugadas))
	print("			-----------------------------------")
	print("			Puntos tu:	{}  -   {}   : ordenador".format(puntos_jugador,puntos_ordenador))  
	print("			-----------------------------------")
	print()


#Programa Principal


puntos_jugador = 0
puntos_ordenador = 0
numero_jugadas= 1
jugadas_humano= ["Piedra"]
ultimo_resultado=1


while True:
	
	panel_puntuacion(puntos_jugador,puntos_ordenador,numero_jugadas)
	
	jugada_humano = movimiento_jugador()
	
	jugada_ordenador= movimiento_ordenador_con_ia(jugadas_humano,ultimo_resultado)
	
	ganador= comprobar_ganador(jugada_humano,jugada_ordenador)
	
	print()
	dibujo(jugada_humano)
	print()
	dibujo(jugada_ordenador)
	print()
	print("           El ordenador:",jugada_ordenador)
	print()
	
	numero_jugadas+= 1
	
	jugadas_humano.append(jugada_humano)
	
	if ganador=="Humano":
		puntos_jugador += 1
		ultimo_resultado =1
		print("          Ganas Tu")
		print()
	elif ganador== "Ordenador":
		puntos_ordenador+=1
		ultimo_resultado=0
		print("          Gana el ordenador")
		print()
			 
	elif ganador =="Ninguno":
		print("          EMPATE")
		print()
		
	input(" ENTER PARA CONTINUAR")
	
	if numero_jugadas == 10:
		panel_puntuacion(puntos_jugador,puntos_ordenador,numero_jugadas)
		mensaje1 = "Fin de la Partida"
		if puntos_jugador > puntos_ordenador:
			mensaje2= " HAS GANADO" 
		elif puntos_jugador<puntos_ordenador:
			mensaje2= "HAS PERDIDO"
		else:
			mensaje2= "EMPATE"
		
		print()
		print()
		print("           {}".format(mensaje1))	
		print("           {}".format(mensaje2))			
		print()
		print()
		
		break
		







