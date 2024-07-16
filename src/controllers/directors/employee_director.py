from typing import Union
from components.WorkforceManagement.domain.model.employee import Employee
from components.WorkforceManagement.persistence.employee import Employee as DBEmployee
from components.WorkforceManagement.domain.builder.employee_builder import EmployeeBuilder
from components.WorkforceManagement.controllers.WorkforceManagement_persistence_controller import WorkforceManagementPersistenceController


from components.WorkforceManagement.domain.builder.region_builder import RegionBuilder

from digitalpy.core.serialization.configuration.serialization_constants import Protocols
from digitalpy.core.domain.node import Node
from digitalpy.core.main.controller import Controller
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response
from digitalpy.core.zmanager.action_mapper import ActionMapper
from digitalpy.core.digipy_configuration.configuration import Configuration
from digitalpy.core.parsing.load_configuration import LoadConfiguration


class EmployeeDirector(Controller):

    def __init__(self, request: Request, response: Response, sync_action_mapper: ActionMapper, configuration: Configuration):
        super().__init__(request, response, sync_action_mapper, configuration)
        self.Employee_builder = EmployeeBuilder(request, response, sync_action_mapper, configuration)
        self.Region_builder = RegionBuilder(request, response, sync_action_mapper, configuration)
        self.persistency_controller = WorkforceManagementPersistenceController(
            request, response, sync_action_mapper, configuration)


    def initialize(self, request, response):
        super().initialize(request, response)
        self.Employee_builder.initialize(request, response)
        self.Region_builder.initialize(request, response)
        self.persistency_controller.initialize(request, response)

    def execute(self, method=None):
        getattr(self, method)(**self.request.get_values())
        return self.response

    def construct_from_db(self, Employee: 'DBEmployee', config_loader, base_object: 'Employee' = None, *args, **kwargs) -> 'Employee':
        """construct a node from a mapped object"""
        if (base_object):
            self.Employee_builder.result = base_object
        else:
            self.Employee_builder.build_empty_object(config_loader=config_loader)
        self.Employee_builder.add_object_data(mapped_object=Employee, protocol=None)
        Employee_completed = self.Employee_builder.get_result()

        Responsiblefor = Employee.Responsiblefor
        self.Region_builder.build_empty_object(config_loader=config_loader)
        self.Region_builder.add_object_data(mapped_object=Responsiblefor, protocol=None)
        Region_completed = self.Region_builder.get_result()
        Employee_completed.Responsiblefor = Region_completed.oid

        return Employee_completed

    def construct_from_json(self, Employee: Union[str, bytes], config_loader, base_object: 'Employee' = None, *args, **kwargs) -> 'Employee':
        """construct a node from a mapped object"""
        # if the base_object is passed use it, otherwise build a new one
        if (base_object):
            self.Employee_builder.result = base_object
        else:
            self.Employee_builder.build_empty_object(config_loader=config_loader)

        # call the Employee builder to serialize the data into the object
        self.Employee_builder.add_object_data(mapped_object=Employee, protocol=Protocols.JSON)
        Employee_completed = self.Employee_builder.get_result()


        return Employee_completed
