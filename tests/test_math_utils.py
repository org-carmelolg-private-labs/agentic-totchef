"""
Unit tests for lib.commons.MathUtils.
"""

import pytest
from lib.commons.MathUtils import cosine_similarity


class TestCosineSimiliarity:
    def test_identical_vectors(self):
        a = [1.0, 0.0, 0.0]
        b = [1.0, 0.0, 0.0]
        assert cosine_similarity(a, b) == pytest.approx(1.0)

    def test_orthogonal_vectors(self):
        a = [1.0, 0.0]
        b = [0.0, 1.0]
        assert cosine_similarity(a, b) == pytest.approx(0.0)

    def test_opposite_vectors(self):
        a = [1.0, 0.0]
        b = [-1.0, 0.0]
        assert cosine_similarity(a, b) == pytest.approx(-1.0)

    def test_known_similarity(self):
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        assert cosine_similarity(a, b) == pytest.approx(0.9746318461970762)

    def test_zero_vector_raises(self):
        with pytest.raises(ZeroDivisionError):
            cosine_similarity([0.0, 0.0], [1.0, 2.0])
