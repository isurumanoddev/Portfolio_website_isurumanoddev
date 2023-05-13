from django.urls import path
from portfolio import views


urlpatterns = [
    path('', views.home ,name="home"),
    path('projects/', views.projects ,name="projects"),
    path('project_page/<str:pk>/', views.project_page, name="project-page"),

]
