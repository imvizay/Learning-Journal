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
# API-View (Class Based Views)
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


# GenericAPIView + mixins

from rest_framework import generics
from rest_framework import mixins
"""
generics.GenericAPIView provides iinfrastrucutre but not actions ,so for actions such as get update put patch delete we uses mixins module to inherit the action based classes such are

ListModeMixin = for all result associated of a class 
CreateModeMixin

ReteriveModeMixin, = to get out one specific result
UpdateModeMixin = to updated 
DestroyModeMixin = to delete 

Mixins = mixins provide us action regarding the api request whereas generics.GenericAPIView provides us infrastrucutre to work 

GenericAPIView provides us:
self.queryset()
self.request()
self.get.queryset()
self.get_serializer()
self.serializer_class()

pagination filtering authentication permission

"""

class GenericExample(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class GenericExampleDetails(mixins.UpdateModelMixin,mixins.RetrieveModelMixinmixins.DestroyModelMixin,generics.GenericAPIView):

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)