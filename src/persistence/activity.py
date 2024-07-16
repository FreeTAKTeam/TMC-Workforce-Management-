from sqlalchemy.orm import relationship, validates, Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List, Optional

from .WorkforceManagement_base import WorkforceManagementBase

if TYPE_CHECKING:
    from .money import Money
    from .schedule import Schedule

class Activity(WorkforceManagementBase):
    """ 
    """

    __tablename__ = 'Activity'
    oid: Mapped[str] = mapped_column(primary_key=True)
    activityNr: Mapped[str]
    name: Mapped[str]
    status: Mapped[str]
    input: Mapped[str]
    output: Mapped[str]
    plannedStart: Mapped[str]
    plannedEnd: Mapped[str]
    plannedTenure: Mapped[str]
    ActivityDoneFor: Mapped[str]

    ActualCost_oid: Mapped[str] = mapped_column(ForeignKey("Money.oid"))
    ActualCost: Mapped["Money"] = relationship("Money")
    Schedule_oid: Mapped[Optional[str]] = mapped_column(ForeignKey("Schedule.oid"))

