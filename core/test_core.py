from datetime import datetime

from django.urls import resolve, reverse

from rest_framework import status


def test_telephone_endpoint_return_200_OK(client):
    """
    Test if root url(/) return 200 OK HTTP Status.
    """

    request = client.get('/')

    assert request.status_code == 200


def test_telephone_endpoint_namespace_definition(client):
    """
    Test if the namespace of root url(/) is defined as "core" and "root"
    as his name.
    """

    url = '/'
    resolved = resolve(url)

    assert resolved.namespace == "core"
    assert resolved.url_name == "root"


def test_telephone_api_endpoint(client):
    """
    Test if root api url(/api/v1/) return 200 Ok HTTP Status.
    """

    url = '/api/v1/'
    request = client.get(url)

    assert request.status_code == status.HTTP_200_OK


def test_telephone_api_namespace_definition(client):
    """
    Test if the namespace of root api url(/api/v1/) is defined as "api" and
    "root" as his name.
    """

    url = '/api/v1/'
    resolved = resolve(url)

    assert resolved.namespace == "api"
    assert resolved.url_name == "root"


def test_telephone_calls_api_endpoint(client):
    """
    Test if calls api url(/api/v1/calls/) return 200 Ok HTTP Status.
    """

    url = '/api/v1/calls/'
    request = client.get(url)

    assert request.status_code == status.HTTP_200_OK


def test_telephone_calls_api_namespace_definition(client):
    """
    Test if the namespace of call api url (/api/v1/calls/) is defined as
    "api" and "calls" as his name.
    """

    url = '/api/v1/calls/'
    resolved = resolve(url)

    assert resolved.namespace == "api"
    assert resolved.url_name == "calls"


def test_telephone_api_returning_a_empty_list(client):
    """
    Test if a GET request return an list from api endpoint.
    """

    url = reverse('api:calls')

    request = client.get(url)

    assert isinstance(request.data, list)


def test_fields_returned_on_a_calls_api_request(client):
    """
    Test which fields return on a GET request to Calls API. The response should
    obey this format:
        {
          "id":  // Record unique identificator;
          "type":  // Indicate if it's a call "start" or "end" record;
          "timestamp":  // The timestamp of when the event occured;
          "call_id":  // Unique for each call record pair;
          "source":  // The subscriber phone number that originated the call;
          "destination":  // The phone number receiving the call.
        }
    """

    fields = {'id', 'type', 'timestamp', 'call_id', 'source', 'destination'}

    url = reverse('api:calls')

    request = client.get(url)

    assert set(request.data[0]).issuperset(fields)


def test_field_type_returned_on_a_calls_api_request(client):
    """
    Test each field type that came on a Calls API response.
    They must obey this format:
        {
          "id":  int,
          "type":  str,
          "timestamp":  datetime,
          "call_id":  int,
          "source":  str
          "destination":  str
        }
    """

    fields = {
        "id":  int,
        "type":  str,
        "timestamp":  datetime,
        "call_id":  int,
        "source":  str,
        "destination":  str,
    }

    url = reverse('api:calls')

    request = client.get(url)

    for field, type in fields.items():
        assert isinstance(request.data[0][field], type)
