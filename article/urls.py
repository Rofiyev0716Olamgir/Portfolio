from django.urls import path
from .views import (
                    article_detail_view,
                    home_view,
                    archive_view,


)

app_name = 'article'

urlpatterns = [
    path('', home_view, name='home'),
    path('detail/<slug:slug>/', article_detail_view, name='detail'),
    path('archive/', archive_view, name='archive'),

]