# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ExternalMedia(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel': 'Channel',
        'local_address': 'str',
        'local_port': 'int'
    }

    attribute_map = {
        'channel': 'channel',
        'local_address': 'local_address',
        'local_port': 'local_port'
    }

    def __init__(self, channel=None, local_address=None, local_port=None):  # noqa: E501
        """ExternalMedia - a model defined in Swagger"""  # noqa: E501

        self._channel = None
        self._local_address = None
        self._local_port = None
        self.discriminator = None

        self.channel = channel
        if local_address is not None:
            self.local_address = local_address
        if local_port is not None:
            self.local_port = local_port

    @property
    def channel(self):
        """Gets the channel of this ExternalMedia.  # noqa: E501

        The Asterisk channel representing the external media  # noqa: E501

        :return: The channel of this ExternalMedia.  # noqa: E501
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ExternalMedia.

        The Asterisk channel representing the external media  # noqa: E501

        :param channel: The channel of this ExternalMedia.  # noqa: E501
        :type: Channel
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def local_address(self):
        """Gets the local_address of this ExternalMedia.  # noqa: E501

        The local ip address used  # noqa: E501

        :return: The local_address of this ExternalMedia.  # noqa: E501
        :rtype: str
        """
        return self._local_address

    @local_address.setter
    def local_address(self, local_address):
        """Sets the local_address of this ExternalMedia.

        The local ip address used  # noqa: E501

        :param local_address: The local_address of this ExternalMedia.  # noqa: E501
        :type: str
        """

        self._local_address = local_address

    @property
    def local_port(self):
        """Gets the local_port of this ExternalMedia.  # noqa: E501

        The local ip port used  # noqa: E501

        :return: The local_port of this ExternalMedia.  # noqa: E501
        :rtype: int
        """
        return self._local_port

    @local_port.setter
    def local_port(self, local_port):
        """Sets the local_port of this ExternalMedia.

        The local ip port used  # noqa: E501

        :param local_port: The local_port of this ExternalMedia.  # noqa: E501
        :type: int
        """

        self._local_port = local_port

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ExternalMedia, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalMedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
