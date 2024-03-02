from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('task/edit/<int:id>', views.edit_task, name='edit_task'),
    path('task/delete/<int:id>', views.delete_task, name='delete_task'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', views.logout_view, name='logout_view'),
    path('register/', views.sign_up, name='register'),
]