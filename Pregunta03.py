f=3
c=3
matriz = []
for i in range(f):
    matriz.append([1]*c)

n= matriz[0][2]
m= matriz[1][2]
z= matriz[2][2]

suma_diagonal= n+m+z

print(suma_diagonal)