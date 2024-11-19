from typing import Callable, Type
from task1.solution.solution import strict
import pytest


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def is_paliandrom(value: str) -> bool:
    value = value.lower()
    return value == value[::-1]


@pytest.mark.parametrize(
    'func,expected_error,args,kwargs',
    [
        (sum_two, None, [1, 3], {}),
        (sum_two, TypeError, [1, 3.6], {}),
        (is_paliandrom, None, [], {'value': 'Otto'}),
        (is_paliandrom, TypeError, [], {'value': 'Otto'.split()}),
    ]
)
def test_strict_annotation(func: Callable, expected_error: Type[Exception] | None, args: list, kwargs: dict):
    if expected_error:
        with pytest.raises(expected_error):
            func(*args, **kwargs)
    else:
        func(*args, **kwargs)
