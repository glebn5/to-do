from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
		path('login/', UserLogin.as_view(), name='login'),
		path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
		path('register/', Register.as_view(), name='register'),

		path('', TaskList.as_view(), name='tasks'),
		#path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
		path('add/', TaskCreate.as_view(), name='add_task'),
		path('task/<int:pk>/', TaskUpdate.as_view(), name='task'),
		path('delete/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
		
]
