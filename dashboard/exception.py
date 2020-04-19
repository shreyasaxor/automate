from rest_framework.exceptions import APIException

class IncorrectData(APIException):
    status_code = 400
    default_detail = 'Wrong format data, try again later.'
    default_code = 'bad_request'

class IncorrectAuthCredentials(APIException):
    status_code = 401
    default_detail = 'Wrong data, .'
    default_code = 'Unauthorized'