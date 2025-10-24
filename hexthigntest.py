import pytest
import hexthign

def test_to_decimal():
    assert hexthign.to_decimal('1A', 16) == 26
    assert hexthign.to_decimal('FF', 16) == 255
    assert hexthign.to_decimal('0', 16) == 0
    assert hexthign.to_decimal('7B', 16) == 123
    assert hexthign.to_decimal('100', 16) == 256
    assert hexthign.to_decimal('Z', 36) == 35

def test_from_decimal():
    assert hexthign.from_decimal(26, 16) == '1A'
    assert hexthign.from_decimal(255, 16) == 'FF'
    assert hexthign.from_decimal(123, 16) == '7B'
    assert hexthign.from_decimal(256, 16) == '100'
    assert hexthign.from_decimal(35, 36) == 'Z'