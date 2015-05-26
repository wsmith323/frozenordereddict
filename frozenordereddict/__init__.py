from collections import Mapping
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from itertools import chain
import operator


class FrozenOrderedDict(Mapping):
    """
    Frozen OrderedDict.
    """

    def __init__(self, items=()):
        self.__dict = OrderedDict(items)
        self.__hash = None

    def __getitem__(self, item):
        return self.__dict[item]

    def __iter__(self):
        return iter(self.__dict)

    def __len__(self):
        return len(self.__dict)

    def __hash__(self):
        if self.__hash is None:
            self.__hash = reduce(operator.xor, map(hash, self.iteritems()), 0)

        return self.__hash

    def __repr__(self):
        return '<{} {!r}>'.format(self.__class__.__name__, self.items())

    def copy(self, new_or_replacement_items=tuple()):
        if isinstance(new_or_replacement_items, Mapping):
            new_or_replacement_items = new_or_replacement_items.iteritems()

        return self.__class__(chain(self.iteritems(), new_or_replacement_items))
