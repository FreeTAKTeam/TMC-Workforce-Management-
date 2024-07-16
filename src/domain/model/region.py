# pylint: disable=invalid-name
from digitalpy.core.domain.node import Node
from digitalpy.core.domain.relationship import Relationship, RelationshipType

from typing import TYPE_CHECKING
# iterating associations

class Region(Node):
    """"""
    def __init__(self, model_configuration, model, oid=None, node_type="Region") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)
        self._RegionID: 'float' = None
        self._RegionName: 'str' = None

    @property
    def RegionID(self) -> 'float':
        """"""
        return self._RegionID

    @RegionID.setter
    def RegionID(self, RegionID: 'float'):
        RegionID = float(RegionID)
        if not isinstance(RegionID, float):
            raise TypeError("'RegionID' must be of type float")
        self._RegionID= RegionID

    @property
    def RegionName(self) -> 'str':
        """"""
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName: 'str'):
        RegionName = str(RegionName)
        if not isinstance(RegionName, str):
            raise TypeError("'RegionName' must be of type str")
        self._RegionName= RegionName
