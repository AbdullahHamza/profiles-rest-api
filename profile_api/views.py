from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers

class HelloApiView(APIView):
    """test API View"""

    """configer api view to have the serializer class"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of API views features"""

        an_apiview =[
            'uses http methods as function (get, post, pathc, put, delete',
            'is similar to django traditional View',
            'bla bla bla',
        ]

        return Response({'message':'Hello!','an_apiview' : an_apiview})

    def post (self,request):
        """create hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello! {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put (self,request):
        """Handle Updating an object"""
        return Response({'method':'PUT'})


    def patch (self,request):
        """Handle a partial Updating an object"""
        return Response({'method':'PATCH'})

    def delete (self,request):
        """Delete an object"""
        return Response({'method':'DELETE'})
