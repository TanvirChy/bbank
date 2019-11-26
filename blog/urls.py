from django.urls import path
from django.conf.urls import url
from django_filters.views import FilterView
from .filters import UserFilter
from .views import (
    search,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    emar
)
from . import views 

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('announcements/', views.announ, name='announce-ments'),
    path('emergency/', emar , name='emer-gency'),
    url(r'^search/$', FilterView.as_view(filterset_class=UserFilter,
        template_name='blog/user_list.html'), name='search'),
]