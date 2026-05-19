"""Tests unitaires pour le module de calculs."""

import pytest
from calculs.core import additionner, soustraire, multiplier


class TestAdditionner:
    def test_entiers(self):
        assert additionner(2, 3) == 5

    def test_flottants(self):
        assert additionner(0.1, 0.2) == pytest.approx(0.3, rel=1e-7)


class TestSoustraire:
    def test_resultat(self):
        assert soustraire(10, 4) == 6


class TestMultiplier:
    def test_entiers(self):
        assert multiplier(3, 4) == 12

    def test_type_incorrect(self):
        with pytest.raises(TypeError):
            multiplier("5", 2)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
