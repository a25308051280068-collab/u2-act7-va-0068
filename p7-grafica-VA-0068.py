import matplotlib.pyplot as plt
import numpy as np

# Christian Garcia Jimenez Nc = 0068 
# Fecha 26/miercoles/10/octubre/2026
print("Christian Garcia Jimenez Nc = 0068")
# Datos
no_lista = [1, 2, 3, 17, 48]
califa_ml = [20, 30, 80, 100, 90]
califa_va = [70, 90, 60, 90, 100]

plt.plot(no_lista, califa_ml, label="califa ML")
plt.plot(no_lista, califa_va, label="califa VA")  # <--- Corregido
plt.title("Calificaciones materias 0068")
plt.xlabel("numero de lista")  # Muestra las etiquetas (labels) de cada línea
plt.ylabel("Calificaciones")
plt.legend()
plt.show()
print("Christian Garcia Jimenez Nc = 0068")