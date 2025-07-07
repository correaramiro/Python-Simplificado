# Metodos de listas

frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)

frutas.insert(1, "uva")
print(frutas)

frutas.remove("banana")
print(frutas)

fruta_eliminada = frutas.pop(2)
print(frutas)
print(fruta_eliminada)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

# Listas de comprensión

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)