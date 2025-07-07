# For

frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

# While

contador1 = 0

while contador1 < 5:
    print(contador1)
    contador1 += 1

# Control de bucles
# Break

contador2 = 0

while True:
    print(contador2)
    contador2 += 1

    if contador2 == 5:
        break

# Continue

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

# Pass

for a in range(5):
    pass
