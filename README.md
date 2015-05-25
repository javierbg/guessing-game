# guessing-game
Probando mediante programación una curiosidad estadística

Inspirado por [este vídeo](https://www.youtube.com/watch?v=ud_frfkt1t0 "How to Win a Guessing Game - Numberphile") (en inglés)

## Explicación

El juego se desarrolla de la siguiente forma: un agente escribe dos números (reales) distintos y los oculta. Un segundo agente puede consultar ÚNICAMENTE uno de los dos números. Su objetivo es adivinar si el número todavía oculto es mayor o menor que el que ha sido descubierto.

Al no tener más información y sólo haber dos posibilidades, en un principio, la probabilidad de acertar es del 50%.

Sin embargo, existe una estrategia que permite aumentar la probabilidad de acertar.

## Estrategia

* Se toma una distribución que abarque el mismo rango de valores que los que pueden elegirse para ocultar (en el caso real sería una distribución que abarque todos los números reales, en el caso de un ordenador, una distribución que abarque el rango entre los límites que puede adoptar la variable).
* Se genera un número aleatorio a partir de esa distribución.
* Si el número obtenido es menor que el que se ha desvelado, entonces afirmar que el número oculto es menor, y viceversa.

(Explicación detallada en el vídeo)

## Contenido

* *interactivo/*: Puedes pasar por línea de comandos la cantidad de tests que quieres que se hagan, para modificar las distintas distribuciones hay que hacerlo a mano
* *automatico/*: Genera estadísticas automatizadas
