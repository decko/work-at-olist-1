from datetime import datetime

from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def Return200Ok(request, **kwargs):
    call_start_record = {
            "id",
            "type",
            "timestamp",
            "call_id",
            "source",
            "destination",
    }

    return Response(data=[call_start_record,], status=200)
