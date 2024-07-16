from sqlalchemy.orm import relationship, validates, Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List, Optional

from .WorkforceManagement_base import WorkforceManagementBase

if TYPE_CHECKING:
    from .employee import Employee
    from .activity import Activity

class Schedule(WorkforceManagementBase):
    """ 
    """

    __tablename__ = 'Schedule'
    oid: Mapped[str] = mapped_column(primary_key=True)

    Employee_oid: Mapped[str] = mapped_column(ForeignKey("Employee.oid"))
    Employee: Mapped["Employee"] = relationship("Employee")
    Activity: Mapped[List["Activity"]] = relationship("Activity")

    @validates('Activity_oid')
    def validate_Activity_oid(self, key, Activity_oid):
        if len(self.Activity) < 0:
            raise ValueError("Number of related instances from Schedule to Activity must be between 0 and -1.")
        return Activity_oid
