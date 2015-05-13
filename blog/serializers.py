from hvad.contrib.restframework import TranslatableModelSerializer
from rest_framework.fields import ReadOnlyField
from blog.models import Category, Post


class CategorySerializer(TranslatableModelSerializer):
    class Meta:
        model = Category


class PostSerializer(TranslatableModelSerializer):
    box_bg = ReadOnlyField(source='get_box_bg_cropped')
    featured_picture = ReadOnlyField(source='get_featured_picture_cropped')
    category = CategorySerializer()

    class Meta:
        model = Post