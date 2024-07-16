# pylint: disable=invalid-name
from digitalpy.core.domain.node import Node
from digitalpy.core.domain.relationship import Relationship, RelationshipType

from typing import TYPE_CHECKING
# iterating associations
# found association
if TYPE_CHECKING:
    from .money import Money

class Activity(Node):
    """"""
    def __init__(self, model_configuration, model, oid=None, node_type="Activity") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)
        self._activityNr: 'str' = None
        self._name: 'str' = None
        self._status: 'str' = None
        self._input: 'str' = None
        self._output: 'str' = None
        self._plannedStart: 'str' = None
        self._plannedEnd: 'str' = None
        self._plannedTenure: 'str' = None
        self._ActivityDoneFor: 'str' = None
        self._ActualCost: str = ""

    @property
    def activityNr(self) -> 'str':
        """"""
        return self._activityNr

    @activityNr.setter
    def activityNr(self, activityNr: 'str'):
        activityNr = str(activityNr)
        if not isinstance(activityNr, str):
            raise TypeError("'activityNr' must be of type str")
        self._activityNr= activityNr

    @property
    def name(self) -> 'str':
        """"""
        return self._name

    @name.setter
    def name(self, name: 'str'):
        name = str(name)
        if not isinstance(name, str):
            raise TypeError("'name' must be of type str")
        self._name= name

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
    def input(self) -> 'str':
        """"""
        return self._input

    @input.setter
    def input(self, input: 'str'):
        input = str(input)
        if not isinstance(input, str):
            raise TypeError("'input' must be of type str")
        self._input= input

    @property
    def output(self) -> 'str':
        """"""
        return self._output

    @output.setter
    def output(self, output: 'str'):
        output = str(output)
        if not isinstance(output, str):
            raise TypeError("'output' must be of type str")
        self._output= output

    @property
    def plannedStart(self) -> 'str':
        """"""
        return self._plannedStart

    @plannedStart.setter
    def plannedStart(self, plannedStart: 'str'):
        plannedStart = str(plannedStart)
        if not isinstance(plannedStart, str):
            raise TypeError("'plannedStart' must be of type str")
        self._plannedStart= plannedStart

    @property
    def plannedEnd(self) -> 'str':
        """"""
        return self._plannedEnd

    @plannedEnd.setter
    def plannedEnd(self, plannedEnd: 'str'):
        plannedEnd = str(plannedEnd)
        if not isinstance(plannedEnd, str):
            raise TypeError("'plannedEnd' must be of type str")
        self._plannedEnd= plannedEnd

    @property
    def plannedTenure(self) -> 'str':
        """"""
        return self._plannedTenure

    @plannedTenure.setter
    def plannedTenure(self, plannedTenure: 'str'):
        plannedTenure = str(plannedTenure)
        if not isinstance(plannedTenure, str):
            raise TypeError("'plannedTenure' must be of type str")
        self._plannedTenure= plannedTenure

    @property
    def ActivityDoneFor(self) -> 'str':
        """"""
        return self._ActivityDoneFor

    @ActivityDoneFor.setter
    def ActivityDoneFor(self, ActivityDoneFor: 'str'):
        ActivityDoneFor = str(ActivityDoneFor)
        if not isinstance(ActivityDoneFor, str):
            raise TypeError("'ActivityDoneFor' must be of type str")
        self._ActivityDoneFor= ActivityDoneFor

    @property
    def ActualCost(self) -> 'str': # type: ignore
        """"""
        return self._ActualCost

    @ActualCost.setter
    def ActualCost(self, ActualCost: 'str'):
        self._ActualCost = ActualCost
