from django.urls import resolve
from rest_framework import status


def test_telephone_endpoint_return_200_OK(client):
    """
    Test if root url(/) return 200 OK HTTP Status.
    """

    request = client.get('/')

    assert request.status_code == 200


def test_telephone_endpoint_namespace_definition(client):
    """
    Test if the namespace of root url(/) is defined as "core" and "index"
    as his name.
    """

    url = '/'
    resolved = resolve(url)

    assert resolved.namespace == "core"
    assert resolved.url_name == "index"


def test_telephone_api_endpoint(client):
    """
    Test if root api url(/api/v1/) return 200 Ok HTTP Status.
    """

    url = '/api/v1/'
    request = client.get(url)

    assert request.status_code == status.HTTP_200_OK


def test_telephone_api_namespace_definition(client):
    """
    Test if the namespace of root api url(/api/v1/) is defined as "core" and
    "api" as his name.
    """

    url = '/api/v1/'
    resolved = resolve(url)

    assert resolved.namespace == "core"
    assert resolved.url_name == "api"
