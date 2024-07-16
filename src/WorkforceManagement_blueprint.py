
from flask import Blueprint, request, make_response, send_file
from digitalpy.core.network.impl.network_flask_http_blueprints import BlueprintCommunicator


page = Blueprint('WorkforceManagement', __name__)

@page.route('/Employee', methods=["POST"])
def POSTEmployee():
    """Creates a new employee record."""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"POSTEmployee",
        	"^Employee",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Employee', methods=["DELETE"])
def DELETEEmployee():
    """Deletes an existing employee record based on the provided ID."""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"DELETEEmployee",
        	"^Employee",
        	{
        "ID": request.args.get('ID'),
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Employee', methods=["GET"])
def GETEmployee():
    """Retrieves a list of all employees."""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETEmployee",
        	"^Employee",
        	{
        }) # type: ignore
        return response.get_value("message"), 200
    except Exception as e:
    	return str(e), 500
@page.route('/Employee', methods=["PATCH"])
def PATCHEmployee():
    """Updates an existing employee record."""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"PATCHEmployee",
        	"^Employee",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Region', methods=["POST"])
def POSTRegion():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"POSTRegion",
        	"^Region",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Region', methods=["DELETE"])
def DELETERegion():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"DELETERegion",
        	"^Region",
        	{
        "ID": request.args.get('ID'),
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Region', methods=["GET"])
def GETRegion():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETRegion",
        	"^Region",
        	{
        }) # type: ignore
        return response.get_value("message"), 200
    except Exception as e:
    	return str(e), 500
@page.route('/Region', methods=["PATCH"])
def PATCHRegion():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"PATCHRegion",
        	"^Region",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Money', methods=["POST"])
def POSTMoney():
    """Creates a new Money record."""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"POSTMoney",
        	"^Money",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Money', methods=["DELETE"])
def DELETEMoney():
    """Deletes an existing Money record based on the provided ID."""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"DELETEMoney",
        	"^Money",
        	{
        "ID": request.args.get('ID'),
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Money', methods=["GET"])
def GETMoney():
    """Retrieves a list of all Money"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETMoney",
        	"^Money",
        	{
        }) # type: ignore
        return response.get_value("message"), 200
    except Exception as e:
    	return str(e), 500
@page.route('/Money', methods=["PATCH"])
def PATCHMoney():
    """Updates an existing Money record."""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"PATCHMoney",
        	"^Money",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Money/<id>', methods=["GET"])
def GETMoneyId(id,):
    """retrieve an existing Money record based on the provided ID."""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETMoneyId",
        	"^Money^",
        	{
        "ID": request.args.get('ID'),
        "id": id,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Activity/Metric/TimeEfficiency', methods=["POST"])
def POSTActivityMetricTimeEfficiency():
    """Activity Metric TimeEfficiency"""
    try:
        # send data to the NetworkInterface
        BlueprintCommunicator().send_message_async(
        	"POSTActivityMetricTimeEfficiency",
        	"^Activity^Metric^TimeEfficiency",
        	{
        }) # type: ignore
        return '', 200
    except Exception as e:
    	return str(e), 500
@page.route('/Employee/<id>', methods=["GET"])
def GETEmployeeId(id,):
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETEmployeeId",
        	"^Employee^",
        	{
        "ID": request.args.get('ID'),
        "id": id,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Schedule', methods=["POST"])
def POSTSchedule():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"POSTSchedule",
        	"^Schedule",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Schedule', methods=["DELETE"])
def DELETESchedule():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"DELETESchedule",
        	"^Schedule",
        	{
        "ID": request.args.get('ID'),
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Schedule', methods=["GET"])
def GETSchedule():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETSchedule",
        	"^Schedule",
        	{
        }) # type: ignore
        return response.get_value("message"), 200
    except Exception as e:
    	return str(e), 500
@page.route('/Schedule', methods=["PATCH"])
def PATCHSchedule():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"PATCHSchedule",
        	"^Schedule",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Region/<id>', methods=["GET"])
def GETRegionId(id,):
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETRegionId",
        	"^Region^",
        	{
        "ID": request.args.get('ID'),
        "id": id,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Schedule/<id>', methods=["GET"])
def GETScheduleId(id,):
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETScheduleId",
        	"^Schedule^",
        	{
        "ID": request.args.get('ID'),
        "id": id,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Activity', methods=["POST"])
def POSTActivity():
    """Activity creation"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"POSTActivity",
        	"^Activity",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Activity', methods=["DELETE"])
def DELETEActivity():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"DELETEActivity",
        	"^Activity",
        	{
        "ID": request.args.get('ID'),
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Activity', methods=["GET"])
def GETActivity():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETActivity",
        	"^Activity",
        	{
        }) # type: ignore
        return response.get_value("message"), 200
    except Exception as e:
    	return str(e), 500
@page.route('/Activity', methods=["PATCH"])
def PATCHActivity():
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"PATCHActivity",
        	"^Activity",
        	{
        "body": request.data,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
@page.route('/Activity/<id>', methods=["GET"])
def GETActivityId(id,):
    """TODO"""
    try:
        # send data to the NetworkInterface
        response = BlueprintCommunicator().send_message_sync(
        	"GETActivityId",
        	"^Activity^",
        	{
        "ID": request.args.get('ID'),
        "id": id,
        }) # type: ignore
        return response.get_value("message")[0], 200
    except Exception as e:
    	return str(e), 500
