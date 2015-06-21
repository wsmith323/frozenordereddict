FrozenOrderedDict
=================

An immutable wrapper around an OrderedDict.

FrozenOrderedDict was inspired by https://pypi.python.org/pypi/frozendict/
(and borrows some code from it). With regards to immutability, it
solves the same problems:

  - Because dictionaries are mutable, they are not hashable and
    cannot be used in sets or as dictionary keys.
  - Nasty bugs can and do occur when mutable data structures are
    passed around.

It can be initialized just like a dict or OrderedDict. However, be
advised that just like with OrderedDict, keyword arguments are not
recommended since their insertion order is arbitrary.

Once instantiated, an instance of FrozenOrderedDict cannot be altered,
since it does not implement the MutableMapping interface.

It does implement the Mapping interface, so can be used just like a
normal dictionary in most cases.

In order to modify the contents of a FrozenOrderedDict, a new
instance must be created. The easiest way to do that is by
calling the `.copy()` method. It will return a new instance of
FrozenOrderedDict initialized using the following steps:

  1. A copy of the wrapped OrderedDict instance will be created.
  2. If any arguments or keyword arguments are passed to the `.copy()`
     method, they will be used to create another OrderedDict
     instance, which will then be used to update the copy made in
     step #1.
  3. Finally, `self.__class__()` will be called, passing the copy as
     the only argument.
