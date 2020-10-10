from map_ops.walk import walk
from copy import deepcopy
from typing import Any, Callable


__all__ = ["cut_", "diff_", "put_"]


def diff_(
    d1: dict,
    d2: dict,
    on_missing: Callable[[Any], Any] = None,
    on_match: Callable[[Any, Any], Any] = None,
    list_strategy: Callable[[Any, Any], Any] = None,
) -> dict:
    """Generalized function for differencing two dicts

    Args:
        d1: A Python dict
        d1: Python dict
        on_missing: A Callable to tell `walk` how to handle
            a key present in `d1` but not `d2`
        on_match: A Callable to tell `walk` how to
            handle same keys with differing values
        list_strategy: A Callable to tell `walk` how to
            handle any lists it encounters

    Returns:
        A Python dict
    """
    d1 = deepcopy(d1)
    return walk(
        d1,
        d2,
        initializer=lambda x, y: {},
        on_missing=on_missing,
        on_match=on_match,
        list_strategy=list_strategy,
    )


def put_(
    d1: dict,
    d2: dict,
    on_missing: Callable[[Any], Any] = None,
    on_match: Callable[[Any, Any], Any] = None,
    list_strategy: Callable[[Any, Any], Any] = None,
) -> dict:
    """Generalized function for inserting `d1` into `d2`

    Args:
        d1: A Python dict
        d1: Python dict
        on_missing: A Callable to tell `walk` how to handle
            a key present in `d1` but not `d2`
        on_match: A Callable to tell `walk` how to
            handle same keys with differing values
        list_strategy: A Callable to tell `walk` how to
            handle any lists it encounters

    Returns:
        A Python dict
    """
    # prevents a key existing in both sides from being
    # overwritten by the value from the left side
    if not on_match:
        on_match = lambda x, y: y

    d2 = deepcopy(d2)
    return walk(
        d1,
        d2,
        initializer=lambda x, y: y,
        on_missing=on_missing,
        on_match=on_match,
        list_strategy=list_strategy,
    )


def cut_(
    d1: dict,
    d2: dict,
    on_missing: Callable[[Any], Any] = None,
    on_match: Callable[[Any, Any], Any] = None,
    list_strategy: Callable[[Any, Any], Any] = None,
) -> dict:
    """Generalized function for removing `d1` from `d2`

    Args:
        d1: A Python dict
        d1: Python dict
        on_missing: A Callable to tell `walk` how to handle
            a key present in `d1` but not `d2`
        on_match: A Callable to tell `walk` how to
            handle same keys with differing values
        list_strategy: A Callable to tell `walk` how to
            handle any lists it encounters

    Returns:
        A Python dict
    """
    d2 = deepcopy(d2)
    return walk(
        d2,
        d1,
        initializer=lambda x, y: {},
        on_missing=on_missing,
        on_match=on_match,
        list_strategy=list_strategy,
    )
