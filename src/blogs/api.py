from django.db.models.functions import Lower
from django.http import Http404
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
    filter_fields = ('blog_id', )
    search_fields = ("title", "body")
    ordering_fields = ("title", "created_at")
    ordering =('-created_at',)

    def get_serializer_class(self):
        return PostListSerializer if self.action == "list" else PostSerializer

    def get_queryset(self):
        queryset = super(PostViewSet, self).get_queryset()

        print(self.kwargs)
        if 'blog_id' in self.kwargs:
            try:
                blog = Blog.objects.get(pk=self.kwargs['blog_id'])
            except:
                raise Http404()

            queryset = queryset.filter(blog=blog)

            if not (blog.user == self.request.user or self.request.user.is_superuser):
                queryset = queryset.filter(public=True)

        queryset.order_by(Lower('created_at').desc())

        return queryset

