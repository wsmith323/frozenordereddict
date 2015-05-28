from collections import OrderedDict
from unittest import TestCase

from frozenordereddict import FrozenOrderedDict


class TestFrozenOrderedDict(TestCase):
    ITEMS_1 = (
        ("b", 2),
        ("a", 1),
    )
    ITEMS_2 = (
        ("d", 4),
        ("c", 3),
    )

    ODICT_1 = OrderedDict(ITEMS_1)
    ODICT_2 = OrderedDict(ITEMS_2)

    def test_init_from_items(self):
        fod = FrozenOrderedDict(self.ITEMS_1)
        self.assertEqual(list(self.ITEMS_1), fod.items())

    def test_init_from_ordereddict(self):
        fod = FrozenOrderedDict(self.ODICT_1)
        self.assertEqual(list(self.ITEMS_1), fod.items())

    def test_setitem(self):
        def doit():
            fod = FrozenOrderedDict()
            fod[1] = "b"

        self.assertRaises(TypeError, doit)

    def test_delitem(self):
        def doit():
            fod = FrozenOrderedDict(self.ITEMS_1)
            del fod[1]

        self.assertRaises(TypeError, doit)

    def test_copy_no_items(self):
        fod1 = FrozenOrderedDict(self.ITEMS_1)
        fod2 = fod1.copy()

        self.assertNotEqual(id(fod1), id(fod2))
        self.assertEqual(fod1.items(), fod2.items())
        self.assertEqual(repr(fod1), repr(fod2))
        self.assertEqual(len(fod1), len(fod2))
        self.assertEqual(hash(fod1), hash(fod2))

    def test_copy_tuple_items(self):
        fod1 = FrozenOrderedDict(self.ITEMS_1)
        fod2 = fod1.copy(self.ITEMS_2)

        self.assertNotEqual(id(fod1), id(fod2))
        self.assertEqual(fod1.items() + list(self.ITEMS_2), fod2.items())

    def test_copy_ordereddict_items(self):
        fod1 = FrozenOrderedDict(self.ITEMS_1)
        fod2 = fod1.copy(self.ODICT_2)

        self.assertNotEqual(id(fod1), id(fod2))
        self.assertEqual(fod1.items() + list(self.ITEMS_2), fod2.items())

    def test_copy_kwargs(self):
        fod1 = FrozenOrderedDict(self.ITEMS_1)
        fod2 = fod1.copy(**self.ODICT_2)

        self.assertNotEqual(id(fod1), id(fod2))
        self.assertEqual(dict(fod1.items() + self.ODICT_2.items()), fod2)





