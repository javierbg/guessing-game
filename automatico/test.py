#import sys
from guess import *

#Se obtendrá el número de tests por línea de argumentos

#n_tests = int(sys.argv[1])
#aciertos = test_automatico(0, 500, 0, 500, n_tests)
#		
#print("Acertados " + str(aciertos) + " de " + str(n_tests))
#print("Porcentaje de acierto = " + str( (aciertos/n_tests) * 100 ) )

n_tests = 1000

#Esto almacenará las tuplas con los resultados
resultados = []

#Este test hace comprobaciones sobre como se comporta
#la probabilidad de acierto según la desviación típica
for i in range(1, 1000, 10):
	aciertos = test_automatico(0, i, 0, i, n_tests)
	resultados.append( (i, (aciertos / n_tests)) )
	
f_result = open('dev_tipica.csv', 'w')
f_result.write('Desviación típica,Probabilidad de acierto\n')
for r in resultados:
	f_result.write('{sd},{prob}\n'.format(sd=r[0], prob=r[1]) )
f_result.close()

resultados = []
#Este test hace comprobaciones sobre como se comporta
#la probabilidad de acierto según la diferencia de mu
for i in range(1, 100, 1):
	sigma = 5000
	aciertos = test_automatico(0, sigma, i, sigma, n_tests)
	resultados.append( (i, (aciertos / n_tests)) )
	
f_result = open('dif_mu.csv', 'w')
f_result.write('Diferencia de medias,Probabilidad de acierto\n')
for r in resultados:
	f_result.write('{deltamu},{prob}\n'.format(deltamu=r[0], prob=r[1]) )
f_result.close()
