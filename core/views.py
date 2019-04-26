from datetime import datetime

from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def Return200Ok(request, **kwargs):
    call_start_record = {
            'id': 1,
            'type': 'start',
            'timestamp': datetime.now(),
            'call_id': 1,
            'source': '11111111111',
            'destination': '22222222222',
    }

    call_stop_record = {
            'id': 2,
            'type': 'stop',
            'timestamp': datetime.now(),
            'call_id': 1,
    }

    return Response(data=[call_start_record, call_stop_record], status=200)
