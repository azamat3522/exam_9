from rest_framework.serializers import ModelSerializer
from webapp.models import Comment, Photo


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'photo', 'created_at',
                  'author']


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'photo', 'signature', 'created_at', 'author', 'count_likes']