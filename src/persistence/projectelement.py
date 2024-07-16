from sqlalchemy.orm import relationship, validates, Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List, Optional

from .WorkforceManagement_base import WorkforceManagementBase

if TYPE_CHECKING:
    pass

class ProjectElement(WorkforceManagementBase):
    """ 
    """

    __tablename__ = 'ProjectElement'
    oid: Mapped[str] = mapped_column(primary_key=True)
    plannedDuration: Mapped[str]
    actualDuration: Mapped[str]
    currentDuration: Mapped[str]
    status: Mapped[str]
    priority: Mapped[str]
    timingConstraint: Mapped[str]


