from django.urls import path
from . import views

urlpatterns =[

path('', views.posts_list, name='posts_list'),
path('<int:pk>/', views.posts_detail, name='posts_detail'),
path('create/', views.posts_create, name='posts_create'),
path('<int:pk>/upd/', views.posts_update, name='posts_update'),
path('<int:pk>/del/', views.posts_delete, name='posts_delete'),
path('<int:pk>/summary/', views.posts_summary, name='posts_summary')
]