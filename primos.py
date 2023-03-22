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
