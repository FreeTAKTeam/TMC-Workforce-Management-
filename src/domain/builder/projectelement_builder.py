from typing import Union
from digitalpy.core.domain.builder import Builder
from digitalpy.core.serialization.configuration.serialization_constants import Protocols
from digitalpy.core.domain.object_id import ObjectId


from components.WorkforceManagement.configuration.WorkforceManagement_constants import PROJECTELEMENT

# import domain model classes
from components.WorkforceManagement.domain.model.projectelement import ProjectElement

from components.WorkforceManagement.persistence.projectelement import ProjectElement as DBProjectElement

class ProjectElementBuilder(Builder):
    """Builds a ProjectElement object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result: ProjectElement = None  # type: ignore

    def build_empty_object(self, config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Builds a ProjectElement object"""
        self.request.set_value("object_class_name", "ProjectElement")

        configuration = config_loader.find_configuration(PROJECTELEMENT)

        self.result = super()._create_model_object(
          configuration, extended_domain={"ProjectElement": ProjectElement,
                                        })

    def add_object_data(self, mapped_object: Union[bytes, str, DBProjectElement], protocol=None):
        """adds the data from the mapped object to the Health object """
        if protocol == Protocols.JSON and isinstance(mapped_object, bytes):
            self._add_json_object_data(mapped_object)

        elif isinstance(mapped_object, DBProjectElement):
            self._add_db_object_data(mapped_object)

    def _add_json_object_data(self, json_object: bytes):
        """adds the data from the json object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", json_object)
        self.request.set_value("protocol", Protocols.JSON)
        self.execute_sub_action("deserialize")

    def _add_db_object_data(self, db_object: DBProjectElement):
        """adds the data from the db object to the Health object """
        self.request.set_value("model_object", self.result)
        self.request.set_value("message", db_object)
        self.result.oid = db_object.oid
        self.result.plannedDuration = db_object.plannedDuration
        self.result.actualDuration = db_object.actualDuration
        self.result.currentDuration = db_object.currentDuration
        self.result.status = db_object.status
        self.result.priority = db_object.priority
        self.result.timingConstraint = db_object.timingConstraint
    def get_result(self):
        """gets the result of the builder"""
        return self.result
