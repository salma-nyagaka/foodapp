import json

from rest_framework.exceptions import ErrorDetail
from rest_framework.renderers import JSONRenderer


class RequestJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code

        # Checks if our status code is successful
        if status_code == 200 or status_code == 201:
            return json.dumps({
                'status': True,
                'message': data.get('message', None),
                'data': data.get('data', [])
            })
        else:
            response_data = format_errors(data)
            return json.dumps({
                'status': False,
                'error': response_data[0]
            })


def format_errors(data):
    """
    Function that formats error messages
    Args:
        data(dict): error dict or error list
    Returns:
        error(list): formated errors
    """

    formatted_data = []

    if 'message' in data:
        formatted_data.append(data['message'])
    else:
        formatted_data.append(data)
    return formatted_data
