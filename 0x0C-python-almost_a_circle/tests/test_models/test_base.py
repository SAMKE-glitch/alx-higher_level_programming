#!/usr/bin/python3
"""A module defining unittest for test base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defining TestBase class"""

    def test_id_with_argument(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_id_without_argument(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_id_bool(self):
        obj = Base(True)
        self.assertEqual(obj.id, True)

    def test_id_range(self):
        obj = Base(range(5))
        self.assertEqual(obj.id, range(5))

    def test_id_bytes(self):
        obj = Base(b'hello')
        self.assertEqual(obj.id, b'hello')

    def test_id_frozenset(self):
        obj = Base(frozenset({1, 2, 3}))
        self.assertEqual(obj.id, frozenset({1, 2, 3}))

    def test_id_str(self):
        obj = Base('example')
        self.assertEqual(obj.id, 'example')

    def test_id_two_args(self):
        obj = Base((10, 20))
        self.assertEqual(obj.id, (10, 20))

    def test_id_NaN(self):
        obj = Base(float('nan'))

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_nb_instances_priv(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_None_id(self):
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_id_inf(self):
        obj = Base(float('inf'))
        self.assertEqual(obj.id, float('inf'))

    def test_id_set(self):
        obj = Base({1, 2, 3})
        self.assertEqual(obj.id, {1, 2, 3})

    def test_id_dict(self):
        obj = Base({1: 'one', 2: 'two'})
        self.assertEqual(obj.id, {1: 'one', 2: 'two'})

    def test_id_unique(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.id, obj3.id)
        self.assertNotEqual(obj2.id, obj3.id)


if __name__ == '__main__':
    unittest.main()
