#orden constante
def displayNum(n):
    print(n)
displayNum(42)
print('---------')
#Orden logarítmico = O(log n)
def displayQuick(n):
    k = 1
    while k <= n:
        print(k)
        k *= 5
displayQuick(10)
print('---------')
#Orden lineal = O(n)
def sum1To(n):
    sum = 1
    for k in range(1, n + 1):
        sum += k
    return sum
print (sum1To(10))
print('---------')
#Orden cuadrático = O(n2)
def display(n):
    for k in range(1, n + 1):
        for j in range(1, n + 1):
            print(j, end=' ')
        print()
display(10)