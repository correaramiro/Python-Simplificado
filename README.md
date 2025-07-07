# ![Python logo](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/1280px-Python_logo_and_wordmark.svg.png)

## Índice

* [Introducción a Python](#introducción-a-python)
* [Características](#caracteristicas)
* [Aplicaciones](#aplicaciones)
* [Instalación y configuración](#instalación-y-configuración)
* [Primer programa en Python](#primer-programa-en-python)
* [Tipos de datos basicos](#tipos-de-datos-basicos)
* [Variables](#variables)
* [Declaración y asignación de variables](#declaración-y-asignación-de-variables)
* [Operadores](#operadores)
* [Estructuras de control](#estructuras-de-control)
* [Bucles / Loops](#bucles--loops)

## Introducción a Python

Creado a finales de los 80's y principios de los 90's, por el programador holandés Guido van Rossum.

> La primera versión fue la **0.9.0**, se lanzó en **1991**.

Python se diseñó con el **objetivo de ser un lenguaje fácil de leer y escribir, con una sintaxis clara y concisa**. A lo largo de los años, ha evolucionado y ganado popularidad hasta convertirse en uno de los lenguajes de programación **más utilizados en el mundo**. 

## Características

- Legibilidad
- Tipado dinámico
- Interpretado
- Multiplataforma
- Amplia biblioteca estándar
- Comunidad activa

## Aplicaciones

- Desarrollo web
- Ciencia de datos
- Inteligencia artificial y machine learning
- Automatización de tareas
- Desarrollo de juegos

## Instalación y configuración

1. Ve al sitio web oficial de Python: https://www.python.org
2. En la sección **Download** encontrarás la última versión estable de Python. Selecciona la versión adecuada para tu sistema operativo (*Windows, macOS o Linux*).
3. Descarga el **instalador de Python** correspondiente a tu sistema operativo.
4. Una vez descargado, ejecuta el instalador. Asegúrate de marcar la opción **Add Python to PATH** durante el proceso de instalación en Windows. Esto te permitirá **ejecutar Python desde la línea de comandos**.
5. Sigue las instrucciones del instalador y espera a que se complete la instalación. 

Para saber si Python se instaló correctamente, prueba a abrir la línea de comandos y escribe el siguiente comando.

```
python --version
```
La consola debería devolver la versión de Python instalada.

## Primer programa en Python

1. Abre tu **IDE** o editor de texto preferido y crea un nuevo archivo.
2. Nombra el archivo como ``hola_mundo.py``. La extensión ``.py`` indica que es un archivo de **Python**. 
3. En el archivo, escribe el siguiente código:
```python
print("Hola mundo")
```
4. Guarda el archivo y ejecuta el programa. Si estás utilizando un **IDE**, busca la opción **Run** o **Execute**. 

Verás que el mensaje ``Hola mundo`` se imprime en la pantalla.

## Tipos de datos básicos

### Enteros ``int``

Números **sin decimales**.

**Ejemplo**

```python
edad = 25
cantidad = 100
```

### Flotantes ``float``

Números con una **parte decimal**.

**Ejemplo**

```python
precio = 9.99
altura = 1.75
```

### Cadenas de texto ``string``

Secuencias de caracteres encerrados en ``''`` o ``""``, se utiliza ``\`` para agregar **caracteres especiales** usando ``\'`` o ``\"``. También usando triple comilla ``'''...'''`` o ``"""..."""`` para cadenas de **varias líneas** o usar ``\n``, ``\t`` para agregar una tabulación.

Para evitar que Python **interprete secuencias de escape**, se pueden usar cadenas **crudas** (*raw strings*), que se indican con una ``r`` antes de la cadena.

**Ejemplo**

```python
nombre = "Juan"
mensaje = '¡Hola mundo!'

caracter_especial = "Ella dijo: \"Hola\""
varias_lineas = """Esta es una cadena
de varias líneas
en Python."""
varias_lineas = "\tJuan"

raw_string = r"C:\nombre\directorio"
```

### Booleanos ``bool``

Representan valores de verdad: ``True`` y falso: ``False``. Se utilizan en operadores **logicos**

**Ejemplo**

```python
es_mayor_de_edad = True
tiene_documento = False
```
> ``True`` y ``False`` siempre se escriben con mayúscula al inicio.

## Variables

Las variables son contenedores que nos permiten almacenar y manipular datos en nuestros programas. Puedes pensar en una variable como una etiqueta a la que asignas a un valor específico. En Python, no es necesario declarar el tipo de datos de una variable de antemano, ya que Python infiere el tipo de datos automáticamente en función del valor asignado.

## Declaración y asignación de variables

Para declarar y asignar variables se utiliza el operador ``=``, el nombre de la variable va a la izquierda y el valor a la derecha.

**Ejemplo**

``nombre_de_la_variable = valor``

**Ejemplo 2**

```python
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True
```

> (Python distinge **minusculas** y **mayusculas**, entonces ``variable``, ``Variable`` y ``VARIABLE``, son tres variables distintas)

Se puede asignar el **mismo valor** a **múltiples variables** en una sola línea, usando el **operador de asignación múltiple**

**Ejemplo**

```python
a = b = c = 10
```

### Normas para nombrar variables

* Los nombres **solo pueden contener** letras (**a-z**) (**A-Z**), números (**0-9**) y guiones bajos (``_``). No pueden comenzar con **números**.

* No se puede utilizar palabras **claves reservadas** de Python como nombres (``if, else, for, while``, etc.)

* Se recomienda utilizar nombres descriptivos para las variables, que indiquen claramente su propósito (**Ej.** ``nombre, edad, total_ventas``, etc.)

Algunos nombres de variables siguiendo estas normas serían:

| ✅ VALIDO| ❌ INVALIDO|
|---|---|
| ``edad`` | ``1edad`` |
| ``nombre_completo`` | ``nombre-completo`` |
| ``_contador`` | ``if`` |

## Operadores

Son **símbolos especiales** que nos permiten **realizar operaciones** en **variables** y **valores**.

### Aritmeticos

* Suma ``+`` : suma dos valores.
* Resta ``-`` : resta el segundo valor al primero.
* Multiplicación ``*`` : multiplica dos valores.
* División ``/`` : divide el primer valor por el segundo y devuelve un resultado de tipo flotante.
* División entera ``//`` : divide el primer valor por el segundo y devuelve un resultado entero (*se descartan los decimales*).
* Módulo ``%`` : devuelve el resto de la división entre el primer y el segundo valor.
* Exponenciación ``**`` : eleva el primer valor a la potencia del segundo.

**Ejemplo**

```python
a = 10
b = 3

suma = a + b #13
resta = a - b #7
multiplicacion = a * b #30
division = a / b #3.333333333
division_entera = a // b #3
modulo = a % b #1
exponenciacion = a ** b #1000
```

> Los comentarios indican el resultado que devuelve Python.

### Comparación

Operadores que se utilizan para comparar dos valores y devuelven un valor booleano (``True`` o ``False``), según el resultado de la comparación.

* Igual a ``==`` : devuelve ``True`` si ambos valores son iguales.
* Diferente a ``!=`` : devuelve ``True`` si los valores son diferentes.
* Mayor que ``>`` : devuelve ``True`` si el primer valor es mayor que el segundo.
* Menor que ``<`` : devuelve ``True`` si el primer valor es menor que el segundo.
* Mayor o igual que ``>=`` : devuelve ``True`` si el primer valor es mayor o igual que el segundo.
* Menor o igual que ``<=`` : devuelve ``True`` si el primer valor es menor o igual que el segundo.

**Ejemplo**

```python
a = 10
b = 3

igual = a == b #False
diferente = a != b #True
mayor = a > b #True
menor = a < b #False
mayor_o_igual = a >= b #True
menor_o_igual = a <= b #False
```

> Los comentarios indican el resultado que devuelve Python.

### Lógicos

Se utilizan para combinar expresiones condicionales y evaluar múltiples condiciones.

* AND ``and`` : devuelve ``True`` si ambas condiciones son verdaderas.
* OR ``or`` : devuelve ``True`` si al menos una de las condiciones es verdadera.
* NOT ``not`` : invierte el valor de una condición, devuelve ``True`` si la condición es falsa y ``False`` si la condición es verdadera.

**Ejemplo**

```python
a = 10
b = 3

resultado_and = (a > 5) and (b < 5) #True
resultado_or = (a > 15) or (b < 5) #True
resultado_not = not (a > 5) #False
```

> Los comentarios indican el resultado que devuelve Python.

> Python sigue las reglas de precedencia de operaciones, la precedencia es: **paréntesis, exponenciación, multiplicación/división, suma/resta, operadores de comparación y operadores lógicos**.

## Estructuras de control

Las **estructuras de control** nos permiten controlar **el flujo de ejecución** de nuestros programas. En Python, las estructuras de control más comunes son las estructuras **condicionales** y los **bucles**. Estas estructuras nos permiten tomar **decisiones** y **repetir** bloques de código según ciertas condiciones.

### Estructuras condicionales
 
### ``if``

La estructura ``if`` se utiliza para ejecutar un bloque de código si una **condición es verdadera**.

**Sintaxis básica**

```python
if condicion:
    # Bloque de código a ejecutar si la condición es verdadera
    instrucciones
```

**Ejemplo**

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

> En este ejemplo, si la variable ``edad`` es mayor o igual a **18**, se ejecutará el bloque de código dentro del ``if`` y se imprimirá el mensaje: ``Eres mayor de edad``

### ``if - else``

La estructura ``if - else`` nos permite especificar un bloque de código **alternativo** que se ejecutará si la condición del ``if`` es **falsa**.

**Ejemplo**

```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

> En este ejemplo, si la variable edad es **mayor o igual a 18**, se ejecutará el bloque de código dentro del ``if`` y se imprimirá el mensaje ``Eres mayor de edad``. De lo contrario, se ejecutará el bloque de código dentro del ``else`` y se imprimirá el mensaje ``Eres menor de edad``.

### ``if  elif  else``

La estructura ``if  elif  else`` nos permite especificar **múltiples condiciones** y bloques de código **alternativos**.

**Sintaxis básica**

```python
if condicion_1:
    # Bloque de código a ejecutar si la condicion_1 es verdadera.
    instrucciones
elif condicion_2:
    # Bloque de código a ejecutar si la condicion_2 es verdadera.
    instucciones
else:
    # Bloque de código a ejecutar si ninguna de las condiciones anteriores es verdadera.
    instrucciones
```

**Ejemplo**

```python
calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bueno")
elif calificacion >= 70:
    print("Bueno")
else:
    print("Necesita mejorar")
```

> En este ejemplo, se evalúan múltiples condiciones en orden. Si la variable **calificación** es **mayor o igual a 90**, se imprime ``Excelente``. Si no se cumple la **primera condición**, pero si **calificación** es **mayor o igual a 80**, se imprime ``Muy bueno``. Si no se cumplen las condiciones anteriores, pero si **calificación** es **mayor o igual a 70**, se imprime ``Bueno``. Si ninguna de las condiciones anteriores es **verdadera**, se ejecuta el bloque ``else`` y se imprime ``Necesita mejorar``

## Bucles / Loops

Los bucles nos permiten **repetir** un bloque de código varias veces. En Python, los bucles más comunes son ``for`` y ``while``

### ``for``

El bucle for se utiliza para **iterar** sobre una secuencia (*como una lista, una tupla o una cadena*) o cualquier objeto iterable.

**Sintaxis básica**

```python
for variable in secuencia:
    # Bloque de código a repetir
    instrucciones
```

**Ejemplo**

```python
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
```

> En este ejemplo, el bucle for **itera** sobre la lista frutas. En cada iteración, la variable ``fruta`` toma el **valor de un elemento de la lista**, y se **ejecuta** el bloque de código dentro del **bucle**. En este caso, se imprime cada fruta en una línea separada.

### ``while``

El bucle ``while`` se utiliza para **repetir** un bloque de código mientras una condición sea **verdadera**.

**Sintaxis básica**

```python
while condicion:
    # Bloque de código a repetir
    instrucciones 
```

**Ejemplo**

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

> En este ejemplo, el bucle ``while`` se **ejecuta mientras la variable** ``contador`` sea **menor que 5**. En cada iteración, se imprime el **valor de contador** y luego se **incrementa en 1** mediante la instrucción contador ``+= 1``. El bucle se **detendrá** cuando ``contador`` alcance el **valor de 5**.

> Te darás cuenta que el contador se detiene en **4**, esto es porque el contador **comienza** en **0**, por lo que imprime los valores del 0 al 4.

> Es **importante** tener cuidado al usar el bucle ``while``, ya que, si la condición **nunca** se vuelve **falsa**, el bucle se ejecutará **indefinidamente**, lo que se conoce como un **bucle infinito**.

### Control de bucles

Python proporciona algunas **instrucciones especiales** para **controlar** el flujo de ejecución dentro de los bucles.

### ``break``

La instrucción ``break`` se utiliza para **salir prematuramente de un bucle**, **independientemente** de la condición. Cuando se encuentra un ``break``, el bucle se **detiene** y el flujo de ejecución **continúa** con la siguiente instrucción fuera del bucle.

**Ejemplo**

```python
contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break
```

> En este ejemplo, el bucle ``while`` se **ejecuta indefinidamente** debido a la condición ``True``. Sin embargo, dentro del bucle se utiliza una **estructura condicional** ``if`` para verificar si contador es **igual a 5**. Cuando se cumple esta condición, se ejecuta la instrucción ``break``, lo que hace que el bucle se detenga y el flujo de ejecución **continúe** con la siguiente instrucción fuera del bucle.

### ``continue``

La instrucción ``continue`` se utiliza para **saltar** el resto del bloque de código dentro de un bucle y **pasar** a la siguiente iteración.

**Ejemplo**

```python
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
```

> En este ejemplo, el bucle ``for`` itera sobre los números del **0 al 9** utilizando la función ``range()``. Dentro del bucle, se **verifica** si el número es divisible por **2** utilizando el operador de módulo ``%``. Si el número es divisible por 2 (*es decir, si es par*), se ejecuta la instrucción ``continue``, lo que hace que se salte el resto del bloque de código y se pase a la siguiente iteración del bucle. Como resultado, solo se imprimirán los números **impares**.

### ``pass``

La instrucción ``pass`` es una operación **nula** que no hace nada. Se utiliza como **marcador de posición** cuando se requiere una instrucción **sintácticamente**, pero no se desea realizar ninguna acción.

**Ejemplo**

```python
for a in range(5):
    pass
```

> En este ejemplo, el bucle ``for`` itera sobre los números del **0 al 4**, pero no se realiza ninguna acción dentro del bucle debido a la instrucción ``pass``. Esto puede ser útil cuando se está desarrollando un programa y se desea **reservar** un bloque de código para implementarlo más adelante.

## Estructuras de datos

Las **estructuras de datos** nos permiten **organizar y almacenar** datos de manera eficiente en nuestros programas. **Python** proporciona varias estructuras de **datos integradas**, como **listas, tuplas, diccionarios y conjuntos**, cada una con sus propias características y usos.

### Listas

Una lista es una **estructura de datos mutable** y ordenada que permite almacenar una **colección de elementos**. Los elementos de una lista pueden ser de **diferentes tipos de datos** y se encierran entre corchetes ``[]``, separados por comas.

**Creación y acceso**

Para crear una lista, simplemente encierra los elementos entre corchetes:

```python
frutas = ["manzana", "banana", "naranja"]
```

Para acceder a los elementos de una lista, utilizar el índice del elemento entre corchetes. Los índices comienzan desde 0.

```python
print(frutas[0]) #Imprime "manzana"
print(frutas[1]) #Imprime "banana"
print(frutas[2]) #Imprime "naranja"
```

También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. El índice ``-1`` representa el último elemento, ``-2`` representa el penúltimo, y así sucesivamente.

```python
print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"
```

**Métodos de listas**

Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista. Algunos métodos comunes son:

* ``append(elemento):`` Agrega un elemento al final de la lista.
* ``insert(índice, elemento):`` Inserta un elemento en una posición específica de la lista.
* ``remove(elemento):`` Elimina la primera aparición de un elemento en la lista.
* ``pop(índice):`` Elimina y devuelve el elemento en una posición específica de la lista.
* ``sort():`` Ordena los elementos de la lista en orden ascendente.
* ``reverse():`` Invierte el orden de los elementos en la lista.

**Ejemplo**

```python
frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]
```

### Listas de comprensión

Las listas de comprensión son una forma concisa de crear nuevas listas basadas en una secuencia existente. Permiten filtrar y transformar los elementos de una lista en una sola línea de código.

**Sintaxis básica**

```python
nueva_lista = [expresion for elemento in secuencia if condicion]
```

**Ejemplo**

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]
```

> En este ejemplo, se crea una nueva lista llamada ``cuadrados``, que contiene los cuadrados de los números pares de la lista **numeros**. La expresión ``x ** 2`` eleva cada elemento al **cuadrado**, y la condición ``if x % 2 == 0`` filtra solo los números **pares**.