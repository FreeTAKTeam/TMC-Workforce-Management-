from typing import Union
from digitalpy.core.domain.builder import Builder
from digitalpy.core.serialization.configuration.serialization_constants import Protocols
from digitalpy.core.domain.object_id import ObjectId


from components.WorkforceManagement.configuration.WorkforceManagement_constants import ACTIVITY

# import domain model classes
from components.WorkforceManagement.domain.model.activity import Activity
from components.WorkforceManagement.domain.model.money import Money
from components.WorkforceManagement.domain.model.schedule import Schedule
from components.WorkforceManagement.domain.model.employee import Employee
from components.WorkforceManagement.domain.model.region import Region

from components.WorkforceManagement.persistence.activity import Activity as DBActivity
from components.WorkforceManagement.persistence.money import Money as DBMoney
from components.WorkforceManagement.persistence.schedule import Schedule as DBSchedule
from components.WorkforceManagement.persistence.employee import Employee as DBEmployee
from components.WorkforceManagement.persistence.region import Region as DBRegion

class ActivityBuilder(Builder):
    """Builds a Activity object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result: Activity = None  # type: ignore

    def build_empty_object(self, config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Builds a Activity object"""
        self.request.set_value("object_class_name", "Activity")

        configuration = config_loader.find_configuration(ACTIVITY)

        self.result = super()._create_model_object(
          configuration, extended_domain={"Activity": Activity,
                                            "Money": Money,
                                            "Schedule": Schedule,
                                            "Employee": Employee,
                                            "Region": Region,
                                        })

    def add_object_data(self, mapped_object: Union[bytes, str, DBActivity], protocol=None):
        """adds the data from the mapped object to the Health object """
        if protocol == Protocols.JSON and isinstance(mapped_object, bytes):
            self._add_json_object_data(mapped_object)

        elif isinstance(mapped_object, DBActivity):
            self._add_db_object_data(mapped_object)

    def _add_json_object_data(self, json_object: bytes):
        """adds the data from the json object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", json_object)
        self.request.set_value("protocol", Protocols.JSON)
        self.execute_sub_action("deserialize")

    def _add_db_object_data(self, db_object: DBActivity):
        """adds the data from the db object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", db_object)
        self.result.oid = db_object.oid
        self.result.activityNr = db_object.activityNr
        self.result.name = db_object.name
        self.result.status = db_object.status
        self.result.input = db_object.input
        self.result.output = db_object.output
        self.result.plannedStart = db_object.plannedStart
        self.result.plannedEnd = db_object.plannedEnd
        self.result.plannedTenure = db_object.plannedTenure
        self.result.ActivityDoneFor = db_object.ActivityDoneFor
    def get_result(self):
        """gets the result of the builder"""
        return self.result
