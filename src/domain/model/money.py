# pylint: disable=invalid-name
from digitalpy.core.domain.node import Node
from digitalpy.core.domain.relationship import Relationship, RelationshipType

from typing import TYPE_CHECKING
# iterating associations

class Money(Node):
    """"""
    def __init__(self, model_configuration, model, oid=None, node_type="Money") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)
        self._unit: 'str' = None
        self._value: 'str' = None

    @property
    def unit(self) -> 'str':
        """Currency (ISO4217 norm uses 3 letters to define the currency)"""
        return self._unit

    @unit.setter
    def unit(self, unit: 'str'):
        unit = str(unit)
        if not isinstance(unit, str):
            raise TypeError("'unit' must be of type str")
        self._unit= unit

    @property
    def value(self) -> 'str':
        """A signed floating point number, the meaning of the sign is according to the context of the API that uses this Data type"""
        return self._value

    @value.setter
    def value(self, value: 'str'):
        value = str(value)
        if not isinstance(value, str):
            raise TypeError("'value' must be of type str")
        self._value= value
