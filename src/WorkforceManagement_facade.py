from .controllers.WorkforceManagement_persistence_controller import WorkforceManagementPersistenceController
from digitalpy.core.component_management.impl.default_facade import DefaultFacade
from digitalpy.core.zmanager.impl.async_action_mapper import AsyncActionMapper
from digitalpy.core.zmanager.impl.default_action_mapper import DefaultActionMapper
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response
from .controllers.WorkforceManagement_controller import WorkforceManagementController
from .configuration.WorkforceManagement_constants import (
    ACTION_MAPPING_PATH,
    LOGGING_CONFIGURATION_PATH,
    INTERNAL_ACTION_MAPPING_PATH,
    MANIFEST_PATH,
    CONFIGURATION_PATH_TEMPLATE,
    LOG_FILE_PATH
)

from . import base


class WorkforceManagement(DefaultFacade):
    """
    """

    def __init__(self, sync_action_mapper: DefaultActionMapper, request: Request,
                 response: Response, configuration,
                 action_mapper: AsyncActionMapper = None,  # type: ignore
                 tracing_provider_instance=None):  # type: ignore
        super().__init__(
            # the path to the external action mapping
            action_mapping_path=str(ACTION_MAPPING_PATH),
            # the path to the internal action mapping
            internal_action_mapping_path=str(INTERNAL_ACTION_MAPPING_PATH),
            # the path to the logger configuration
            logger_configuration=str(LOGGING_CONFIGURATION_PATH),
            # the package containing the base classes
            base=base,  # type: ignore
            # the general action mapper (passed by constructor)
            action_mapper=sync_action_mapper,
            # the request object (passed by constructor)
            request=request,
            # the response object (passed by constructor)
            response=response,
            # the configuration object (passed by constructor)
            configuration=configuration,
            # log file path
            log_file_path=LOG_FILE_PATH,
            # the tracing provider used
            tracing_provider_instance=tracing_provider_instance,
            # the template for the absolute path to the model object definitions
            configuration_path_template=CONFIGURATION_PATH_TEMPLATE,
            # the path to the manifest file
            manifest_path=str(MANIFEST_PATH),
        )
        self.persistence_controller = WorkforceManagementPersistenceController(
            request, response, sync_action_mapper, configuration)
        self.WorkforceManagement_controller = WorkforceManagementController(
            request, response, sync_action_mapper, configuration)

    def initialize(self, request, response):
        self.WorkforceManagement_controller.initialize(request, response)
        self.persistence_controller.initialize(request, response)

        return super().initialize(request, response)

    def execute(self, method=None):
        try:
            if hasattr(self, method):  # type: ignore
                print("executing method "+str(method))  # type: ignore
                getattr(self, method)(**self.request.get_values())  # type: ignore
            else:
                self.request.set_value("logger", self.logger)
                self.request.set_value("config_loader", self.config_loader)
                self.request.set_value("tracer", self.tracer)
                response = self.execute_sub_action(self.request.get_action())
                self.response.set_values(response.get_values())
        except Exception as e:
            self.logger.fatal(str(e))
    @DefaultFacade.public
    def POSTEmployee(self, *args, **kwargs):
        """Creates a new employee record.
        """
        self.WorkforceManagement_controller.POSTEmployee(*args, **kwargs)
    @DefaultFacade.public
    def DELETEEmployee(self, *args, **kwargs):
        """Deletes an existing employee record based on the provided ID.
        """
        self.WorkforceManagement_controller.DELETEEmployee(*args, **kwargs)
    @DefaultFacade.public
    def GETEmployee(self, *args, **kwargs):
        """Retrieves a list of all employees.
        """
        self.WorkforceManagement_controller.GETEmployee(*args, **kwargs)
    @DefaultFacade.public
    def PATCHEmployee(self, *args, **kwargs):
        """Updates an existing employee record.
        """
        self.WorkforceManagement_controller.PATCHEmployee(*args, **kwargs)
    @DefaultFacade.public
    def POSTRegion(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.POSTRegion(*args, **kwargs)
    @DefaultFacade.public
    def DELETERegion(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.DELETERegion(*args, **kwargs)
    @DefaultFacade.public
    def GETRegion(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.GETRegion(*args, **kwargs)
    @DefaultFacade.public
    def PATCHRegion(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.PATCHRegion(*args, **kwargs)
    @DefaultFacade.public
    def POSTMoney(self, *args, **kwargs):
        """Creates a new Money record.
        """
        self.WorkforceManagement_controller.POSTMoney(*args, **kwargs)
    @DefaultFacade.public
    def DELETEMoney(self, *args, **kwargs):
        """Deletes an existing Money record based on the provided ID.
        """
        self.WorkforceManagement_controller.DELETEMoney(*args, **kwargs)
    @DefaultFacade.public
    def GETMoney(self, *args, **kwargs):
        """Retrieves a list of all Money
        """
        self.WorkforceManagement_controller.GETMoney(*args, **kwargs)
    @DefaultFacade.public
    def PATCHMoney(self, *args, **kwargs):
        """Updates an existing Money record.
        """
        self.WorkforceManagement_controller.PATCHMoney(*args, **kwargs)
    @DefaultFacade.public
    def GETMoneyId(self, *args, **kwargs):
        """retrieve an existing Money record based on the provided ID.
        """
        self.WorkforceManagement_controller.GETMoneyId(*args, **kwargs)
    @DefaultFacade.public
    def POSTActivityMetricTimeEfficiency(self, *args, **kwargs):
        """Activity Metric TimeEfficiency
        """
        self.WorkforceManagement_controller.POSTActivityMetricTimeEfficiency(*args, **kwargs)
    @DefaultFacade.public
    def GETEmployeeId(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.GETEmployeeId(*args, **kwargs)
    @DefaultFacade.public
    def POSTSchedule(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.POSTSchedule(*args, **kwargs)
    @DefaultFacade.public
    def DELETESchedule(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.DELETESchedule(*args, **kwargs)
    @DefaultFacade.public
    def GETSchedule(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.GETSchedule(*args, **kwargs)
    @DefaultFacade.public
    def PATCHSchedule(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.PATCHSchedule(*args, **kwargs)
    @DefaultFacade.public
    def GETRegionId(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.GETRegionId(*args, **kwargs)
    @DefaultFacade.public
    def GETScheduleId(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.GETScheduleId(*args, **kwargs)
    @DefaultFacade.public
    def POSTActivity(self, *args, **kwargs):
        """Activity creation
        """
        self.WorkforceManagement_controller.POSTActivity(*args, **kwargs)
    @DefaultFacade.public
    def DELETEActivity(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.DELETEActivity(*args, **kwargs)
    @DefaultFacade.public
    def GETActivity(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.GETActivity(*args, **kwargs)
    @DefaultFacade.public
    def PATCHActivity(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.PATCHActivity(*args, **kwargs)
    @DefaultFacade.public
    def GETActivityId(self, *args, **kwargs):
        """TODO
        """
        self.WorkforceManagement_controller.GETActivityId(*args, **kwargs)
