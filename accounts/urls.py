from django.urls import path
from .views import RegisterView, RetrieveUserView, LogoutView
from . import views

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view()),
    path('login', views.LoginView,name="login"),
    path('logout', LogoutView.as_view()),
    path('verify_token',views.verify_token,name='verify_token'),
    path('profile_view/<int:id>',views.profile_view,name='profile_view'),
    path('addImage/<int:id>',views.addImage,name='addImage'),
    
    
    
    #adminside
    path('admin_login',views.admin_login,name='admin_login'),
    path('user_list',views.user_list,name='user_list'),
    path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    path('update_user/<int:id>',views.update_user,name='update_user'),
    # path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),

]
