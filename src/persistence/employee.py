from sqlalchemy.orm import relationship, validates, Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List, Optional

from .WorkforceManagement_base import WorkforceManagementBase

if TYPE_CHECKING:
    from .region import Region
    from .schedule import Schedule

class Employee(WorkforceManagementBase):
    """ 
    """

    __tablename__ = 'Employee'
    oid: Mapped[str] = mapped_column(primary_key=True)
    EmplNumber: Mapped[float]
    LastName: Mapped[str]
    FirstName: Mapped[str]
    MiddleName: Mapped[str]
    isManager: Mapped[str]
    RegionID: Mapped[float]
    EmplStreet1: Mapped[str]
    EmplStreet2: Mapped[str]
    EmplPostalCode: Mapped[str]
    EmplCity: Mapped[str]
    EmplSalary: Mapped[str]

    Responsiblefor_oid: Mapped[str] = mapped_column(ForeignKey("Region.oid"))
    Responsiblefor: Mapped["Region"] = relationship("Region")

