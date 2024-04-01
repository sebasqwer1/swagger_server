import connexion
import six

from swagger_server.models.request_login import RequestLogin  # noqa: E501
from swagger_server.models.response_get_users import ResponseGetUsers  # noqa: E501
from swagger_server import util


def login_user(body=None):  # noqa: E501
    """login_user

    Inicio de sesión # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseGetUsers
    """
    if connexion.request.is_json:
        body = RequestLogin.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
