"""
Ejemplo sumatoria 
"""
def f_suma():
    suma = 0
    for i in range (100,45001):
        suma += 2*i + 8
    return suma

def sol_suma():
    return 45000*45001 - 99*100 + 8*45000 - 8*99

print(f_suma(), sol_suma())  


"""
Ejemplo sumatoria 2
"""
def f_sum(n):
    suma = 0
    for i in range (-40, 2*n+1):
        for j in range (40,n**2+1):
            suma += 2*i*j + 8*j
    return suma

def sol_suma(n):
    x = (n**2*(n**2+1))/2 -39*20
    parte1 = -40*41+2*n*(2*n+1)
    parte2 = 8*(2*n+41)
    return x*(parte1+parte2)

for n in [10,20,40,80,100]:
    print(n,f_sum(n), sol_suma(n))