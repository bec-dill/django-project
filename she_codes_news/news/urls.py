from django.urls import path
from . import views
from django.views.generic.dates import ArchiveIndexView

from news.models import Article
app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('archive/', ArchiveIndexView.as_view(model=Article, date_field="pub_date"), name="article_archive"),
]
