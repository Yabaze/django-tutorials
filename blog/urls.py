from django.urls import path

from .views import (
    post_model_list_view ,
    post_model_detail_view,
    post_model_create_view,
    post_model_update_view,
)
urlpatterns = [#/posts 
    path('', post_model_list_view, name='list'), # home function name
    path("create/",post_model_create_view , name = 'create'),
    path('1/',post_model_detail_view , name = 'detail'),
    path("1/edit/",post_model_update_view , name = 'update'),

] 