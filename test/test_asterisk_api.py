# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.asterisk_api import AsteriskApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAsteriskApi(unittest.TestCase):
    """AsteriskApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.asterisk_api.AsteriskApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_asterisk_config_dynamic_config_class_object_type_id_delete(self):
        """Test case for asterisk_config_dynamic_config_class_object_type_id_delete

        Delete a dynamic configuration object.  # noqa: E501
        """
        pass

    def test_asterisk_config_dynamic_config_class_object_type_id_get(self):
        """Test case for asterisk_config_dynamic_config_class_object_type_id_get

        Retrieve a dynamic configuration object.  # noqa: E501
        """
        pass

    def test_asterisk_config_dynamic_config_class_object_type_id_put(self):
        """Test case for asterisk_config_dynamic_config_class_object_type_id_put

        Create or update a dynamic configuration object.  # noqa: E501
        """
        pass

    def test_asterisk_info_get(self):
        """Test case for asterisk_info_get

        Gets Asterisk system information.  # noqa: E501
        """
        pass

    def test_asterisk_logging_get(self):
        """Test case for asterisk_logging_get

        Gets Asterisk log channel information.  # noqa: E501
        """
        pass

    def test_asterisk_logging_log_channel_name_delete(self):
        """Test case for asterisk_logging_log_channel_name_delete

        Deletes a log channel.  # noqa: E501
        """
        pass

    def test_asterisk_logging_log_channel_name_post(self):
        """Test case for asterisk_logging_log_channel_name_post

        Adds a log channel.  # noqa: E501
        """
        pass

    def test_asterisk_logging_log_channel_name_rotate_put(self):
        """Test case for asterisk_logging_log_channel_name_rotate_put

        Rotates a log channel.  # noqa: E501
        """
        pass

    def test_asterisk_modules_get(self):
        """Test case for asterisk_modules_get

        List Asterisk modules.  # noqa: E501
        """
        pass

    def test_asterisk_modules_module_name_delete(self):
        """Test case for asterisk_modules_module_name_delete

        Unload an Asterisk module.  # noqa: E501
        """
        pass

    def test_asterisk_modules_module_name_get(self):
        """Test case for asterisk_modules_module_name_get

        Get Asterisk module information.  # noqa: E501
        """
        pass

    def test_asterisk_modules_module_name_post(self):
        """Test case for asterisk_modules_module_name_post

        Load an Asterisk module.  # noqa: E501
        """
        pass

    def test_asterisk_modules_module_name_put(self):
        """Test case for asterisk_modules_module_name_put

        Reload an Asterisk module.  # noqa: E501
        """
        pass

    def test_asterisk_ping_get(self):
        """Test case for asterisk_ping_get

        Response pong message.  # noqa: E501
        """
        pass

    def test_asterisk_variable_get(self):
        """Test case for asterisk_variable_get

        Get the value of a global variable.  # noqa: E501
        """
        pass

    def test_asterisk_variable_post(self):
        """Test case for asterisk_variable_post

        Set the value of a global variable.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
