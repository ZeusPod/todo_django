from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [ 

    path('', views.HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('task/create/', views.TaskCreateView.as_view(), name='create_task'),
    path('task/delete/<int:pk>',views.DeleteTaskView.as_view(), name='delete_task' ),
    path('task/update/<int:pk>', views.UpdateTaskView.as_view(), name='update_task'),

]