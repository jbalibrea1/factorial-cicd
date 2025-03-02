""" Calcula el factorial de un número entero no negativo.
Args:
    n (int): Número entero no negativo.
"""


def factorial(n):
    """Calcula el factorial de un número entero no negativo.
    Args:
        n (int): Número entero no negativo.
    Returns:
        int: Factorial de n.
    Raises:
        ValueError: Si n no es un entero no negativo.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo")
    if n in (0, 1):
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
