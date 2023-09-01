import matplotlib.pyplot as plt
import numpy as np

def fx():
    # Coordenadas de los puntos dados
    x_points = [-2, -1, 0, 1, 2]
    y_points = [3, 5, 1, 4, 10]

    # Definir el polinomio P(x)
    def P(x):
        return -2.5*x**4 + 15*x**3 - 2.5*x**2 + 10*x

    # Generar puntos para la gráfica
    x = np.linspace(-2.5, 2.5, 100)
    y = P(x)

    # Graficar los puntos dados
    plt.scatter(x_points, y_points, color='red', label='Puntos dados')

    # Graficar el polinomio
    plt.plot(x, y, color='blue', label='Polinomio ajustado')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ajuste de polinomio a puntos dados')
    plt.legend()
    plt.grid(True)
    plt.show()
