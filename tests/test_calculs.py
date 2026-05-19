"""Tests unitaires pour le module de calculs."""

import pytest
from calculs.core import additionner, soustraire, multiplier, diviser


class TestAdditionner:
    def test_entiers(self):
        assert additionner(2, 3) == 5

    def test_flottants(self):
        assert additionner(0.1, 0.2) == pytest.approx(0.3, rel=1e-7)

    def test_failed_notNumber(self):
        with pytest.raises( TypeError): 
            additionner("pas un nombre", 0.2)


class TestSoustraire:
    def test_resultat(self):
        assert soustraire(10, 4) == 6

    def test_failed_notNumber(self):
        with pytest.raises( TypeError): 
            soustraire("pas un nombre", 0.2)

    def test_failed_negativ_result(self):
        with pytest.raises(ArithmeticError):
            soustraire(5,20)


class TestMultiplier:
    def test_entiers(self):
        assert multiplier(3, 4) == 12

    def test_type_incorrect(self):
        with pytest.raises(TypeError):
            multiplier("5", 2)


class TestDiviser:
    def test_entiers(self):
        assert diviser(20,5) == 4

    def test_type_incorrect(self):
        with pytest.raises(TypeError):
            diviser("5", 2)

    def test_failed_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            diviser(20,0)
    

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
