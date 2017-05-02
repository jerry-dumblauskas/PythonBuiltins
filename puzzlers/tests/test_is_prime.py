from unittest import TestCase
import puzzlers.prime_numbers


class TestIsPrime(TestCase):
    def test_is_prime_base(self):
        self.assertTrue(puzzlers.prime_numbers.is_prime(99))

    def test_is_prime_no_base(self):
        self.assertFalse(puzzlers.prime_numbers.is_prime(17))

    def test_is_prime_neg(self):
        with self.assertRaises(Exception):
            self.assertFalse(puzzlers.prime_numbers.is_prime(-99))

    def test_is_prime_general(self):
        self.assertTrue(puzzlers.prime_numbers.is_prime(117))

    def test_is_prime_not_number(self):
        with self.assertRaises(Exception):
            self.assertFalse(puzzlers.prime_numbers.is_prime("A"))
