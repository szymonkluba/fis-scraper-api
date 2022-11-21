from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = "Service temporarily unavailable, try again later."
    default_code = "service_unavailable"


class SomethingWentWrong(APIException):
    status_code = 500
    default_detail = "Something went wrong:/"
    default_code = "something_went_wrong"


class RaceNotFound(APIException):
    status_code = 404
    default_detail = "Race with such FIS ID cannot be found."
    default_code = "race_not_found"


class RaceDataEmpty(APIException):
    status_code = 404
    default_detail = "Race data is empty."
    default_code = "race_data_empty"


class InvalidDataProvided(APIException):
    status_code = 400
    default_detail = "Invalid data provided."
    default_code = "invalid_data"


class TooManyRequests(APIException):
    status_code = 429
    default_detail = "Too many requests, try again later."
    default_code = "too_many_requests"


class Unauthorized(APIException):
    status_code = 401
    default_detail = "Authorization error."
    default_code = "unauthorized"


class CommunicationError(APIException):
    status_code = 400
    default_detail = "Storage communication error."
    default_code = "communication_error"


class AccessDenied(APIException):
    status_code = 403
    default_detail = "Cannot access the resource:("
    default_code = "forbidden"


class NoTablesFound(APIException):
    status_code = 404
    default_detail = "No tables found:("
    default_code = "no_tables_found"


class NoDetailsView(APIException):
    status_code = 400
    default_detail = "No details view for this race"
    default_code = "no_details_view"
