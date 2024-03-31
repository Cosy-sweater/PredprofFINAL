import unittest
from request_api import vvod


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_one_symbol(self):
        self.assertEqual(len(reverse('a')), 1)

    def test_palindrom(self):
        self.assertEqual(reverse("aboba"), "aboba")

    def test_simple(self):
        self.assertEqual(reverse("pohru"), "urhop")

    def test_noniterable(self):
        with self.assertRaises(TypeError):
            reverse(22)

    def test_iterable(self):
        with self.assertRaises(TypeError):
            reverse([42, "asas", "bnm<>"])


if __name__ == '__main__':
    unittest.main()
