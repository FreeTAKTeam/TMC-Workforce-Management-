from sqlalchemy.orm import relationship, validates, Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List, Optional

from .WorkforceManagement_base import WorkforceManagementBase

if TYPE_CHECKING:
    pass

class Error(WorkforceManagementBase):
    """ "Error"
    """

    __tablename__ = 'Error'
    oid: Mapped[str] = mapped_column(primary_key=True)


