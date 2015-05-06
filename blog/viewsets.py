from rest_framework import viewsets
from blog.models import Category, Post
from blog.serializers import CategorySerializer, PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related().all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related().all()
    serializer_class = PostSerializer