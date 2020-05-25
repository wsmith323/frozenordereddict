
from collections import Mapping

try:
    reduce
except NameError:
    from functools import reduce

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import operator
import os

with open(os.path.join(os.path.dirname(__file__), 'VERSION.txt')) as f:
    __version__ = f.read().strip()


class FrozenOrderedDict(Mapping):
    """
    Frozen OrderedDict.
    """

    def __init__(self, *args, **kwargs):
        self.__dict = OrderedDict(*args, **kwargs)
        self.__hash = None

    def __getitem__(self, item):
        return self.__dict[item]

    def __iter__(self):
        return iter(self.__dict)

    def __len__(self):
        return len(self.__dict)

    def __hash__(self):
        if self.__hash is None:
            self.__hash = reduce(operator.xor, map(hash, self.__dict.items()), 0)

        return self.__hash

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self.__dict.items())

    def copy(self, *args, **kwargs):
        new_dict = self.__dict.copy()

        if args or kwargs:
            new_dict.update(OrderedDict(*args, **kwargs))

        return self.__class__(new_dict)
