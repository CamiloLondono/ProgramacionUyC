#ejercicio 1
r = 0
suma = 0
for i in range(5):
    r += 1
    suma += r *( r + 1 )
print (suma)
#ejercicio 2
suma = 0
for r in range(1, 8):
    valor = (-1) ** (r - 1) / r
    suma += valor

print(suma)
#ejercicio 3
suma = 0
for r in range(1, 5): 
    valor = (-1) ** r * 3 ** (r + 1)
    suma += valor

print(suma)
#ejercicio 4
suma = 0
for n in range(3, 21): 
    valor = 1 / n
    suma += valor

print(suma)
#parte 2 primer ejercicio
def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    comparisons = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Realizar un intercambio si es necesario
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps, comparisons

arr = [50, 26, 7, 9, 15, 27]
swaps, comparisons = bubble_sort(arr)
print("Arreglo ordenado:", arr)
print("Intercambios realizados:", swaps)
print("Comparaciones realizadas:", comparisons)
