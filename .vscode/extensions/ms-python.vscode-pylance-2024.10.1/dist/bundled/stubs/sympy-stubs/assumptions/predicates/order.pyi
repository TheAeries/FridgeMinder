from typing_extensions import LiteralString

from sympy.assumptions import Predicate
from sympy.multipledispatch import Dispatcher

class NegativePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class NonNegativePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class NonZeroPredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class ZeroPredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class NonPositivePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class PositivePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class ExtendedPositivePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class ExtendedNegativePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class ExtendedNonZeroPredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class ExtendedNonPositivePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...

class ExtendedNonNegativePredicate(Predicate):
    name: LiteralString = ...
    handler: Dispatcher = ...
