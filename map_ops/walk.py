from typing import Any, Callable


__all__ = ["walk"]


def walk(
    d1: dict,
    d2: dict,
    initializer: Callable[[dict, dict], dict] = None,
    on_missing: Callable[[Any], Any] = None,
    on_match: Callable[[Any, Any], Any] = None,
    on_mismatch: Callable[[Any, Any], Any] = None,
    list_strategy: Callable[[Any, Any], Any] = None,
) -> dict:
    """Generalized function for pairwise traversal of dicts
    Args:
        d1: A Python dict
        d1: Python dict
        initializer: A Callable to tell `walk` what to
            compare `d1` to while traversing
        on_missing: A Callable to tell `walk` how to handle
            a key present in `d1` but not `d2`
        on_match: A Callable to tell `walk` how to
            handle same keys with differing values
        on_mismatch: A Callable to tell `walk` how to
            handle same keys with differing types
        list_strategy: A Callable to tell `walk` how to
            handle any lists it encounters

    Returns:
        A Python dict
    """
    if not initializer:
        initializer = lambda x, _: x

    output = initializer(d1, d2)

    for k, v in d1.items():
        try:
            res = None

            if k not in d2:
                if not on_missing:
                    output[k] = v
                else:
                    # allow ANY falsy values
                    output[k] = on_missing(v)

            elif type(v) != type(d2[k]):
                if not on_mismatch:
                    pass
                else:
                    output[k] = on_mismatch(v, d2[k])

            elif isinstance(v, dict):
                res = walk(
                    d1=v,  # type: ignore
                    d2=d2[k],  # type: ignore
                    initializer=initializer,
                    on_missing=on_missing,
                    on_match=on_match,
                    on_mismatch=on_mismatch,
                    list_strategy=list_strategy,
                )
                if res:
                    output[k] = res

            elif isinstance(v, (set, list, tuple)):
                if not list_strategy:
                    output[k] = v
                else:
                    # allow ONLY [] falsy value
                    _res = list_strategy(v, d2[k])
                    if _res is None:
                        pass
                    else:
                        output[k] = _res

            else:
                if on_match:
                    output[k] = on_match(v, d2[k])

        except Exception as e:
            e.args = (k, e.args)
            raise e

    return output
