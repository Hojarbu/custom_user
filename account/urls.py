from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
 path('create', views.CreateCustomUserView.as_view(), name='create'),
 path('update/<int:pk>', views.UpdateCustomUserView.as_view(), name='update')
]