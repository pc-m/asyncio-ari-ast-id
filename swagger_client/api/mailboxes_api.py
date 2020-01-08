# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MailboxesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def mailboxes_get(self, **kwargs):  # noqa: E501
        """List all mailboxes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mailboxes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: list[Mailbox]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mailboxes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.mailboxes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def mailboxes_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all mailboxes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mailboxes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: list[Mailbox]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mailboxes_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mailboxes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Mailbox]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def mailboxes_mailbox_name_delete(self, mailbox_name, **kwargs):  # noqa: E501
        """Destroy a mailbox.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mailboxes_mailbox_name_delete(mailbox_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mailbox_name: Name of the mailbox (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mailboxes_mailbox_name_delete_with_http_info(mailbox_name, **kwargs)  # noqa: E501
        else:
            (data) = self.mailboxes_mailbox_name_delete_with_http_info(mailbox_name, **kwargs)  # noqa: E501
            return data

    def mailboxes_mailbox_name_delete_with_http_info(self, mailbox_name, **kwargs):  # noqa: E501
        """Destroy a mailbox.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mailboxes_mailbox_name_delete_with_http_info(mailbox_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mailbox_name: Name of the mailbox (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mailbox_name', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mailboxes_mailbox_name_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mailbox_name' is set
        if ('mailbox_name' not in params or
                params['mailbox_name'] is None):
            raise ValueError("Missing the required parameter `mailbox_name` when calling `mailboxes_mailbox_name_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mailbox_name' in params:
            path_params['mailboxName'] = params['mailbox_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mailboxes/{mailboxName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def mailboxes_mailbox_name_get(self, mailbox_name, **kwargs):  # noqa: E501
        """Retrieve the current state of a mailbox.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mailboxes_mailbox_name_get(mailbox_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mailbox_name: Name of the mailbox (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Mailbox
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mailboxes_mailbox_name_get_with_http_info(mailbox_name, **kwargs)  # noqa: E501
        else:
            (data) = self.mailboxes_mailbox_name_get_with_http_info(mailbox_name, **kwargs)  # noqa: E501
            return data

    def mailboxes_mailbox_name_get_with_http_info(self, mailbox_name, **kwargs):  # noqa: E501
        """Retrieve the current state of a mailbox.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mailboxes_mailbox_name_get_with_http_info(mailbox_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mailbox_name: Name of the mailbox (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Mailbox
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mailbox_name', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mailboxes_mailbox_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mailbox_name' is set
        if ('mailbox_name' not in params or
                params['mailbox_name'] is None):
            raise ValueError("Missing the required parameter `mailbox_name` when calling `mailboxes_mailbox_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mailbox_name' in params:
            path_params['mailboxName'] = params['mailbox_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mailboxes/{mailboxName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Mailbox',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def mailboxes_mailbox_name_put(self, mailbox_name, old_messages, new_messages, **kwargs):  # noqa: E501
        """Change the state of a mailbox. (Note - implicitly creates the mailbox).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mailboxes_mailbox_name_put(mailbox_name, old_messages, new_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mailbox_name: Name of the mailbox (required)
        :param int old_messages: Count of old messages in the mailbox (required)
        :param int new_messages: Count of new messages in the mailbox (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mailboxes_mailbox_name_put_with_http_info(mailbox_name, old_messages, new_messages, **kwargs)  # noqa: E501
        else:
            (data) = self.mailboxes_mailbox_name_put_with_http_info(mailbox_name, old_messages, new_messages, **kwargs)  # noqa: E501
            return data

    def mailboxes_mailbox_name_put_with_http_info(self, mailbox_name, old_messages, new_messages, **kwargs):  # noqa: E501
        """Change the state of a mailbox. (Note - implicitly creates the mailbox).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mailboxes_mailbox_name_put_with_http_info(mailbox_name, old_messages, new_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mailbox_name: Name of the mailbox (required)
        :param int old_messages: Count of old messages in the mailbox (required)
        :param int new_messages: Count of new messages in the mailbox (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mailbox_name', 'old_messages', 'new_messages', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mailboxes_mailbox_name_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mailbox_name' is set
        if ('mailbox_name' not in params or
                params['mailbox_name'] is None):
            raise ValueError("Missing the required parameter `mailbox_name` when calling `mailboxes_mailbox_name_put`")  # noqa: E501
        # verify the required parameter 'old_messages' is set
        if ('old_messages' not in params or
                params['old_messages'] is None):
            raise ValueError("Missing the required parameter `old_messages` when calling `mailboxes_mailbox_name_put`")  # noqa: E501
        # verify the required parameter 'new_messages' is set
        if ('new_messages' not in params or
                params['new_messages'] is None):
            raise ValueError("Missing the required parameter `new_messages` when calling `mailboxes_mailbox_name_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mailbox_name' in params:
            path_params['mailboxName'] = params['mailbox_name']  # noqa: E501

        query_params = []
        if 'old_messages' in params:
            query_params.append(('oldMessages', params['old_messages']))  # noqa: E501
        if 'new_messages' in params:
            query_params.append(('newMessages', params['new_messages']))  # noqa: E501

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mailboxes/{mailboxName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)