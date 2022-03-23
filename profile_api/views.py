from email import message
from lib2to3.pgen2 import token
from urllib import response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profile_api import serializers
from profile_api import models
from profile_api import permissions

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    """configer api view to have the serializer class"""
    serializer_class = serializers.HelloSerializer


    def list(self, request):
         a_viewset =[
            'uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code',
        ]
        
         return Response({'message':'Hello!','a_viewset' : a_viewset})

    def create(self,request):
        """create a new hello message"""    
        print('xdddd')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello! {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve (self,request,pk=None):
        """Handle Getting an object by its ID"""
        return Response({'http_method':'GET'})


    def update (self,request,pk=None):
        """Handle Updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update (self,request,pk=None):
        """Handle Updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy (self,request,pk=None):
        """Handle Deleting an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

    

      
        