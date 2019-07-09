from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import TouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):

    serializer_class = TouristSpotSerializer

    def get_queryset(self):
        return TouristSpot.objects.filter(status=True)
    """
    # Sempre que fizer um get na aplicação, será disparado esse método list, onde pode se reescrever o comportamento da aplicação
    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})

    # Sempre que for dado o post podemos alterar o comportamento da api nesse método
    def create(self, request, *args, **kwargs):
        return Response({'Hellow': request.data['name']})

    # Sempre que for chamado o delete, podemos reescrever o comportamento dele atraez do destroy
    def destroy(self, request, *args, **kwargs):
        return Response({'key': kwargs['pk']})

    # Sempre que for chamado o PUT, podemos reescrever com esse metodo
    def update(self, request, *args, **kwargs):
        return Response({'update': request.data['description']})

    # Sempre que for chamado o get com o id, podemos reescrever com esse método
    def retrieve(self, request, *args, **kwargs):
        return Response({'get_data': request.data['name']})

    # Sempre que for chamado o patch, podemos reescrever com esse método
    def partial_update(self, request, *args, **kwargs):
        return Response({'Partial Update': request.data['name']})
    """