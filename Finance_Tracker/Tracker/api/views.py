from rest_framework.viewsets import ModelViewSet
from ..models import Finance_Info
from .serializers import PostSerializers

class PostViewSet(ModelViewSet):
    queryset = Finance_Info.objects.all()
    serializer_class = PostSerializers

