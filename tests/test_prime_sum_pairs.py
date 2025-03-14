import pytest
from src.prime_sum_pairs import unique_prime_sum_pairs, is_prime

def test_is_prime():
    """Test the is_prime helper function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False

def test_unique_prime_sum_pairs_basic():
    """Test basic functionality of prime sum pairs generator."""
    assert unique_prime_sum_pairs(2) == [3, 5]
    assert unique_prime_sum_pairs(4) == [3, 5, 7]

def test_unique_prime_sum_pairs_edge_cases():
    """Test edge cases of prime sum pairs generator."""
    assert unique_prime_sum_pairs(1) == [2]
    
    with pytest.raises(ValueError):
        unique_prime_sum_pairs(0)
    
    with pytest.raises(ValueError):
        unique_prime_sum_pairs(-1)

def test_unique_prime_sum_pairs_order():
    """Ensure the returned list is sorted and unique."""
    result = unique_prime_sum_pairs(10)
    assert result == sorted(set(result))

def test_unique_prime_sum_pairs_comprehensiveness():
    """Test the comprehensiveness of prime sum generation."""
    result = unique_prime_sum_pairs(10)
    # Some known expectations
    expected_primes = [2, 3, 5, 7, 11, 13]
    for prime in expected_primes:
        assert prime in result