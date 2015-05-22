from collections import OrderedDict
from itertools import chain

from frozendict import frozendict


class FrozenOrderedDict(frozendict):

    def __init__(self, *args):
        self.__dict = OrderedDict(*args)
        self.__hash = None

    def copy(self, *add_or_replace_items):
        return self.__class__(*(chain(self.iteritems(), add_or_replace_items)))

    def __repr__(self):
        return '<{} {!r}>'.format(self.__class__.__name__, self.__dict)
