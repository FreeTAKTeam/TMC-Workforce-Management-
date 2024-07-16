# pylint: disable=invalid-name
from digitalpy.core.domain.node import Node
from digitalpy.core.domain.relationship import Relationship, RelationshipType

from typing import TYPE_CHECKING
# iterating associations
# found association
if TYPE_CHECKING:
    from .employee import Employee
# found association
if TYPE_CHECKING:
    from .activity import Activity

class Schedule(Node):
    """"""
    def __init__(self, model_configuration, model, oid=None, node_type="Schedule") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)
        self._Employee: str = ""
        self._Activity: list[str] = []

    @property
    def Employee(self) -> 'str': # type: ignore
        """"""
        return self._Employee

    @Employee.setter
    def Employee(self, Employee: 'str'):
        self._Employee = Employee

    @property
    def Activity(self) -> list['str']: # type: ignore
        """"""
        return self._Activity

    @Activity.setter
    def Activity(self, Activity: 'str'):
        self._Activity = Activity
