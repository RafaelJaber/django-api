from rest_framework.viewsets import ModelViewSet
from ..models import Comment
from .serializers import CommentSerializers


class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
