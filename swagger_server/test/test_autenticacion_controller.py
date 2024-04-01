# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_login import RequestLogin  # noqa: E501
from swagger_server.models.response_get_users import ResponseGetUsers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAutenticacionController(BaseTestCase):
    """AutenticacionController integration test stubs"""

    def test_login_user(self):
        """Test case for login_user

        
        """
        body = RequestLogin()
        response = self.client.open(
            '/api/autentication-ms/v1.0//login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
