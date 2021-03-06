from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField("get_username")
    class Meta:
        model = Post
        fields = ['id','title','message','group','username','updated_at']

    def get_username(self,post):
        username = post.user.username
        return username



class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','message']