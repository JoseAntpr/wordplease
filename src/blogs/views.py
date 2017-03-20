from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blogs.models import Post, Blog
from django.utils.decorators import method_decorator
from django.views import View

from blogs.forms import PostForm


def lastest_posts(request):
    """
    Recupera los últimos posts de la base de datos y los pinta.
    :param request:
    :return: HttResponse
    """

    posts = Post.objects.all().order_by("-created_at")

    context = {
        'posts_objects': posts
    }

    return render(request, "blogs/index.html", context)

def blogs_list(request):
    """
    Recupera los blogs que hay en la plataforma
    :param request:
    :return: HttResponse
    """

    blogs = Blog.objects.all()

    context = {
        'blogs_objects': blogs
    }

    return render(request, "blogs/blogs_list.html", context)

def blog_detail(request, slug):
    """
    Recupera los blogs que hay en la plataforma
    :param request:
    :return: HttResponse
    """

    # Recuperar blog

    try:
        blog = Blog.objects.select_related().get(slug=slug)
    except Blog.DoesNotExist:
        return HttpResponse("No se encuentra el blog", status=404)
    except Blog.MultipleObjectReturned:
        return HttpResponse("Existen varios post con ese nombre", status=300)

    posts = Post.objects.filter(blog=blog)


    context = {
        'posts': posts
    }

    return render(request, "blogs/blog_detail.html", context)

def post_detail(request, slug, post_pk):
    """
    Recupera los blogs que hay en la plataforma
    :param request:
    :return: HttResponse
    """

    try:
        post = Post.objects.select_related().get(pk=post_pk)
    except Blog.DoesNotExist:
        return HttpResponse("No se encuentra el post", status=404)
    except Blog.MultipleObjectReturned:
        return HttpResponse("Existen varios post con el mismo id", status=300)



    context = {
        'post': post
    }

    return render(request, "blogs/post_detail.html", context)

class NewPostView(View):
    @method_decorator(login_required)
    def get(self,request):
        form = PostForm(request.user)

        context = {
            "form": form
        }
        return render(request,'blogs/new_post.html', context)

    @method_decorator(login_required)
    def post(self,request):

        form = PostForm(request.user,request.POST)

        if form.is_valid():
            post = form.save()

            message = "Post creado con éxito!"

            form = PostForm(request.user)
        else:
            message = "Se ha producido un error"

        context = {
            "form": form,
            "message": message
        }

        return render(request, 'blogs/new_post.html', context)


