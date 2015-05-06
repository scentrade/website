from rest_framework import viewsets
from blog.models import Category, Post
from blog.serializers import CategorySerializer, PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related().all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related().all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    filter_fields = ('category', 'category__slug')