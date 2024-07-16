from typing import Union
from components.WorkforceManagement.domain.model.activity import Activity
from components.WorkforceManagement.persistence.activity import Activity as DBActivity
from components.WorkforceManagement.domain.builder.activity_builder import ActivityBuilder
from components.WorkforceManagement.controllers.WorkforceManagement_persistence_controller import WorkforceManagementPersistenceController


from components.WorkforceManagement.domain.builder.money_builder import MoneyBuilder

from digitalpy.core.serialization.configuration.serialization_constants import Protocols
from digitalpy.core.domain.node import Node
from digitalpy.core.main.controller import Controller
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response
from digitalpy.core.zmanager.action_mapper import ActionMapper
from digitalpy.core.digipy_configuration.configuration import Configuration
from digitalpy.core.parsing.load_configuration import LoadConfiguration


class ActivityDirector(Controller):

    def __init__(self, request: Request, response: Response, sync_action_mapper: ActionMapper, configuration: Configuration):
        super().__init__(request, response, sync_action_mapper, configuration)
        self.Activity_builder = ActivityBuilder(request, response, sync_action_mapper, configuration)
        self.Money_builder = MoneyBuilder(request, response, sync_action_mapper, configuration)
        self.persistency_controller = WorkforceManagementPersistenceController(
            request, response, sync_action_mapper, configuration)


    def initialize(self, request, response):
        super().initialize(request, response)
        self.Activity_builder.initialize(request, response)
        self.Money_builder.initialize(request, response)
        self.persistency_controller.initialize(request, response)

    def execute(self, method=None):
        getattr(self, method)(**self.request.get_values())
        return self.response

    def construct_from_db(self, Activity: 'DBActivity', config_loader, base_object: 'Activity' = None, *args, **kwargs) -> 'Activity':
        """construct a node from a mapped object"""
        if (base_object):
            self.Activity_builder.result = base_object
        else:
            self.Activity_builder.build_empty_object(config_loader=config_loader)
        self.Activity_builder.add_object_data(mapped_object=Activity, protocol=None)
        Activity_completed = self.Activity_builder.get_result()

        ActualCost = Activity.ActualCost
        self.Money_builder.build_empty_object(config_loader=config_loader)
        self.Money_builder.add_object_data(mapped_object=ActualCost, protocol=None)
        Money_completed = self.Money_builder.get_result()
        Activity_completed.ActualCost = Money_completed.oid

        return Activity_completed

    def construct_from_json(self, Activity: Union[str, bytes], config_loader, base_object: 'Activity' = None, *args, **kwargs) -> 'Activity':
        """construct a node from a mapped object"""
        # if the base_object is passed use it, otherwise build a new one
        if (base_object):
            self.Activity_builder.result = base_object
        else:
            self.Activity_builder.build_empty_object(config_loader=config_loader)

        # call the Activity builder to serialize the data into the object
        self.Activity_builder.add_object_data(mapped_object=Activity, protocol=Protocols.JSON)
        Activity_completed = self.Activity_builder.get_result()


        return Activity_completed
