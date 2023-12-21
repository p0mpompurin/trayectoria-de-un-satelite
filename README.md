# trayectoria-de-un-satelite

El siguiente código tiene la finalidad de simular la trayectoria de un satélite mediante el control de sus condiciones iniciales, utilizando el método de integración de Leapfrog. Entre las dependencias del código se encuentran las librerías numpy, matplotlib.pyplot y matplotlib.animation.

En este repositorio podrán encontrar las siguientes funciones: update_pos, update_vel, leapfrog y update.

La función update_pos tiene como finalidad actualizar la posición en el eje X e Y del satélite dadas las condiciones iniciales de velocidad y un paso de tiempo. Esta función recibe como argumentos un objeto de la clase Satelite y un incremento de tiempo.

Luego update_vel actualizará la velocidad del satélite dada una aceleración calculada a través de la fuerza de gravitación y también un paso de tiempo. Esta función recibe como argumentos un objeto de la clase Satelite y un incremento de tiempo.

Después se presenta la función Leapfrog que va a desempeñar la labor de simular la órbita del satélite mediante las actualizaciones de posición y velocidad en los pasos de tiempo elegidos. Esta función recibe como argumentos un objeto de la clase Satelite y un incremento de tiempo.

Por último la función update se encargará de actualizar cada frame de la animación que muestra la trayectoria retornando de esta forma los objetos actualizados.

Observación: Los valores relacionados a las características del planeta y satélite se pueden modificar a gusto. El lenguaje de programación utilizado es Python

