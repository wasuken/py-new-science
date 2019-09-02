import unittest
import practice1 as pt
from functools  import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

class TestPractice1(unittest.TestCase):
    """test class of practice1.py
    """

    def test_fib(self):
        """test method for tashizan
        """
        value1 = 2
        value2 = 6
        expected = fib(50)
        actual = pt.fib(50)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
