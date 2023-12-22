from typing import TypeVar, Union

# AnyStr = TypeVar('AnyStr', str, bytes)
#
# def longest(first: AnyStr, second: AnyStr) -> AnyStr:
#     return first if len(first) >= len(second) else second
#
# result = longest('a', 'abc')  # The inferred type for result is str
# print(result)
# result = longest('a', b'abc')  # Fails static type check
# print(result)


U = Union[str, bytes]

# U = TypeVar('U',str,bytes)
def longest(first: U, second: U) -> U:
    # return first if len(first) >= len(second) else second
    return first + second



result = longest(b'a', b'abc')
print(type(result))
