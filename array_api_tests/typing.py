from typing import Tuple, Type, Union, Any

__all__ = [
    "DataType",
    "ScalarType",
    "Shape",
    "Param",
]

DataType = Type[Any]
ScalarType = Union[Type[bool], Type[int], Type[float]]
Shape = Tuple[int, ...]
Param = Tuple