from typing import Union
from digitalpy.core.domain.builder import Builder
from digitalpy.core.serialization.configuration.serialization_constants import Protocols
from digitalpy.core.domain.object_id import ObjectId


from components.WorkforceManagement.configuration.WorkforceManagement_constants import REGION

# import domain model classes
from components.WorkforceManagement.domain.model.region import Region
from components.WorkforceManagement.domain.model.employee import Employee
from components.WorkforceManagement.domain.model.schedule import Schedule
from components.WorkforceManagement.domain.model.activity import Activity
from components.WorkforceManagement.domain.model.money import Money

from components.WorkforceManagement.persistence.region import Region as DBRegion
from components.WorkforceManagement.persistence.employee import Employee as DBEmployee
from components.WorkforceManagement.persistence.schedule import Schedule as DBSchedule
from components.WorkforceManagement.persistence.activity import Activity as DBActivity
from components.WorkforceManagement.persistence.money import Money as DBMoney

class RegionBuilder(Builder):
    """Builds a Region object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result: Region = None  # type: ignore

    def build_empty_object(self, config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Builds a Region object"""
        self.request.set_value("object_class_name", "Region")

        configuration = config_loader.find_configuration(REGION)

        self.result = super()._create_model_object(
          configuration, extended_domain={"Region": Region,
                                            "Employee": Employee,
                                            "Schedule": Schedule,
                                            "Activity": Activity,
                                            "Money": Money,
                                        })

    def add_object_data(self, mapped_object: Union[bytes, str, DBRegion], protocol=None):
        """adds the data from the mapped object to the Health object """
        if protocol == Protocols.JSON and isinstance(mapped_object, bytes):
            self._add_json_object_data(mapped_object)

        elif isinstance(mapped_object, DBRegion):
            self._add_db_object_data(mapped_object)

    def _add_json_object_data(self, json_object: bytes):
        """adds the data from the json object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", json_object)
        self.request.set_value("protocol", Protocols.JSON)
        self.execute_sub_action("deserialize")

    def _add_db_object_data(self, db_object: DBRegion):
        """adds the data from the db object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", db_object)
        self.result.oid = db_object.oid
        self.result.RegionID = db_object.RegionID
        self.result.RegionName = db_object.RegionName
    def get_result(self):
        """gets the result of the builder"""
        return self.result
