from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('files/<int:id>', views.myfiles, name='myfiles'),
    path('logout/', views.logout_view, name='logout'),
]
