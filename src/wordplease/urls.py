"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from blogs.views import lastest_posts, blogs_list, blog_detail, post_detail, NewPostView
from users.views import LoginView, SignUpView

from users.api import UserViewSet
from blogs.api import BlogViewSet, PostViewSet

router = DefaultRouter()
router.register("users", UserViewSet, base_name="users_api")
router.register("blogs", BlogViewSet, base_name="blogs_api")
router.register("posts", PostViewSet, base_name="posts_api")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', lastest_posts, name="index"),
    url(r'^blogs/?$', blogs_list, name="blog_list"),
    url(r'^blogs/(?P<slug>[\w.@+-]+)/?$', blog_detail, name="blog_detail"),
    url(r'^blogs/(?P<slug>[\w.@+-]+)/(?P<post_pk>[0-9]+)/?$', post_detail, name="post_detail"),
    url(r'^new_post', NewPostView.as_view(), name="new_post"),
    url(r'^login',LoginView.as_view(), name="login"),
    url(r'^signup',SignUpView.as_view(), name="signup"),

    #api
    url(r'^api/1.0/', include(router.urls)),
]
