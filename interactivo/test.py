import sys
from guess import *

#Se obtendrá el número de tests por línea de argumentos

n_tests = int(sys.argv[1])
aciertos = 0
for i in range(n_tests):
	valores = genera_par()
	
	resultado_real = valores.index(max(valores))
	resultado_adiv = adivina(valores)
	
	if resultado_real == resultado_adiv:
		aciertos += 1
		
print("Acertados " + str(aciertos) + " de " + str(n_tests))
print("Porcentaje de acierto = " + str( (aciertos/n_tests) * 100 ) )
