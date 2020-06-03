from django.urls import path

# from . import views
from Insta.views import PostListView

urlpatterns = [
    path('', PostListView.as_view()),
]