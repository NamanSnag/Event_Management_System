from typing import Optional, Dict, List
from rest_framework import status
from rest_framework.response import Response

def get_response(
    data: Optional[Dict] = None,
    message: str = None,
    error: str = None,
    error_list: Optional[List[str]] = None,
    status_code=status.HTTP_200_OK,
    headers: Optional[Dict] = None,
) -> Response:
    response_data = {
        "data": data,
        "message": message,
        "error": error,
        "error_list": error_list,
        "status": status_code,
    }
    return Response(
        response_data,
        status=status_code,
        headers=headers,
    )
