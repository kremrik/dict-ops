from typing import Any, Callable


__all__ = ["walk"]


def walk(
    d1: dict,
    d2: dict,
    initializer: Callable[[dict, dict], dict] = None,
    on_missing: Callable[[Any], Any] = None,
    on_match: Callable[[Any, Any], Any] = None,
    list_strategy: Callable[[Any, Any], Any] = None,
) -> dict:
    """Generalized function for pairwise traversal of dicts
    Args:
        d1: A Python dict
        d1: Python dict
        initializer: A Callable to tell `walk` what to
            compare `d1` to while traversing
        on_match: A Callable to tell `walk` how to
            handle same keys with differing values
        list_strategy: A Callable to tell `walk` how to
            handle any lists it encounters

    Returns:
        A Python dict
    """
    if not initializer:
        initializer = lambda x, y: x
    if not on_missing:
        on_missing = lambda x: x
    if not on_match:
        on_match = lambda x, y: None
    if not list_strategy:
        list_strategy = lambda x, y: x

    output = initializer(d1, d2)

    for k, v in d1.items():
        res = None

        if k not in d2:
            res = on_missing(v)

        elif isinstance(v, dict):
            res = walk(
                v,  # type: ignore
                d2[k],  # type: ignore
                initializer,
                on_missing,
                on_match,
                list_strategy,
            )

        elif isinstance(v, (set, list, tuple)):
            res = list_strategy(v, d2[k])

        else:
            res = on_match(v, d2[k])

        if res:
            output[k] = res

    return output
