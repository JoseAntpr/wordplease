from rest_framework import serializers

from blogs.models import Blog, Post


class blogSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='blog_detail', lookup_field="slug")

    class Meta:
        model = Blog
        fields = ("url", "name", "user", "created_at")
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "media", "summary", "created_at")
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
