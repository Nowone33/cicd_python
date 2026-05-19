#!/usr/bin/env python3
"""Point d'entrée de l'application."""

from calculs.core import additionner, soustraire, multiplier


def main():
    print("=== Application de Calculs ===")
    print(f"2 + 3 = {additionner(2, 3)}")
    print(f"10 - 4 = {soustraire(10, 4)}")
    print(f"1 - 4 = {soustraire(1, 4)}")
    print(f"3 × 4 = {multiplier(3, 4)}")


if __name__ == "__main__":
    main()
