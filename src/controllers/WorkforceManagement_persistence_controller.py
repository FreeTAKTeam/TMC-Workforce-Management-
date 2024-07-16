from typing import TYPE_CHECKING, List, Union
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# import tables in initialization order
from components.WorkforceManagement.persistence.activity import Activity as DBActivity
from components.WorkforceManagement.persistence.money import Money as DBMoney
from components.WorkforceManagement.persistence.projectelement import ProjectElement as DBProjectElement
from components.WorkforceManagement.persistence.employee import Employee as DBEmployee
from components.WorkforceManagement.persistence.region import Region as DBRegion
from components.WorkforceManagement.persistence.schedule import Schedule as DBSchedule
from components.WorkforceManagement.persistence.error import Error as DBError

# import domain model classes
from components.WorkforceManagement.domain.model.activity import Activity
from components.WorkforceManagement.domain.model.money import Money
from components.WorkforceManagement.domain.model.projectelement import ProjectElement
from components.WorkforceManagement.domain.model.employee import Employee
from components.WorkforceManagement.domain.model.region import Region
from components.WorkforceManagement.domain.model.schedule import Schedule
from components.WorkforceManagement.domain.model.error import Error

from digitalpy.core.main.controller import Controller
from components.WorkforceManagement.persistence.WorkforceManagement_base import WorkforceManagementBase
from components.WorkforceManagement.configuration.WorkforceManagement_constants import DB_PATH

if TYPE_CHECKING:
    from digitalpy.core.zmanager.request import Request
    from digitalpy.core.zmanager.response import Response
    from digitalpy.core.digipy_configuration.configuration import Configuration
    from digitalpy.core.zmanager.action_mapper import ActionMapper


