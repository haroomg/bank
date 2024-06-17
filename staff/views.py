from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import CreateStaffSerializer

class StaffView (APIView):

    def post(self, request):
        
        serializer = CreateStaffSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        
        else:
            return Response(serializer.errors, status=400)
        