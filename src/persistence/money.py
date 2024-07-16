from sqlalchemy.orm import relationship, validates, Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List, Optional

from .WorkforceManagement_base import WorkforceManagementBase

if TYPE_CHECKING:
    from .activity import Activity

class Money(WorkforceManagementBase):
    """ 
    """

    __tablename__ = 'Money'
    oid: Mapped[str] = mapped_column(primary_key=True)
    unit: Mapped[str]
    value: Mapped[str]


