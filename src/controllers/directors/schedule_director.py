from typing import Union
from components.WorkforceManagement.domain.model.schedule import Schedule
from components.WorkforceManagement.persistence.schedule import Schedule as DBSchedule
from components.WorkforceManagement.domain.builder.schedule_builder import ScheduleBuilder
from components.WorkforceManagement.controllers.WorkforceManagement_persistence_controller import WorkforceManagementPersistenceController


from components.WorkforceManagement.domain.builder.employee_builder import EmployeeBuilder
from components.WorkforceManagement.domain.builder.activity_builder import ActivityBuilder

from digitalpy.core.serialization.configuration.serialization_constants import Protocols
from digitalpy.core.domain.node import Node
from digitalpy.core.main.controller import Controller
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response
from digitalpy.core.zmanager.action_mapper import ActionMapper
from digitalpy.core.digipy_configuration.configuration import Configuration
from digitalpy.core.parsing.load_configuration import LoadConfiguration


class ScheduleDirector(Controller):

    def __init__(self, request: Request, response: Response, sync_action_mapper: ActionMapper, configuration: Configuration):
        super().__init__(request, response, sync_action_mapper, configuration)
        self.Schedule_builder = ScheduleBuilder(request, response, sync_action_mapper, configuration)
        self.Employee_builder = EmployeeBuilder(request, response, sync_action_mapper, configuration)
        self.Activity_builder = ActivityBuilder(request, response, sync_action_mapper, configuration)
        self.persistency_controller = WorkforceManagementPersistenceController(
            request, response, sync_action_mapper, configuration)


    def initialize(self, request, response):
        super().initialize(request, response)
        self.Schedule_builder.initialize(request, response)
        self.Employee_builder.initialize(request, response)
        self.Activity_builder.initialize(request, response)
        self.persistency_controller.initialize(request, response)

    def execute(self, method=None):
        getattr(self, method)(**self.request.get_values())
        return self.response

    def construct_from_db(self, Schedule: 'DBSchedule', config_loader, base_object: 'Schedule' = None, *args, **kwargs) -> 'Schedule':
        """construct a node from a mapped object"""
        if (base_object):
            self.Schedule_builder.result = base_object
        else:
            self.Schedule_builder.build_empty_object(config_loader=config_loader)
        self.Schedule_builder.add_object_data(mapped_object=Schedule, protocol=None)
        Schedule_completed = self.Schedule_builder.get_result()

        Employee = Schedule.Employee
        self.Employee_builder.build_empty_object(config_loader=config_loader)
        self.Employee_builder.add_object_data(mapped_object=Employee, protocol=None)
        Employee_completed = self.Employee_builder.get_result()
        Schedule_completed.Employee = Employee_completed.oid
        for Activity in Schedule.Activity:
            self.Activity_builder.build_empty_object(config_loader=config_loader)
            self.Activity_builder.add_object_data(mapped_object=Activity, protocol=None)
            Activity_completed = self.Activity_builder.get_result()
            Schedule_completed.Activity.append(Activity_completed.oid)

        return Schedule_completed

    def construct_from_json(self, Schedule: Union[str, bytes], config_loader, base_object: 'Schedule' = None, *args, **kwargs) -> 'Schedule':
        """construct a node from a mapped object"""
        # if the base_object is passed use it, otherwise build a new one
        if (base_object):
            self.Schedule_builder.result = base_object
        else:
            self.Schedule_builder.build_empty_object(config_loader=config_loader)

        # call the Schedule builder to serialize the data into the object
        self.Schedule_builder.add_object_data(mapped_object=Schedule, protocol=Protocols.JSON)
        Schedule_completed = self.Schedule_builder.get_result()


        return Schedule_completed
