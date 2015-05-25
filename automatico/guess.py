import random

#Genera el par de números a adivinar
#Los devuelve en forma de tupla
def genera_par(mu, sigma):
	#Genera números a partir de una
	#distribución normal/gaussiana
	while True:
		a = random.gauss(mu, sigma)
		b = random.gauss(mu, sigma)
		if a != b : break #Estúpidamente improbable, pero posible
		
	return (a,b)
		
#Dado la tupla de valores generados elige uno
#e indica si cree que el otro es mayor o menor.
#Devuelve el índice del que cree que es el mayor
def adivina(p, mu, sigma):
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

#Realiza n_tests tests utilizando como parámetros
#para generar números aleatorios los mu_(gen|adv)
#(media de la distribución) y sigma_(gen|adv) para
#la desviación típica (distribución normal, gen para
#la función generadora y adv para la adivinadora)
#Devuelve el número de aciertos
def test_automatico(mu_gen, sigma_gen, mu_adv, sigma_adv, n_tests):
	aciertos = 0
	for i in range(n_tests):
		valores = genera_par(mu_gen, sigma_gen)
	
		resultado_real = valores.index(max(valores))
		resultado_adiv = adivina(valores, mu_adv, sigma_adv)
	
		if resultado_real == resultado_adiv:
			aciertos += 1
	
	return aciertos
