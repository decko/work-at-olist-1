from django.urls import resolve


def test_telephone_endpoint_return_200_OK(client):
    """
    Test if root api url return 200 OK Http Status.
    """

    request = client.get('/')

    assert request.status_code == 200


def test_telephone_endpoint_namespace_definition(client):
    """
    Test if the namespace of root api url is defined as "core" and "index"
    as his name.
    """

    url = '/'
    resolved = resolve(url)

    assert resolved.namespace == "core"
    assert resolved.url_name == "index"
