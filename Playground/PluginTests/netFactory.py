"""Factory for creating a Neural Network."""

from NNBase import NNBase
from typing import Any, Callable

#from game.character import GameCharacter

NN_creation_funcs: dict[str, Callable[..., NNBase]] = {}

def register(NN_type: str, NN_fn: Callable[..., NNBase]) -> None:
    """Register a new game character type."""
    NN_creation_funcs[NN_type] = NN_fn


def unregister(NN_type: str) -> None:
    """Unregister a game character type."""
    NN_creation_funcs.pop(NN_type, None)


def create(arguments: dict[str, Any]) -> NNBase:
    """Create a game character of a specific type, given JSON data."""
    args_copy = arguments.copy()
    NN_type = args_copy.pop("type")
    try:
        creator_func = NN_creation_funcs[NN_type]
    except KeyError:
        raise ValueError(f"unknown neaural network type {NN_type!r}") from None
    return creator_func(**args_copy)
