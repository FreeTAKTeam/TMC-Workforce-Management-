# pylint: disable=invalid-name
from digitalpy.core.domain.node import Node
from digitalpy.core.domain.relationship import Relationship, RelationshipType

from typing import TYPE_CHECKING
# iterating associations

class ProjectElement(Node):
    """"""
    def __init__(self, model_configuration, model, oid=None, node_type="ProjectElement") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)
        self._plannedDuration: 'str' = None
        self._actualDuration: 'str' = None
        self._currentDuration: 'str' = None
        self._status: 'str' = None
        self._priority: 'str' = None
        self._timingConstraint: 'str' = None

    @property
    def plannedDuration(self) -> 'str':
        """"""
        return self._plannedDuration

    @plannedDuration.setter
    def plannedDuration(self, plannedDuration: 'str'):
        plannedDuration = str(plannedDuration)
        if not isinstance(plannedDuration, str):
            raise TypeError("'plannedDuration' must be of type str")
        self._plannedDuration= plannedDuration

    @property
    def actualDuration(self) -> 'str':
        """"""
        return self._actualDuration

    @actualDuration.setter
    def actualDuration(self, actualDuration: 'str'):
        actualDuration = str(actualDuration)
        if not isinstance(actualDuration, str):
            raise TypeError("'actualDuration' must be of type str")
        self._actualDuration= actualDuration

    @property
    def currentDuration(self) -> 'str':
        """"""
        return self._currentDuration

    @currentDuration.setter
    def currentDuration(self, currentDuration: 'str'):
        currentDuration = str(currentDuration)
        if not isinstance(currentDuration, str):
            raise TypeError("'currentDuration' must be of type str")
        self._currentDuration= currentDuration

    @property
    def status(self) -> 'str':
        """"""
        return self._status

    @status.setter
    def status(self, status: 'str'):
        status = str(status)
        if not isinstance(status, str):
            raise TypeError("'status' must be of type str")
        self._status= status

    @property
    def priority(self) -> 'str':
        """"""
        return self._priority

    @priority.setter
    def priority(self, priority: 'str'):
        priority = str(priority)
        if not isinstance(priority, str):
            raise TypeError("'priority' must be of type str")
        self._priority= priority

    @property
    def timingConstraint(self) -> 'str':
        """"""
        return self._timingConstraint

    @timingConstraint.setter
    def timingConstraint(self, timingConstraint: 'str'):
        timingConstraint = str(timingConstraint)
        if not isinstance(timingConstraint, str):
            raise TypeError("'timingConstraint' must be of type str")
        self._timingConstraint= timingConstraint
