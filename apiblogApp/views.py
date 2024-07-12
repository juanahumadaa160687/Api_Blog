from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from apiblogApp.models import Post


class PostView(View):

    def get(self, request, id=0):
        if id > 0:
            posts = list(Post.objects.filter(id=id).values())
            if len(posts) > 0:
                post = posts[0]
                datos = {'message': 'Success', 'posts': post}
            else:
                datos = {'message': 'No data'}
            return JsonResponse(datos)

        else:
            posts = list(Post.objects.values())
            if len(posts) > 0:
                datos = {'message': 'Success', 'posts': posts}
            else:
                datos = {'message': 'No data'}
            return JsonResponse(datos)


