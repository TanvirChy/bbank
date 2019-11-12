import django_filters
from .models import Post

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['blood','phone','rigion']