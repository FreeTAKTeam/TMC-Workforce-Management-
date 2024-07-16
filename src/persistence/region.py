from sqlalchemy.orm import relationship, validates, Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List, Optional

from .WorkforceManagement_base import WorkforceManagementBase

if TYPE_CHECKING:
    from .employee import Employee

class Region(WorkforceManagementBase):
    """ 
    """

    __tablename__ = 'Region'
    oid: Mapped[str] = mapped_column(primary_key=True)
    RegionID: Mapped[float]
    RegionName: Mapped[str]


