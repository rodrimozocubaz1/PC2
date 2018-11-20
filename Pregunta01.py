import math

x= int(input("Ingrese el valor en el eje x de su coordenada"))
y= int(input("Ingrese el valor en el eje y de su coordenada"))

coordenada = (x*x) + (y*y)
distancia = math.sqrt(coordenada)
print("La distancia es:")
print (distancia)
print("La coordenada es:")
print(x,",",y)
