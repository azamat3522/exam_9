from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import CommentSerializer, PhotoSerializer
from webapp.models import Comment, Photo


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action not in ['update', 'partial_update', 'destroy', 'create']:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(methods=['post'], detail=True)
    def like_up(self, request, pk=None):
        photo = self.get_object()
        photo.count_likes += 1
        photo.save()
        return Response({'id': photo.pk, 'count_likes': photo.count_likes})

    @action(methods=['post'], detail=True)
    def like_down(self, request, pk=None):
        photo = self.get_object()
        photo.count_likes -= 1
        photo.save()
        return Response({'id': photo.pk, 'count_likes': photo.count_likes})


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer