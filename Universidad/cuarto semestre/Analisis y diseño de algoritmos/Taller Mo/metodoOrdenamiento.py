import random
import time
import csv
import statistics

# Función para cargar datos desde un archivo CSV
def cargar_datos_desde_csv(archivo_csv):
    datos = []
    with open(archivo_csv, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')  # Especifica el delimitador como punto y coma
        for row in reader:
            datos.append({"nDIEmp": int(row["nDIEmp"]), "Nombre": row["nomEmp"]})
    return datos

# Reemplaza la ruta con la correcta a tu archivo CSV
archivo_csv = "C:/Users/crist/OneDrive/Documentos/Programacion/Universidad/cuarto semestre/Analisis y diseño de algoritmos/Taller Mo/Libro1.csv"
datos = cargar_datos_desde_csv(archivo_csv)

# Implementación de Bubble Sort para ordenar por la columna 'nDIEmp'
def bubble_sort(datos):
    start_time = time.time()
    n = len(datos)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if datos[j]["nDIEmp"] > datos[j + 1]["nDIEmp"]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    end_time = time.time()
    return end_time - start_time

# Implementación de Selection Sort
def selection_sort(datos):
    start_time = time.time()
    n = len(datos)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if datos[j]["nDIEmp"] < datos[min_index]["nDIEmp"]:
                min_index = j
        datos[i], datos[min_index] = datos[min_index], datos[i]
    end_time = time.time()
    return end_time - start_time

# Implementación de Insertion Sort
def insertion_sort(datos):
    start_time = time.time()
    for i in range(1, len(datos)):
        key = datos[i]
        j = i - 1
        while j >= 0 and key["nDIEmp"] < datos[j]["nDIEmp"]:
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = key
    end_time = time.time()
    return end_time - start_time

# Implementación de Merge Sort
def merge_sort(datos):
    if len(datos) > 1:
        mid = len(datos) // 2
        L = datos[:mid]
        R = datos[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i]["nDIEmp"] < R[j]["nDIEmp"]:
                datos[k] = L[i]
                i += 1
            else:
                datos[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            datos[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            datos[k] = R[j]
            j += 1
            k += 1

# Función para proyectar registros futuros
def proyectar_registros_futuros(cantidad_registros_inicial, tasa_crecimiento_anual, años):
    return cantidad_registros_inicial * (1 + tasa_crecimiento_anual) ** años

# Función para determinar el mejor algoritmo de ordenamiento
def determinar_mejor_algoritmo(datos, tasa_crecimiento_anual, años):
    tiempos_bubble = ejecutar_algoritmo(bubble_sort, datos.copy())
    tiempos_selection = ejecutar_algoritmo(selection_sort, datos.copy())
    tiempos_insertion = ejecutar_algoritmo(insertion_sort, datos.copy())
    tiempos_merge = ejecutar_algoritmo(merge_sort, datos.copy())

    desviacion_bubble = statistics.stdev(tiempos_bubble) if tiempos_bubble else 0
    desviacion_selection = statistics.stdev(tiempos_selection) if tiempos_selection else 0
    desviacion_insertion = statistics.stdev(tiempos_insertion) if tiempos_insertion else 0
    desviacion_merge = statistics.stdev(tiempos_merge) if tiempos_merge else 0

    dispersión_menor = min(desviacion_bubble, desviacion_selection, desviacion_insertion, desviacion_merge)

    algoritmo_mejor = "Bubble Sort" if dispersión_menor == desviacion_bubble else \
        "Selection Sort" if dispersión_menor == desviacion_selection else \
        "Insertion Sort" if dispersión_menor == desviacion_insertion else "Merge Sort"

    cantidad_registros_inicial = len(datos)
    cantidad_registros_proyectados = proyectar_registros_futuros(cantidad_registros_inicial, tasa_crecimiento_anual, años)

    print(f"Cantidad de registros iniciales: {cantidad_registros_inicial}")
    print(f"Cantidad de registros proyectados en {años} años: {cantidad_registros_proyectados}")
    print(f"El mejor algoritmo de ordenamiento es {algoritmo_mejor} con una dispersión lineal de {dispersión_menor:.6f}")

# Función para ejecutar un algoritmo y medir su tiempo de ejecución
def ejecutar_algoritmo(algoritmo, datos):
    tiempos = []
    for _ in range(10):  # Ejecutar el algoritmo 10 veces
        datos_copia = list(datos)  # Hacer una copia de la lista de datos
        start_time = time.time()
        algoritmo(datos_copia)
        end_time = time.time()
        tiempo = end_time - start_time
        tiempos.append(tiempo)
    return tiempos

# Función principal
def main():
    tasa_crecimiento_anual = 0.05
    años = 5

    while True:
        print("\nMenú de Ordenamiento:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("0. Salir")

        opcion = int(input("Seleccione un método de ordenamiento (0 para salir): "))

        if opcion == 0:
            break

        if opcion == 1:
            determinar_mejor_algoritmo(datos, tasa_crecimiento_anual, años)
        elif opcion == 2:
            determinar_mejor_algoritmo(datos, tasa_crecimiento_anual, años)
        elif opcion == 3:
            determinar_mejor_algoritmo(datos, tasa_crecimiento_anual, años)
        elif opcion == 4:
            determinar_mejor_algoritmo(datos, tasa_crecimiento_anual, años)

main()