class WorkforceManagementPersistenceController(Controller):
    """this class is responsible for handling the persistence of the WorkforceManagement
    component. It is responsible for creating, removing and retrieving records.
    """

    def __init__(
        self,
        request: 'Request',
        response: 'Response',
        sync_action_mapper: 'ActionMapper',
        configuration: 'Configuration',
    ):
        super().__init__(request, response, sync_action_mapper, configuration)
        self.ses = self.create_db_session()

    def create_db_session(self) -> Session:
        """open a new session in the database

        Returns:
            Session: the session connecting the db
        """
        engine = create_engine(DB_PATH)
        # create a configured "Session" class
        SessionClass = sessionmaker(bind=engine)

        WorkforceManagementBase.metadata.create_all(engine)

        # create a Session
        return SessionClass()

    # Begin methods for activity table


    def save_activity(self, activity: Activity, *args, **kwargs) -> 'DBActivity':
        if not isinstance(activity, Activity):
            raise TypeError("'Activity' must be an instance of Activity")

        db_activity = DBActivity()
        db_activity.oid = activity.oid
        db_activity.activityNr = activity.activityNr
        db_activity.name = activity.name
        db_activity.status = activity.status
        db_activity.input = activity.input
        db_activity.output = activity.output
        db_activity.plannedStart = activity.plannedStart
        db_activity.plannedEnd = activity.plannedEnd
        db_activity.plannedTenure = activity.plannedTenure
        db_activity.ActivityDoneFor = activity.ActivityDoneFor
        ActualCost = activity.ActualCost
        if ActualCost:
            db_ActualCost_list = self.get_money(oid = ActualCost)
            if len(db_ActualCost_list)>0:
                db_activity.ActualCost = db_ActualCost_list[0]
                db_activity.ActualCost_oid = db_ActualCost_list[0].oid
        self.ses.add(db_activity)
        self.ses.commit()
        return db_activity


    def remove_activity(self, activity: Activity, *args, **kwargs):
        if not isinstance(activity, Activity):
            raise TypeError("'Activity' must be an instance of Activity")
        activity_db = self.get_activity(oid=activity.oid)[0]
        self.ses.delete(activity_db)
        self.ses.commit()

    def get_activity(self, activityNr:Union['str', None] = None, name:Union['str', None] = None, status:Union['str', None] = None, input:Union['str', None] = None, output:Union['str', None] = None, plannedStart:Union['str', None] = None, plannedEnd:Union['str', None] = None, plannedTenure:Union['str', None] = None, ActivityDoneFor:Union['str', None] = None, ActualCost:Union['Money', None] = None, oid: 'str' = None, *args, **kwargs) -> List[DBActivity]:

        query = self.ses.query(DBActivity)

        if oid != None:
            query = query.filter(DBActivity.oid == oid)
        if activityNr != None:
            query = query.filter(DBActivity.activityNr == activityNr)
        if name != None:
            query = query.filter(DBActivity.name == name)
        if status != None:
            query = query.filter(DBActivity.status == status)
        if input != None:
            query = query.filter(DBActivity.input == input)
        if output != None:
            query = query.filter(DBActivity.output == output)
        if plannedStart != None:
            query = query.filter(DBActivity.plannedStart == plannedStart)
        if plannedEnd != None:
            query = query.filter(DBActivity.plannedEnd == plannedEnd)
        if plannedTenure != None:
            query = query.filter(DBActivity.plannedTenure == plannedTenure)
        if ActivityDoneFor != None:
            query = query.filter(DBActivity.ActivityDoneFor == ActivityDoneFor)
        if ActualCost != None:
            query = query.filter(DBActivity.ActualCost == ActualCost)

        return query.all()


    def get_all_activity(self, *args, **kwargs) -> list[DBActivity]:
        return self.ses.query(DBActivity).all()

    def update_activity(self, activity: Activity, *args, **kwargs):
        if not isinstance(activity, Activity):
            raise TypeError("'activity' must be an instance of Activity")
        activity_db = self.get_activity(oid = activity.oid)[0]
        activity_db.activityNr = activity.activityNr
        activity_db.name = activity.name
        activity_db.status = activity.status
        activity_db.input = activity.input
        activity_db.output = activity.output
        activity_db.plannedStart = activity.plannedStart
        activity_db.plannedEnd = activity.plannedEnd
        activity_db.plannedTenure = activity.plannedTenure
        activity_db.ActivityDoneFor = activity.ActivityDoneFor
        activity_db.ActualCost_oid = activity.ActualCost
        self.ses.commit()

    # Begin methods for activity table

    # Begin methods for money table


    def save_money(self, money: Money, *args, **kwargs) -> 'DBMoney':
        if not isinstance(money, Money):
            raise TypeError("'Money' must be an instance of Money")

        db_money = DBMoney()
        db_money.oid = money.oid
        db_money.unit = money.unit
        db_money.value = money.value
        self.ses.add(db_money)
        self.ses.commit()
        return db_money


    def remove_money(self, money: Money, *args, **kwargs):
        if not isinstance(money, Money):
            raise TypeError("'Money' must be an instance of Money")
        money_db = self.get_money(oid=money.oid)[0]
        self.ses.delete(money_db)
        self.ses.commit()

    def get_money(self, unit:Union['str', None] = None, value:Union['str', None] = None, oid: 'str' = None, *args, **kwargs) -> List[DBMoney]:

        query = self.ses.query(DBMoney)

        if oid != None:
            query = query.filter(DBMoney.oid == oid)
        if unit != None:
            query = query.filter(DBMoney.unit == unit)
        if value != None:
            query = query.filter(DBMoney.value == value)

        return query.all()


    def get_all_money(self, *args, **kwargs) -> list[DBMoney]:
        return self.ses.query(DBMoney).all()

    def update_money(self, money: Money, *args, **kwargs):
        if not isinstance(money, Money):
            raise TypeError("'money' must be an instance of Money")
        money_db = self.get_money(oid = money.oid)[0]
        money_db.unit = money.unit
        money_db.value = money.value
        self.ses.commit()

    # Begin methods for money table

    # Begin methods for projectelement table


    def save_projectelement(self, projectelement: ProjectElement, *args, **kwargs) -> 'DBProjectElement':
        if not isinstance(projectelement, ProjectElement):
            raise TypeError("'ProjectElement' must be an instance of ProjectElement")

        db_projectelement = DBProjectElement()
        db_projectelement.oid = projectelement.oid
        db_projectelement.plannedDuration = projectelement.plannedDuration
        db_projectelement.actualDuration = projectelement.actualDuration
        db_projectelement.currentDuration = projectelement.currentDuration
        db_projectelement.status = projectelement.status
        db_projectelement.priority = projectelement.priority
        db_projectelement.timingConstraint = projectelement.timingConstraint
        self.ses.add(db_projectelement)
        self.ses.commit()
        return db_projectelement


    def remove_projectelement(self, projectelement: ProjectElement, *args, **kwargs):
        if not isinstance(projectelement, ProjectElement):
            raise TypeError("'ProjectElement' must be an instance of ProjectElement")
        projectelement_db = self.get_projectelement(oid=projectelement.oid)[0]
        self.ses.delete(projectelement_db)
        self.ses.commit()

    def get_projectelement(self, plannedDuration:Union['str', None] = None, actualDuration:Union['str', None] = None, currentDuration:Union['str', None] = None, status:Union['str', None] = None, priority:Union['str', None] = None, timingConstraint:Union['str', None] = None, oid: 'str' = None, *args, **kwargs) -> List[DBProjectElement]:

        query = self.ses.query(DBProjectElement)

        if oid != None:
            query = query.filter(DBProjectElement.oid == oid)
        if plannedDuration != None:
            query = query.filter(DBProjectElement.plannedDuration == plannedDuration)
        if actualDuration != None:
            query = query.filter(DBProjectElement.actualDuration == actualDuration)
        if currentDuration != None:
            query = query.filter(DBProjectElement.currentDuration == currentDuration)
        if status != None:
            query = query.filter(DBProjectElement.status == status)
        if priority != None:
            query = query.filter(DBProjectElement.priority == priority)
        if timingConstraint != None:
            query = query.filter(DBProjectElement.timingConstraint == timingConstraint)

        return query.all()


    def get_all_projectelement(self, *args, **kwargs) -> list[DBProjectElement]:
        return self.ses.query(DBProjectElement).all()

    def update_projectelement(self, projectelement: ProjectElement, *args, **kwargs):
        if not isinstance(projectelement, ProjectElement):
            raise TypeError("'projectelement' must be an instance of ProjectElement")
        projectelement_db = self.get_projectelement(oid = projectelement.oid)[0]
        projectelement_db.plannedDuration = projectelement.plannedDuration
        projectelement_db.actualDuration = projectelement.actualDuration
        projectelement_db.currentDuration = projectelement.currentDuration
        projectelement_db.status = projectelement.status
        projectelement_db.priority = projectelement.priority
        projectelement_db.timingConstraint = projectelement.timingConstraint
        self.ses.commit()

    # Begin methods for projectelement table

    # Begin methods for employee table


    def save_employee(self, employee: Employee, *args, **kwargs) -> 'DBEmployee':
        if not isinstance(employee, Employee):
            raise TypeError("'Employee' must be an instance of Employee")

        db_employee = DBEmployee()
        db_employee.oid = employee.oid
        db_employee.EmplNumber = employee.EmplNumber
        db_employee.LastName = employee.LastName
        db_employee.FirstName = employee.FirstName
        db_employee.MiddleName = employee.MiddleName
        db_employee.isManager = employee.isManager
        db_employee.RegionID = employee.RegionID
        db_employee.EmplStreet1 = employee.EmplStreet1
        db_employee.EmplStreet2 = employee.EmplStreet2
        db_employee.EmplPostalCode = employee.EmplPostalCode
        db_employee.EmplCity = employee.EmplCity
        db_employee.EmplSalary = employee.EmplSalary
        Responsiblefor = employee.Responsiblefor
        if Responsiblefor:
            db_Responsiblefor_list = self.get_region(oid = Responsiblefor)
            if len(db_Responsiblefor_list)>0:
                db_employee.Responsiblefor = db_Responsiblefor_list[0]
                db_employee.Responsiblefor_oid = db_Responsiblefor_list[0].oid
        self.ses.add(db_employee)
        self.ses.commit()
        return db_employee


    def remove_employee(self, employee: Employee, *args, **kwargs):
        if not isinstance(employee, Employee):
            raise TypeError("'Employee' must be an instance of Employee")
        employee_db = self.get_employee(oid=employee.oid)[0]
        self.ses.delete(employee_db)
        self.ses.commit()

    def get_employee(self, EmplNumber:Union['float', None] = None, LastName:Union['str', None] = None, FirstName:Union['str', None] = None, MiddleName:Union['str', None] = None, isManager:Union['str', None] = None, RegionID:Union['float', None] = None, EmplStreet1:Union['str', None] = None, EmplStreet2:Union['str', None] = None, EmplPostalCode:Union['str', None] = None, EmplCity:Union['str', None] = None, EmplSalary:Union['str', None] = None, Responsiblefor:Union['Region', None] = None, oid: 'str' = None, *args, **kwargs) -> List[DBEmployee]:

        query = self.ses.query(DBEmployee)

        if oid != None:
            query = query.filter(DBEmployee.oid == oid)
        if EmplNumber != None:
            query = query.filter(DBEmployee.EmplNumber == EmplNumber)
        if LastName != None:
            query = query.filter(DBEmployee.LastName == LastName)
        if FirstName != None:
            query = query.filter(DBEmployee.FirstName == FirstName)
        if MiddleName != None:
            query = query.filter(DBEmployee.MiddleName == MiddleName)
        if isManager != None:
            query = query.filter(DBEmployee.isManager == isManager)
        if RegionID != None:
            query = query.filter(DBEmployee.RegionID == RegionID)
        if EmplStreet1 != None:
            query = query.filter(DBEmployee.EmplStreet1 == EmplStreet1)
        if EmplStreet2 != None:
            query = query.filter(DBEmployee.EmplStreet2 == EmplStreet2)
        if EmplPostalCode != None:
            query = query.filter(DBEmployee.EmplPostalCode == EmplPostalCode)
        if EmplCity != None:
            query = query.filter(DBEmployee.EmplCity == EmplCity)
        if EmplSalary != None:
            query = query.filter(DBEmployee.EmplSalary == EmplSalary)
        if Responsiblefor != None:
            query = query.filter(DBEmployee.Responsiblefor == Responsiblefor)

        return query.all()


    def get_all_employee(self, *args, **kwargs) -> list[DBEmployee]:
        return self.ses.query(DBEmployee).all()

    def update_employee(self, employee: Employee, *args, **kwargs):
        if not isinstance(employee, Employee):
            raise TypeError("'employee' must be an instance of Employee")
        employee_db = self.get_employee(oid = employee.oid)[0]
        employee_db.EmplNumber = employee.EmplNumber
        employee_db.LastName = employee.LastName
        employee_db.FirstName = employee.FirstName
        employee_db.MiddleName = employee.MiddleName
        employee_db.isManager = employee.isManager
        employee_db.RegionID = employee.RegionID
        employee_db.EmplStreet1 = employee.EmplStreet1
        employee_db.EmplStreet2 = employee.EmplStreet2
        employee_db.EmplPostalCode = employee.EmplPostalCode
        employee_db.EmplCity = employee.EmplCity
        employee_db.EmplSalary = employee.EmplSalary
        employee_db.Responsiblefor_oid = employee.Responsiblefor
        self.ses.commit()

    # Begin methods for employee table

    # Begin methods for region table


    def save_region(self, region: Region, *args, **kwargs) -> 'DBRegion':
        if not isinstance(region, Region):
            raise TypeError("'Region' must be an instance of Region")

        db_region = DBRegion()
        db_region.oid = region.oid
        db_region.RegionID = region.RegionID
        db_region.RegionName = region.RegionName
        self.ses.add(db_region)
        self.ses.commit()
        return db_region


    def remove_region(self, region: Region, *args, **kwargs):
        if not isinstance(region, Region):
            raise TypeError("'Region' must be an instance of Region")
        region_db = self.get_region(oid=region.oid)[0]
        self.ses.delete(region_db)
        self.ses.commit()

    def get_region(self, RegionID:Union['float', None] = None, RegionName:Union['str', None] = None, oid: 'str' = None, *args, **kwargs) -> List[DBRegion]:

        query = self.ses.query(DBRegion)

        if oid != None:
            query = query.filter(DBRegion.oid == oid)
        if RegionID != None:
            query = query.filter(DBRegion.RegionID == RegionID)
        if RegionName != None:
            query = query.filter(DBRegion.RegionName == RegionName)

        return query.all()


    def get_all_region(self, *args, **kwargs) -> list[DBRegion]:
        return self.ses.query(DBRegion).all()

    def update_region(self, region: Region, *args, **kwargs):
        if not isinstance(region, Region):
            raise TypeError("'region' must be an instance of Region")
        region_db = self.get_region(oid = region.oid)[0]
        region_db.RegionID = region.RegionID
        region_db.RegionName = region.RegionName
        self.ses.commit()

    # Begin methods for region table

    # Begin methods for schedule table


    def save_schedule(self, schedule: Schedule, *args, **kwargs) -> 'DBSchedule':
        if not isinstance(schedule, Schedule):
            raise TypeError("'Schedule' must be an instance of Schedule")

        db_schedule = DBSchedule()
        db_schedule.oid = schedule.oid
        Employee = schedule.Employee
        if Employee:
            db_Employee_list = self.get_employee(oid = Employee)
            if len(db_Employee_list)>0:
                db_schedule.Employee = db_Employee_list[0]
                db_schedule.Employee_oid = db_Employee_list[0].oid
        for Activity in schedule.Activity:
            db_Activity_list = self.get_activity(oid = Activity)
            if len(db_Activity_list)>0:
                db_Activity = db_Activity_list[0]
                db_schedule.Activity.append(db_Activity)
        self.ses.add(db_schedule)
        self.ses.commit()
        return db_schedule


    def remove_schedule(self, schedule: Schedule, *args, **kwargs):
        if not isinstance(schedule, Schedule):
            raise TypeError("'Schedule' must be an instance of Schedule")
        schedule_db = self.get_schedule(oid=schedule.oid)[0]
        self.ses.delete(schedule_db)
        self.ses.commit()

    def get_schedule(self, Employee:Union['Employee', None] = None, Activity:Union['Activity', None] = None, oid: 'str' = None, *args, **kwargs) -> List[DBSchedule]:

        query = self.ses.query(DBSchedule)

        if oid != None:
            query = query.filter(DBSchedule.oid == oid)
        if Employee != None:
            query = query.filter(DBSchedule.Employee == Employee)
        if Activity != None:
            query = query.filter(DBSchedule.Activity == Activity)

        return query.all()


    def get_all_schedule(self, *args, **kwargs) -> list[DBSchedule]:
        return self.ses.query(DBSchedule).all()

    def update_schedule(self, schedule: Schedule, *args, **kwargs):
        if not isinstance(schedule, Schedule):
            raise TypeError("'schedule' must be an instance of Schedule")
        schedule_db = self.get_schedule(oid = schedule.oid)[0]
        schedule_db.Employee_oid = schedule.Employee
        schedule_db.Activity = []
        for Activity in schedule.Activity:
            Activity_db = self.get_activity(oid=Activity)[0]
            schedule_db.Activity.append(Activity_db)
        self.ses.commit()

    # Begin methods for schedule table

    # Begin methods for error table


    def save_error(self, error: Error, *args, **kwargs) -> 'DBError':
        if not isinstance(error, Error):
            raise TypeError("'Error' must be an instance of Error")

        db_error = DBError()
        db_error.oid = error.oid
        self.ses.add(db_error)
        self.ses.commit()
        return db_error


    def remove_error(self, error: Error, *args, **kwargs):
        if not isinstance(error, Error):
            raise TypeError("'Error' must be an instance of Error")
        error_db = self.get_error(oid=error.oid)[0]
        self.ses.delete(error_db)
        self.ses.commit()

    def get_error(self, oid: 'str' = None, *args, **kwargs) -> List[DBError]:

        query = self.ses.query(DBError)

        if oid != None:
            query = query.filter(DBError.oid == oid)

        return query.all()


    def get_all_error(self, *args, **kwargs) -> list[DBError]:
        return self.ses.query(DBError).all()

    def update_error(self, error: Error, *args, **kwargs):
        if not isinstance(error, Error):
            raise TypeError("'error' must be an instance of Error")
        error_db = self.get_error(oid = error.oid)[0]
        self.ses.commit()

    # Begin methods for error table


    def __getstate__(self) -> object:
        state: dict = super().__getstate__()  # type: ignore
        if "ses" in state:
            del state["ses"]
        return state

    def __setstate__(self, state: dict) -> None:
        self.__dict__.update(state)
        self.ses = self.create_db_session()
