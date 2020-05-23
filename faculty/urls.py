from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('notice/', views.notice, name = 'notice'),
    path('notice/new', views.notice_new, name = 'notice_new'),
    path('assignment', views.assignment, name = 'assignment'),
    path('assignment/new', views.assignment_new, name = 'assignment_new'),
]