"DRF api VIEWS"

from rest_framework import status

"04 ways to create views"

# Functional ,
# APIView, 
# GenericAPIView + mixins, 
# ViewSets + routers





# Functional based views

from rest_framework.decorators import api_view,permission_classes,throttle_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.throttling import UserRateThrottle

@api_view(["GET","POST","PUT","DELETE"])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])

def apiList(request):
    """Functional based views"""
    pass


# Class Based Views

"APIView is the foundation of all class based views in the drf"

from rest_framework.views import APIView

class ProductList(APIView):
    """ APIView developer need to manually write logic """
    def get(self,request):
        pass

    def post(self,request):
        pass

class ProductDetails(APIView):
    
    def get(self,request,pk):
        pass

    def put(self,request,pk):
        pass

    def delete(self,request,pk):
        pass



