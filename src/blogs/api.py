from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog, Post
from blogs.serializers import blogSerializer, PostSerializer,PostListSerializer
from blogs.permissions import PostPermission


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("user__username",)
    ordering_fields = ("user__first_name",)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("title", "body")
    ordering_fields = ("title", "created_at")
    ordering =('-created_at',)

    def get_serializer_class(self):
        return PostListSerializer if self.action == "list" else PostSerializer

    def get_queryset(self):
        user = self.request.user
        pk = self.blog.pk
        blog = Blog.objects.get(pk=pk)

        if (user.is_authenticated() and (blog.user == user)) or user.is_superuser:
            return Post.objects.select_related().filter(blog__id=pk)
        else:
            return Post.objects.select.relatec().filter(blog__id=pk, public=True)
