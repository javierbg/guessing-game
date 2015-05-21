import random

#Genera el par de números a adivinar
#Los devuelve en forma de tupla
def genera_par():
	mu = 0		#Media de la distribución
	sigma = 500	#Desv. típica de la distribución
	
	#Genera números a partir de una
	#distribución normal/random.gaussiana
	while True:
		a = random.gauss(mu, sigma)
		b = random.gauss(mu, sigma)
		if a != b : break #Estúpidamente improbable, pero posible
		
	return (a,b)
		
#Dado la tupla de valores generados elige uno
#e indica si cree que el otro es mayor o menor.
#Devuelve el índice del que cree que es el mayor
def adivina(p):
	mu = 0
	sigma = 500
	
	choice = random.choice([0,1])
	a = p[choice]
	
	while True:
		k = random.gauss(mu, sigma)
		if k != a: break #Igual de estúpido que antes
	
	if k < a:
		return choice
	else:
		if choice == 1:	return 0
		else:			return 1
