# Segunda tarea de APA 2023: Manejo de números primos

## Nom i cognoms: Victor Ceballos Fouces

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.

##### Doctest Passed
![Doctest Passed](doctest_passed)

##### Doctest Failed
![Doctest Failed](doctest_failed)


Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.

```python
"""
Victor Ceballos Fouces

"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2,numero):
        if numero % prueba == 0: return False

    return True


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple([ prueba for prueba in range(2, numero) if esPrimo(prueba)])


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            factores.append(divisor)
            numero /= divisor
        else:
            divisor += 1
    return tuple(factores)


def mcm(numero1,numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(90, 14)
    630
    """
    # Obtenemos los factores primos de ambos números
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)

    # Combinamos todos los factores necesarios para el mcm
    todos_factores = set(factores1 + factores2)
    mcm = 1

    # Iterar sobre cada factor y calcular el máximo número de veces
    # que aparece en los factores primos de cada número
    for factor in todos_factores:
        veces1 = factores1.count(factor)
        veces2 = factores2.count(factor)
        mcm *= factor ** max(veces1, veces2)
        
    return mcm


def mcd(numero1,numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcd(924, 780)
    12
    """
    # Obtenemos los factores primos de ambos números
    factores_primos1 = descompon(numero1)
    factores_primos2 = descompon(numero2)
    
    # Identificamos los factores comunes más grandes
    mcd = 1
    for factor in factores_primos1:
        if factor in factores_primos2:
            mcd *= factor
    
    return mcd


def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    # Encontrar el máximo número en la lista
    max_num = max(numeros)

    # Inicializar la variable del MCM
    mcm = max_num

    # Encontrar el MCM
    while True:
        if all(mcm % num == 0 for num in numeros):
            return mcm
        else:
            mcm += max_num


def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcdN(820, 630, 1050, 1470)
    10
    """
    # Encontrar el mínimo número en la lista
    min_num = min(numeros)

    # Inicializar la variable del MCD
    mcd = 1

    # Encontrar el MCD
    for i in range(1, min_num + 1):
        if all(num % i == 0 for num in numeros):
            mcd = i

    return mcd



import doctest
doctest.testmod(verbose = True)
```

#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
