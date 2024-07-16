# pylint: disable=invalid-name
from digitalpy.core.domain.node import Node
from digitalpy.core.domain.relationship import Relationship, RelationshipType

from typing import TYPE_CHECKING
# iterating associations
# found association
if TYPE_CHECKING:
    from .region import Region

class Employee(Node):
    """"""
    def __init__(self, model_configuration, model, oid=None, node_type="Employee") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)
        self._EmplNumber: 'float' = None
        self._LastName: 'str' = None
        self._FirstName: 'str' = None
        self._MiddleName: 'str' = None
        self._isManager: 'str' = None
        self._RegionID: 'float' = None
        self._EmplStreet1: 'str' = None
        self._EmplStreet2: 'str' = None
        self._EmplPostalCode: 'str' = None
        self._EmplCity: 'str' = None
        self._EmplSalary: 'str' = None
        self._Responsiblefor: str = ""

    @property
    def EmplNumber(self) -> 'float':
        """"""
        return self._EmplNumber

    @EmplNumber.setter
    def EmplNumber(self, EmplNumber: 'float'):
        EmplNumber = float(EmplNumber)
        if not isinstance(EmplNumber, float):
            raise TypeError("'EmplNumber' must be of type float")
        self._EmplNumber= EmplNumber

    @property
    def LastName(self) -> 'str':
        """"""
        return self._LastName

    @LastName.setter
    def LastName(self, LastName: 'str'):
        LastName = str(LastName)
        if not isinstance(LastName, str):
            raise TypeError("'LastName' must be of type str")
        self._LastName= LastName

    @property
    def FirstName(self) -> 'str':
        """"""
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName: 'str'):
        FirstName = str(FirstName)
        if not isinstance(FirstName, str):
            raise TypeError("'FirstName' must be of type str")
        self._FirstName= FirstName

    @property
    def MiddleName(self) -> 'str':
        """"""
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName: 'str'):
        MiddleName = str(MiddleName)
        if not isinstance(MiddleName, str):
            raise TypeError("'MiddleName' must be of type str")
        self._MiddleName= MiddleName

    @property
    def isManager(self) -> 'str':
        """"""
        return self._isManager

    @isManager.setter
    def isManager(self, isManager: 'str'):
        isManager = str(isManager)
        if not isinstance(isManager, str):
            raise TypeError("'isManager' must be of type str")
        self._isManager= isManager

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
    def EmplStreet1(self) -> 'str':
        """"""
        return self._EmplStreet1

    @EmplStreet1.setter
    def EmplStreet1(self, EmplStreet1: 'str'):
        EmplStreet1 = str(EmplStreet1)
        if not isinstance(EmplStreet1, str):
            raise TypeError("'EmplStreet1' must be of type str")
        self._EmplStreet1= EmplStreet1

    @property
    def EmplStreet2(self) -> 'str':
        """"""
        return self._EmplStreet2

    @EmplStreet2.setter
    def EmplStreet2(self, EmplStreet2: 'str'):
        EmplStreet2 = str(EmplStreet2)
        if not isinstance(EmplStreet2, str):
            raise TypeError("'EmplStreet2' must be of type str")
        self._EmplStreet2= EmplStreet2

    @property
    def EmplPostalCode(self) -> 'str':
        """"""
        return self._EmplPostalCode

    @EmplPostalCode.setter
    def EmplPostalCode(self, EmplPostalCode: 'str'):
        EmplPostalCode = str(EmplPostalCode)
        if not isinstance(EmplPostalCode, str):
            raise TypeError("'EmplPostalCode' must be of type str")
        self._EmplPostalCode= EmplPostalCode

    @property
    def EmplCity(self) -> 'str':
        """"""
        return self._EmplCity

    @EmplCity.setter
    def EmplCity(self, EmplCity: 'str'):
        EmplCity = str(EmplCity)
        if not isinstance(EmplCity, str):
            raise TypeError("'EmplCity' must be of type str")
        self._EmplCity= EmplCity

    @property
    def EmplSalary(self) -> 'str':
        """"""
        return self._EmplSalary

    @EmplSalary.setter
    def EmplSalary(self, EmplSalary: 'str'):
        EmplSalary = str(EmplSalary)
        if not isinstance(EmplSalary, str):
            raise TypeError("'EmplSalary' must be of type str")
        self._EmplSalary= EmplSalary

    @property
    def Responsiblefor(self) -> 'str': # type: ignore
        """"""
        return self._Responsiblefor

    @Responsiblefor.setter
    def Responsiblefor(self, Responsiblefor: 'str'):
        self._Responsiblefor = Responsiblefor
