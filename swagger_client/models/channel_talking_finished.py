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


class ChannelTalkingFinished(object):
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
        'duration': 'int'
    }

    attribute_map = {
        'channel': 'channel',
        'duration': 'duration'
    }

    def __init__(self, channel=None, duration=None):  # noqa: E501
        """ChannelTalkingFinished - a model defined in Swagger"""  # noqa: E501

        self._channel = None
        self._duration = None
        self.discriminator = None

        self.channel = channel
        self.duration = duration

    @property
    def channel(self):
        """Gets the channel of this ChannelTalkingFinished.  # noqa: E501

        The channel on which talking completed.  # noqa: E501

        :return: The channel of this ChannelTalkingFinished.  # noqa: E501
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelTalkingFinished.

        The channel on which talking completed.  # noqa: E501

        :param channel: The channel of this ChannelTalkingFinished.  # noqa: E501
        :type: Channel
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def duration(self):
        """Gets the duration of this ChannelTalkingFinished.  # noqa: E501

        The length of time, in milliseconds, that talking was detected on the channel  # noqa: E501

        :return: The duration of this ChannelTalkingFinished.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ChannelTalkingFinished.

        The length of time, in milliseconds, that talking was detected on the channel  # noqa: E501

        :param duration: The duration of this ChannelTalkingFinished.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

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
        if issubclass(ChannelTalkingFinished, dict):
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
        if not isinstance(other, ChannelTalkingFinished):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
