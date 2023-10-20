import random
import time
import csv

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

# Función para cargar datos de prueba (simulados)
def cargar_datos(cantidad_registros):
    datos = [{"nDIEmp": i, "Nombre": f"Empleado {i}"} for i in range(1, cantidad_registros + 1)]
    return datos

# Implementación de Bubble Sort para ordenar por la columna 'nDIEmp'
def bubble_sort_por_columna(datos):
    start_time = time.time()
    n = len(datos)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if datos[j]["nDIEmp"] > datos[j + 1]["nDIEmp"]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    end_time = time.time()
    return end_time - start_time

def selection_sort_por_columna(datos):
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

def insertion_sort_por_columna(datos):
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

def merge_sort_por_columna(datos):
    def merge(L, R):
        result = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i]["nDIEmp"] < R[j]["nDIEmp"]:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        result.extend(L[i:])
        result.extend(R[j:])
        return result

    if len(datos) <= 1:
        return datos
    mid = len(datos) // 2
    L = datos[:mid]
    R = datos[mid:]
    L = merge_sort_por_columna(L)
    R = merge_sort_por_columna(R)
    return merge(L, R)

# Función para proyectar registros futuros
def proyectar_registros_futuros(cantidad_registros_inicial, tasa_crecimiento_anual, años):
    return cantidad_registros_inicial * (1 + tasa_crecimiento_anual) ** años


# Función principal
class Main():
    def main():
        cantidad_registros_inicial = len(datos)
        # Definir la tasa de crecimiento antes del bucle principal
        tasa_crecimiento_anual = 0.05  # Tasa de crecimiento del 5% anual
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
                tiempo_ordenamiento = bubble_sort_por_columna(datos.copy())
                print(f"Tiempo de ordenamiento con Bubble Sort: {tiempo_ordenamiento:.6f} segundos")
                print(f"Cantidad de registros iniciales: {cantidad_registros_inicial}")
                cantidad_registros_futuros = proyectar_registros_futuros(cantidad_registros_inicial, tasa_crecimiento_anual, años)
                print(f"Cantidad de registros proyectados en {años} años: {cantidad_registros_futuros}")

            elif opcion == 2:
                tiempo_ordenamiento = selection_sort_por_columna(datos.copy())
                print(f"Tiempo de ordenamiento con Selection Sort: {tiempo_ordenamiento:.6f} segundos")
                print(f"Cantidad de registros iniciales: {cantidad_registros_inicial}")
                cantidad_registros_futuros = proyectar_registros_futuros(cantidad_registros_inicial, tasa_crecimiento_anual, años)
                print(f"Cantidad de registros proyectados en {años} años: {cantidad_registros_futuros}")

            elif opcion == 3:
                tiempo_ordenamiento = insertion_sort_por_columna(datos.copy())
                print(f"Tiempo de ordenamiento con Insertion Sort: {tiempo_ordenamiento:.6f} segundos")
                print(f"Cantidad de registros iniciales: {cantidad_registros_inicial}")
                cantidad_registros_futuros = proyectar_registros_futuros(cantidad_registros_inicial, tasa_crecimiento_anual, años)
                print(f"Cantidad de registros proyectados en {años} años: {cantidad_registros_futuros}")

            elif opcion == 4:
                datos_copy = datos.copy()
                tiempo_ordenamiento = time.time()
                merge_sort_por_columna(datos_copy)
                tiempo_ordenamiento = time.time() - tiempo_ordenamiento
                print(f"Tiempo de ordenamiento con Merge Sort: {tiempo_ordenamiento:.6f} segundos")
                print(f"Cantidad de registros iniciales: {cantidad_registros_inicial}")
                cantidad_registros_futuros = proyectar_registros_futuros(cantidad_registros_inicial, tasa_crecimiento_anual, años)
                print(f"Cantidad de registros proyectados en {años} años: {cantidad_registros_futuros}")

    main()