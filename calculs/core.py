"""Module de calculs mathématiques simples."""


def additionner(a: float, b: float) -> float:
    """
    Calcule la somme de deux nombres.

    Args:
        a: Premier nombre.
        b: Deuxième nombre.

    Returns:
        La somme de a et b.

    Examples:
        >>> additionner(2, 3)
        5
        >>> additionner(-1, 1)
        0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")
    return a + b


def soustraire(a: float, b: float) -> float:
    """
    Calcule la différence entre deux nombres.

    Args:
        a: Le nombre à partir duquel on soustrait.
        b: Le nombre à soustraire.

    Returns:
        Le résultat de a - b.

    Examples:
        >>> soustraire(10, 4)
        6
        >>> soustraire(5, 5)
        0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")
    if b > a:
        raise ArithmeticError("Impossible d'avoir un résultat négatif")
    return a - b


def multiplier(a: float, b: float) -> float:
    """
    Calcule le produit de deux nombres.

    Args:
        a: Premier facteur.
        b: Deuxième facteur.

    Returns:
        Le produit de a et b.

    Raises:
        TypeError: Si a ou b ne sont pas des nombres.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")
    return a * b


def diviser(a: float, b: float) -> float:
    """
    Calcule le quotient de deux nombres.

    Args:
        a: Le dividende.
        b: Le diviseur.

    Returns:
        Le résultat de a / b.

    Raises:
        TypeError: Si a ou b ne sont pas des nombres.
        ZeroDivisionError: Si b est égal à zéro.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")
    if b == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro")
    return a / b
