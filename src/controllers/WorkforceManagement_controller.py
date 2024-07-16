"""
This is the main controller class of the application. Every operation of the controller is realized by this file
OOTB. It is recommended that you (the developper) avoid adding further methods to the file and instead add supporting
controllers with these methods should you need them. This controller is called directly by the facade in order to
fulfil any requests made to the component by default.
"""

from typing import TYPE_CHECKING, List

from digitalpy.core.main.controller import Controller
from digitalpy.core.serialization.configuration.serialization_constants import Protocols
# import builders
from components.WorkforceManagement.controllers.directors.activity_director import ActivityDirector
from components.WorkforceManagement.domain.builder.activity_builder import ActivityBuilder
from components.WorkforceManagement.domain.builder.money_builder import MoneyBuilder
from components.WorkforceManagement.domain.builder.projectelement_builder import ProjectElementBuilder
from components.WorkforceManagement.controllers.directors.employee_director import EmployeeDirector
from components.WorkforceManagement.domain.builder.employee_builder import EmployeeBuilder
from components.WorkforceManagement.domain.builder.region_builder import RegionBuilder
from components.WorkforceManagement.controllers.directors.schedule_director import ScheduleDirector
from components.WorkforceManagement.domain.builder.schedule_builder import ScheduleBuilder
from components.WorkforceManagement.domain.builder.error_builder import ErrorBuilder
from .WorkforceManagement_persistence_controller import WorkforceManagementPersistenceController

if TYPE_CHECKING:
    from digitalpy.core.digipy_configuration.configuration import Configuration
    from digitalpy.core.zmanager.impl.default_action_mapper import DefaultActionMapper
    from digitalpy.core.zmanager.request import Request
    from digitalpy.core.zmanager.response import Response
    from digitalpy.core.domain.domain.network_client import NetworkClient
    from components.WorkforceManagement.domain.model.activity import Activity
    from components.WorkforceManagement.domain.model.money import Money
    from components.WorkforceManagement.domain.model.projectelement import ProjectElement
    from components.WorkforceManagement.domain.model.employee import Employee
    from components.WorkforceManagement.domain.model.region import Region
    from components.WorkforceManagement.domain.model.schedule import Schedule
    from components.WorkforceManagement.domain.model.error import Error

