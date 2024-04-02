import connexion
import six

from swagger_server.models.request_login import RequestLogin  # noqa: E501
from swagger_server.models.response_get_users import ResponseGetUsers  # noqa: E501
from swagger_server import util
from swagger_server.use_cases.autentication_use_case import AutenticationUseCase
from swagger_server.validators.validators import Validator

def login_user(body=None):  # noqa: E501
    """login_user

    Inicio de sesión # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseGetUsers
    """
    if connexion.request.is_json:
        body = RequestLogin.from_dict(connexion.request.get_json())  # noqa: E501

        flag, message = Validator.validar_login(body)

        if flag:
            use_case = AutenticationUseCase()
            resultado = use_case.login(body)
        else:
            resultado = message

    return resultado
