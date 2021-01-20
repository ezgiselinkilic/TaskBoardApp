from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.login_view,name="login"),
    path('projects/', views.projects, name="projects"),
    path('create/',views.create,name="create"),
    path('deleteTodos/<Todos_id>',views.deleteTodos,name="deleteTodos"),
    path('yes_finish/<Todos_id>',views.yes_finish,name="yes_finish"),
    path('no_finish/<Todos_id>',views.no_finish,name="no_finish"),
    path('update/<Todos_id>',views.update,name="update"),
    path('detailProject/todo/update/',views.todoUpdate,name="todoUpdate"),
    path('createproject/',views.createproject,name="createproject"),
    path('deleteProject/<Project_id>',views.deleteProject,name="deleteProject"),
    path('detailProject/<Project_id>',views.detailProject,name="detailProject"),
    path('calculate/<Todos_id>',views.calculate,name="calculate"),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout')
  
]
