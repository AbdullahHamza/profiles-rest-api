from rest_framework.views import APIView

from rest_framework.response import Response

class HelloApiView(APIView):
    """test API View"""

    def get(self,request,format=None):
        """Returns a list of API views features"""

        an_apiview =[
            'uses http methods as function (get, post, pathc, put, delete',
            'is similar to django traditional View',
        ]

        return Response({'message':'Hello!','an_apiview' : an_apiview})