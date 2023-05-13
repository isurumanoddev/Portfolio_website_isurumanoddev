from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('project_page/<str:pk>/', views.project_page, name="project-page"),

    path('create_project/', views.create_project, name="create-project"),
    path('edit_project/<str:pk>/', views.edit_project, name="edit-project"),
    path('delete_project/<str:pk>/', views.delete_project, name="delete-project"),

    path('inbox/', views.inbox, name="inbox"),
    path('contact_form/', views.contact_form, name="contact-form"),

]
