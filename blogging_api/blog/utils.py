
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Handle PermissionError
    if isinstance(exc, PermissionError):
        return Response({'detail': str(exc)}, status=status.HTTP_403_FORBIDDEN)

    # Return the original response for unhandled exceptions
    return response
