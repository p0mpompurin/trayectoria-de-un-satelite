#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Librerías utilizadas

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# In[9]:


G = 6.67430e-11  # Constante gravitacional (m^3 kg^-1 s^-2)
M_planeta = 5.972e24 #Masa del planeta
R_planeta = 6.371e6 #Radio del planeta
m_satelite = 500 #Masa del satélite
r_orbita = 2.5e7 #Radio de la órbita inicial

# Condiciones iniciales
x_satelite = 2.5e7 # Radio órbita
y_satelite = 0.0 # Posición inicial en el eje Y
vx_satelite = 0.0 #Velocidad inicial en el eje X
vy_satelite = np.sqrt( (G * M_planeta) / (R_planeta + r_orbita)) # Velocidad de escape del planeta en eje Y


class Satelite: # Se define la clase Satelite
    def __init__(self, x, y, vx, vy): # Toma cuatro parámetros que representan la posición y velocidad inicial
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0.0
        self.ay = 0.0

def update_pos(sat, dt): # Se define una función que toma un objeto de la clase Satelite y un incremento de tiempo
    """ Esta función actualiza la posición del satélite """
    sat.x += sat.vx * dt
    sat.y += sat.vy * dt

def update_vel(sat, dt): # Se define una función que toma un objeto de la clase Satélite y un incremento de tiempo
    """ Esta función actualiza la velocidad del satélite """
    sat.vx += sat.ax * dt
    sat.vy += sat.ay * dt

def leapfrog(sat, dt): #Se definde la función Leapfrog que toma un objeto de la clase Satélite y un incremento de tiempo
    """ Esta función utiliza el método de Leapfrog para simular la trayectoria del satélite """
    
    update_pos(sat, dt/2) # Llama la función para actualizar la posición en la mitad del paso del tiempo
    angulo = np.arctan2(sat.y, sat.x) # Calcula el ángulo de la posición del satélite en coordenadas polares
    sat.ax = (-G * M_planeta / (sat.x**2 + sat.y**2)) * np.cos(angulo) # Calcula la acelaración en el eje X
    sat.ay = (-G * M_planeta / (sat.x**2 + sat.y**2)) * np.sin(angulo) # Calcula la aceleración en el eje Y
    update_vel(sat, dt/2) # Llama la función para actualizar la velocidad en la mitad del paso del tiempo


satelite = Satelite(x_satelite, y_satelite, vx_satelite, vy_satelite) # Se crea un objeto con las condiciones iniciales
dt = 100 # Se define el tamaño del paso de tiempo
pasos = 1000 # Número de los pasos de tiempo, cuánto la simulación avanzará en el tiempo


X, Y = [], [] # Se crean listas vacías para almacenar las posiciones

for _ in range(pasos): # Iteración sobre el número de pasos
    leapfrog(satelite, dt) # Llamado a la función Leapfrog para avanzar con la simulación
    X.append(satelite.x) # Se guarda la coordenada x
    Y.append(satelite.y) # Se guarda la coordenada y

# Gráfico de los datos
plt.plot(X, Y, color = 'blue', label = 'Trayectoria del Satélite')
plt.scatter(0, 0, color = 'green', marker = 'o', label = 'Planeta')
plt.scatter(x_satelite, y_satelite, color='red', marker= 'o', label = 'Satélite')
plt.title('Trayectoria del Satélite')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc = 'upper right', bbox_to_anchor=(0.1, 0.1))
plt.grid(True)
plt.show()


# In[10]:


fig, ax = plt.subplots() # Crea una figura y un conjunto de ejes
trayectoria, = ax.plot([], [], color='blue') # Se crea un objeto para representar la trayectoria
planeta, = ax.plot([], [], 'o', color='green') # Se crea un objeto para representar el planeta
satelite_dot, = ax.plot([], [], 'o', color='red') # Se crea un objeto para representar la posición actual del satélite

def init():
    """ Esta función establece los límites de los ejes y devuelve los objetos trayectoria, planeta y satelite_dot """
    ax.set_xlim(-3e7, 3e7)
    ax.set_ylim(-3e7, 3e7)
    return trayectoria, planeta, satelite_dot

def update(frame):
    """ Esta función actualiza la animación de cada frame y devuelve los objetos actualizados """
    leapfrog(satelite, dt)
    X.append(satelite.x)
    Y.append(satelite.y)
    trayectoria.set_data(X, Y)
    planeta.set_data(0, 0)
    satelite_dot.set_data(satelite.x, satelite.y)
    return trayectoria, planeta, satelite_dot


X, Y = [], [] # Lista vacía para almacenar las coordenadas X e Y en cada paso

# Crea una animación utilizando la función FuncAnimation 
animacion = FuncAnimation(fig, update, frames = pasos, init_func = init, blit=True, interval = 70)
# Se guarda la animación como archivo gif
animacion.save('trayectoriadelsatelite.gif', writer='pillow')

# Gráfico de los datos
plt.title('Trayectoria del Satélite')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