class WorkforceManagementController(Controller):

    def __init__(self, request: 'Request',
                 response: 'Response',
                 sync_action_mapper: 'DefaultActionMapper',
                 configuration: 'Configuration'):
        super().__init__(request, response, sync_action_mapper, configuration)
        self.Activity_director = ActivityDirector(request, response, sync_action_mapper, configuration)
        self.Activity_builder = ActivityBuilder(request, response, sync_action_mapper, configuration)
        self.Money_builder = MoneyBuilder(request, response, sync_action_mapper, configuration)
        self.Projectelement_builder = ProjectElementBuilder(request, response, sync_action_mapper, configuration)
        self.Employee_director = EmployeeDirector(request, response, sync_action_mapper, configuration)
        self.Employee_builder = EmployeeBuilder(request, response, sync_action_mapper, configuration)
        self.Region_builder = RegionBuilder(request, response, sync_action_mapper, configuration)
        self.Schedule_director = ScheduleDirector(request, response, sync_action_mapper, configuration)
        self.Schedule_builder = ScheduleBuilder(request, response, sync_action_mapper, configuration)
        self.Error_builder = ErrorBuilder(request, response, sync_action_mapper, configuration)
        self.WorkforceManagement_persistence_controller = WorkforceManagementPersistenceController(
            request, response, sync_action_mapper, configuration)

    def initialize(self, request: 'Request', response: 'Response'):
        """This function is used to initialize the controller. 
        It is intiated by the service manager."""
        self.Activity_director.initialize(request, response)
        self.Activity_builder.initialize(request, response)
        self.Money_builder.initialize(request, response)
        self.Projectelement_builder.initialize(request, response)
        self.Employee_director.initialize(request, response)
        self.Employee_builder.initialize(request, response)
        self.Region_builder.initialize(request, response)
        self.Schedule_director.initialize(request, response)
        self.Schedule_builder.initialize(request, response)
        self.Error_builder.initialize(request, response)
        self.WorkforceManagement_persistence_controller.initialize(request, response)
        return super().initialize(request, response)
    def POSTEmployee(self, body: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Creates a new employee record."""

        # initialize Employee builder
        domain_obj  = self.Employee_director.construct_from_json(body, config_loader)

        # Save the Employee record to the database
        self.WorkforceManagement_persistence_controller.save_employee(domain_obj)

        domain_records = [domain_obj]
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def DELETEEmployee(self, ID: str, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Deletes an existing employee record based on the provided ID."""
        db_records = self.WorkforceManagement_persistence_controller.get_employee(ID = ID)
        domain_records: List['Employee'] = []

        # convert the records to the domain object
        for record in db_records:
            record = self.Employee_director.construct_from_db(record, config_loader)
            self.WorkforceManagement_persistence_controller.remove_employee(record)
            domain_records.append(record)
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def GETEmployee(self, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Retrieves a list of all employees."""
        # retrieve the Employee record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_all_employee()
        domain_records: List['Employee'] = []

        # convert the records to the domain object
        for record in db_records:
            Employee = self.Employee_director.construct_from_db(record, config_loader)
            domain_records.append(Employee)
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def PATCHEmployee(self, body: 'Employee',  client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Updates an existing employee record."""
        # create the basic domain object from the json data
        self.Employee_builder.build_empty_object(config_loader)
        self.Employee_builder.add_object_data(body, Protocols.JSON)
        domain_obj = self.Employee_builder.get_result()

        # get from the database
        db_obj = self.WorkforceManagement_persistence_controller.get_employee(oid=str(domain_obj.oid))[0]

        # initialize the object
        self.Employee_director.construct_from_db(db_obj, config_loader, domain_obj)
        # TODO: this duplaction seems unnecessary
        # update the object with json data
        domain_obj = self.Employee_director.construct_from_json(body, config_loader, domain_obj)
        # Save the Schedule record to the database
        self.WorkforceManagement_persistence_controller.update_employee(domain_obj)

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", [domain_obj])

        # publish the records
        self.response.set_action("publish")

    def POSTRegion(self, body: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Create a new region"""

        # initialize Region builder
        self.Region_builder.build_empty_object(config_loader=config_loader)
        self.Region_builder.add_object_data(mapped_object = body, protocol=Protocols.JSON)
        domain_obj = self.Region_builder.get_result()

        # Save the Region record to the database
        self.WorkforceManagement_persistence_controller.save_region(domain_obj)

        domain_records = [domain_obj]
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def DELETERegion(self, ID: str, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Delete by ID a Region"""
        db_records = self.WorkforceManagement_persistence_controller.get_region(ID = ID)
        domain_records: List['Region'] = []

        # convert the records to the domain object
        for record in db_records:
            self.Region_builder.build_empty_object(config_loader=config_loader)
            self.Region_builder.add_object_data(record)
            record = self.Region_builder.get_result()
            self.WorkforceManagement_persistence_controller.remove_region(record)
            domain_records.append(record)
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def GETRegion(self, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Returns a list of all Regions"""
        # retrieve the Region record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_all_region()
        domain_records: List['Region'] = []

        # convert the records to the domain object
        for record in db_records:
            self.Region_builder.build_empty_object(config_loader=config_loader)
            self.Region_builder.add_object_data(record)
            domain_records.append(self.Region_builder.get_result())
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def PATCHRegion(self, body: 'Region',  client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Unpdate by ID a Region"""
        # create the basic domain object from the json data
        self.Region_builder.build_empty_object(config_loader)
        self.Region_builder.add_object_data(body, Protocols.JSON)
        domain_obj = self.Region_builder.get_result()

        # get from the database
        db_obj = self.WorkforceManagement_persistence_controller.get_region(oid=str(domain_obj.oid))[0]

        # initialize the object
        self.Region_builder.build_empty_object(config_loader)
        self.Region_builder.add_object_data(db_obj)
        # TODO: this duplaction seems unnecessary
        # update the object with json data
        self.Region_builder.add_object_data(body, Protocols.JSON)
        # Save the Schedule record to the database
        self.WorkforceManagement_persistence_controller.update_region(domain_obj)

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", [domain_obj])

        # publish the records
        self.response.set_action("publish")

    def POSTMoney(self, body: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Creates a new Money record."""

        # initialize Money builder
        self.Money_builder.build_empty_object(config_loader=config_loader)
        self.Money_builder.add_object_data(mapped_object = body, protocol=Protocols.JSON)
        domain_obj = self.Money_builder.get_result()

        # Save the Money record to the database
        self.WorkforceManagement_persistence_controller.save_money(domain_obj)

        domain_records = [domain_obj]
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def DELETEMoney(self, ID: str, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Deletes an existing Money record based on the provided ID."""
        db_records = self.WorkforceManagement_persistence_controller.get_money(ID = ID)
        domain_records: List['Money'] = []

        # convert the records to the domain object
        for record in db_records:
            self.Money_builder.build_empty_object(config_loader=config_loader)
            self.Money_builder.add_object_data(record)
            record = self.Money_builder.get_result()
            self.WorkforceManagement_persistence_controller.remove_money(record)
            domain_records.append(record)
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def GETMoney(self, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Retrieves a list of all Money"""
        # retrieve the Money record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_all_money()
        domain_records: List['Money'] = []

        # convert the records to the domain object
        for record in db_records:
            self.Money_builder.build_empty_object(config_loader=config_loader)
            self.Money_builder.add_object_data(record)
            domain_records.append(self.Money_builder.get_result())
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def PATCHMoney(self, body: 'Money',  client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Updates an existing Money record."""
        # create the basic domain object from the json data
        self.Money_builder.build_empty_object(config_loader)
        self.Money_builder.add_object_data(body, Protocols.JSON)
        domain_obj = self.Money_builder.get_result()

        # get from the database
        db_obj = self.WorkforceManagement_persistence_controller.get_money(oid=str(domain_obj.oid))[0]

        # initialize the object
        self.Money_builder.build_empty_object(config_loader)
        self.Money_builder.add_object_data(db_obj)
        # TODO: this duplaction seems unnecessary
        # update the object with json data
        self.Money_builder.add_object_data(body, Protocols.JSON)
        # Save the Schedule record to the database
        self.WorkforceManagement_persistence_controller.update_money(domain_obj)

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", [domain_obj])

        # publish the records
        self.response.set_action("publish")

    def GETMoneyId(self, ID: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """retrieve an existing Money record based on the provided ID."""

        # retrieve the Money record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_money(ID = ID)
        domain_records: List['Money'] = []

        # convert the records to the domain object
        for record in db_records:
            self.Money_builder.build_empty_object(config_loader=config_loader)
            self.Money_builder.add_object_data(record)
            domain_records.append(self.Money_builder.get_result())

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def POSTActivityMetricTimeEfficiency(self, client: 'NetworkClient', config_loader, *args, **kwargs): # pylint: disable=unused-argument
        """Activity Metric TimeEfficiency"""
        return None

    def GETEmployeeId(self, ID: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Return by ID an Employee"""

        # retrieve the Employee record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_employee(ID = ID)
        domain_records: List['Employee'] = []

        # convert the records to the domain object
        for record in db_records:
            Employee = self.Employee_director.construct_from_db(record, config_loader)
            domain_records.append(Employee)

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def POSTSchedule(self, body: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Create a new Schedule"""

        # initialize Schedule builder
        domain_obj  = self.Schedule_director.construct_from_json(body, config_loader)

        # Save the Schedule record to the database
        self.WorkforceManagement_persistence_controller.save_schedule(domain_obj)

        domain_records = [domain_obj]
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def DELETESchedule(self, ID: str, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Delete by ID a Schehdule"""
        db_records = self.WorkforceManagement_persistence_controller.get_schedule(ID = ID)
        domain_records: List['Schedule'] = []

        # convert the records to the domain object
        for record in db_records:
            record = self.Schedule_director.construct_from_db(record, config_loader)
            self.WorkforceManagement_persistence_controller.remove_schedule(record)
            domain_records.append(record)
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def GETSchedule(self, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Returns a list of all Schedules"""
        # retrieve the Schedule record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_all_schedule()
        domain_records: List['Schedule'] = []

        # convert the records to the domain object
        for record in db_records:
            Schedule = self.Schedule_director.construct_from_db(record, config_loader)
            domain_records.append(Schedule)
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def PATCHSchedule(self, body: 'Schedule',  client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Unpdate by ID a Schedule"""
        # create the basic domain object from the json data
        self.Schedule_builder.build_empty_object(config_loader)
        self.Schedule_builder.add_object_data(body, Protocols.JSON)
        domain_obj = self.Schedule_builder.get_result()

        # get from the database
        db_obj = self.WorkforceManagement_persistence_controller.get_schedule(oid=str(domain_obj.oid))[0]

        # initialize the object
        self.Schedule_director.construct_from_db(db_obj, config_loader, domain_obj)
        # TODO: this duplaction seems unnecessary
        # update the object with json data
        domain_obj = self.Schedule_director.construct_from_json(body, config_loader, domain_obj)
        # Save the Schedule record to the database
        self.WorkforceManagement_persistence_controller.update_schedule(domain_obj)

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", [domain_obj])

        # publish the records
        self.response.set_action("publish")

    def GETRegionId(self, ID: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Return by ID a Region"""

        # retrieve the Region record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_region(ID = ID)
        domain_records: List['Region'] = []

        # convert the records to the domain object
        for record in db_records:
            self.Region_builder.build_empty_object(config_loader=config_loader)
            self.Region_builder.add_object_data(record)
            domain_records.append(self.Region_builder.get_result())

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def GETScheduleId(self, ID: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Return by ID a Schedule"""

        # retrieve the Schedule record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_schedule(ID = ID)
        domain_records: List['Schedule'] = []

        # convert the records to the domain object
        for record in db_records:
            Schedule = self.Schedule_director.construct_from_db(record, config_loader)
            domain_records.append(Schedule)

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def POSTActivity(self, body: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Activity creation"""

        # initialize Activity builder
        domain_obj  = self.Activity_director.construct_from_json(body, config_loader)

        # Save the Activity record to the database
        self.WorkforceManagement_persistence_controller.save_activity(domain_obj)

        domain_records = [domain_obj]
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def DELETEActivity(self, ID: str, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Delete by ID an Activity"""
        db_records = self.WorkforceManagement_persistence_controller.get_activity(ID = ID)
        domain_records: List['Activity'] = []

        # convert the records to the domain object
        for record in db_records:
            record = self.Activity_director.construct_from_db(record, config_loader)
            self.WorkforceManagement_persistence_controller.remove_activity(record)
            domain_records.append(record)
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def GETActivity(self, client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Returns a list of all Activities"""
        # retrieve the Activity record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_all_activity()
        domain_records: List['Activity'] = []

        # convert the records to the domain object
        for record in db_records:
            Activity = self.Activity_director.construct_from_db(record, config_loader)
            domain_records.append(Activity)
        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

    def PATCHActivity(self, body: 'Activity',  client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Unpdate by ID an Activity"""
        # create the basic domain object from the json data
        self.Activity_builder.build_empty_object(config_loader)
        self.Activity_builder.add_object_data(body, Protocols.JSON)
        domain_obj = self.Activity_builder.get_result()

        # get from the database
        db_obj = self.WorkforceManagement_persistence_controller.get_activity(oid=str(domain_obj.oid))[0]

        # initialize the object
        self.Activity_director.construct_from_db(db_obj, config_loader, domain_obj)
        # TODO: this duplaction seems unnecessary
        # update the object with json data
        domain_obj = self.Activity_director.construct_from_json(body, config_loader, domain_obj)
        # Save the Schedule record to the database
        self.WorkforceManagement_persistence_controller.update_activity(domain_obj)

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", [domain_obj])

        # publish the records
        self.response.set_action("publish")

    def GETActivityId(self, ID: 'str', client: 'NetworkClient', config_loader, *args, **kwargs):  # pylint: disable=unused-argument
        """Return by ID an Activity"""

        # retrieve the Activity record from the database
        db_records = self.WorkforceManagement_persistence_controller.get_activity(ID = ID)
        domain_records: List['Activity'] = []

        # convert the records to the domain object
        for record in db_records:
            Activity = self.Activity_director.construct_from_db(record, config_loader)
            domain_records.append(Activity)

        # set the target
        self.response.set_value("recipients", [str(client.get_oid())])

        # return the records
        self.response.set_value("message", domain_records)

        # publish the records
        self.response.set_action("publish")

