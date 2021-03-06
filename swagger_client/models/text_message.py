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


class TextMessage(object):
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
        'body': 'str',
        '_from': 'str',
        'to': 'str',
        'variables': 'list[TextMessageVariable]'
    }

    attribute_map = {
        'body': 'body',
        '_from': 'from',
        'to': 'to',
        'variables': 'variables'
    }

    def __init__(self, body=None, _from=None, to=None, variables=None):  # noqa: E501
        """TextMessage - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self.__from = None
        self._to = None
        self._variables = None
        self.discriminator = None

        self.body = body
        self._from = _from
        self.to = to
        if variables is not None:
            self.variables = variables

    @property
    def body(self):
        """Gets the body of this TextMessage.  # noqa: E501

        The text of the message.  # noqa: E501

        :return: The body of this TextMessage.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this TextMessage.

        The text of the message.  # noqa: E501

        :param body: The body of this TextMessage.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def _from(self):
        """Gets the _from of this TextMessage.  # noqa: E501

        A technology specific URI specifying the source of the message. For sip and pjsip technologies, any SIP URI can be specified. For xmpp, the URI must correspond to the client connection being used to send the message.  # noqa: E501

        :return: The _from of this TextMessage.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this TextMessage.

        A technology specific URI specifying the source of the message. For sip and pjsip technologies, any SIP URI can be specified. For xmpp, the URI must correspond to the client connection being used to send the message.  # noqa: E501

        :param _from: The _from of this TextMessage.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this TextMessage.  # noqa: E501

        A technology specific URI specifying the destination of the message. Valid technologies include sip, pjsip, and xmp. The destination of a message should be an endpoint.  # noqa: E501

        :return: The to of this TextMessage.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this TextMessage.

        A technology specific URI specifying the destination of the message. Valid technologies include sip, pjsip, and xmp. The destination of a message should be an endpoint.  # noqa: E501

        :param to: The to of this TextMessage.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def variables(self):
        """Gets the variables of this TextMessage.  # noqa: E501

        Technology specific key/value pairs associated with the message.  # noqa: E501

        :return: The variables of this TextMessage.  # noqa: E501
        :rtype: list[TextMessageVariable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this TextMessage.

        Technology specific key/value pairs associated with the message.  # noqa: E501

        :param variables: The variables of this TextMessage.  # noqa: E501
        :type: list[TextMessageVariable]
        """

        self._variables = variables

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
        if issubclass(TextMessage, dict):
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
        if not isinstance(other, TextMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
