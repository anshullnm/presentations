# -*- coding: utf-8 -*-
import unittest


def sorted_ci(words):
    return sorted(words, key=lambda x: x.lower)


def sorted_numbers(numbers):
    return sorted_ci([str(num) for num in numbers])


class Test(unittest.TestCase):

    def test_basic(self):
        assert (sorted_ci(['apple', 'Orange'])
                == ['apple', 'Orange'])

    def test_zero(self):
        1/0

    def test_failure(self):
        assert 1 == 0

    def test_not_strings(self):
        self.assertRaises(AttributeError,
                          sorted_ci, [4, 5])

    def test_unicode(self):
        utf8_str = u'বাংলা'.encode('utf-8')
        assert (sorted_ci([utf8_str, 'Orange'])
                == ['Orange', utf8_str])


if __name__ == '__main__':
    unittest.main()
