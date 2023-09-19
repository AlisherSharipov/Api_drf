from rest_framework import generics, mixins
from rest_framework import viewsets
from django.forms.models import model_to_dict
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser,IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer

'''class WomenViewSet(viewsets.ModelViewSet):  # ReadOnlyModelViewSet
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats':[c.name for c in cats]})#[c.name for c in cats]
                                                        # for c in cats:
                                                        #   c.name
'''


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
   # permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )#IsOwnerOrReadOnly
    #authentication_classes = (TokenAuthentication, )


class WomenAPIDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer  
    permission_classes = (IsAdminOrReadOnly, )
