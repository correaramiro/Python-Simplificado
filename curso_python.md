# ![Python logo](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/1280px-Python_logo_and_wordmark.svg.png)

## Índice

* [Caracteristicas](#caracteristicas)
* [Aplicaciones](#aplicaciones)
* [Tipos de datos basicos](#tipos-de-datos-basicos)
* [Declaración y asignación de variables](#declaración-y-asignación-de-variables)
* [Operadores](#operadores)

Creado a finales de los 80's y pricipios de los 90's, por Guido van Rossum.

> La primera versión fue la 0.9.0, se lanzo en 1991.

## Caracteristicas

- Legibilidad
- Tipado dinamico
- Interpretado
- Multiplataforma
- Amplia biblioteca estandar
- Comunidad activa

## Aplicaciones

- Desarrollo web
- Ciencia de datos
- Inteligencia artificial y machine learnig
- Automatizado de tareas
- Desarrollo de juegos

***

## Tipos de datos basicos

### Enteros (``int``)

Números **sin decimales**.

**Ejemplo**

```python
edad = 25
cantidad = 100
```

### Flotantes (``float``)

Números con un **par decimal**.

**Ejemplo**

```python
precio = 9.99
altura = 1.75
```

### Cadenas de texto (``string``)

Secuencias de caracteres encerrados en ``''`` o ``""``, se utiliza ``\`` para agregar **caracteres especiales** usando ``\'`` o ``\"``. Tambien usando triple comilla ``'''...'''`` o ``"""..."""`` para cadenas de **varias lineas** o usar ``\n``, ``\t`` para agregar una tabulación.

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

### Booleanos

Representan valores de verdad: ``True`` y falso: ``False``. Se utilizan en operadores **logicos**

**Ejemplo**

```python
es_mayor_de_edad = True
tiene_documento = False
```

## Declaración y asignación de variables

Para declarar y asignar variables se utiliza el operador ``=``.

**Ejemplo**

``nombre_de_la_variable = valor``

**Ejemplo 2**

```python
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True
```

> *(Python distinge **minusculas** y **mayusculas**, entonces ``variable``, ``Variable`` y ``VARIABLE``, son tres variables distintas)*

Se puede asignar el **mismo valor** a **multiples variables** en una sola linea, uzando el **operador de asignación multiple**

**Ejemplo**

```python
a = b = c = 10
```

### Normas para nombrar variables

* Los nombres **solo pueden contener** letras (**a-z**) (**A-Z**), números (**0-9**) y guines bajos (``_``). No pueden comenzar con **números**.

* No se puede utilizar palabras **calves reservadas** de Python como nombres (``if, else, for, while``, etc.)

* Se recomienda utilizar nombres descriptivos para las variables, que indiquen claramente su proposito (**Ej.** ``nombre, edad, total_ventas``, etc.)

Algunos nombres de variables siguiendo estas normas serian:

| ✅ VALIDO| ❌ INVALIDO|
|---|---|
| ``edad`` | ``1edad`` |
| ``nombre_completo`` | ``nombre-completo`` |
| ``_contador`` | ``if`` |

## Operadores

Son **simbolos especiales** que nos permiten **realizar operaciones** en **variables** y **valores**.

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

> *Los comentarios en verde indican el resultado que devuelve python*.

### Comparación

Operadores que se utilizan para comparar dos valores y devuelven un valor booleano (``True`` o ``False``), según el resultado de la comparación.

* Igual a ``==`` (==) : devuelve ``True`` si ambos valores son iguales.
* Diferente a ``!=`` (!=) : devuelve ``True`` si los valores son diferentes.
* Mayor que ``>`` : devuelve ``True`` si el primer valor es mayor que el segundo.
* Menor que ``<`` : devuelve ``True`` si el primer valor es menor que el segundo.
* Mayor o igual que ``>=`` (>=) : devuelve ``True`` si el primer valor es mayor o igual que el segundo.
* Menor o igual que ``<=`` (<=) : devuelve ``True`` si el primer valor es menor o igual que el segundo.

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

> *Los comentarios en verde indican el resultado que devuelve python*.

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

> *Los comentarios en verde indican el resultado que devuelve python*.

> *Python sigue las reglas de precedencia de operaciones, la procedencia es: **paréntesis, exponenciación, multiplicación/división, suma/resta, operadores de comparación y operadores lógicos***