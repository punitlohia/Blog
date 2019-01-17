from django.urls import path
from . import views

urlpatterns = [
    path('',views.initialpage,name='initialpage'),
    path('blog',views.index,name='index'),
    path('profile/register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('profile/edit',views.EditProfile,name="EditProfile"),
    path('password/',views.ChangePassword,name="ChangePassword"),
    path('logout',views.LogoutProfile,name="LogoutProfile"),
    path('<id>/add_comment',views.add_comment,name="add_comment"),
    path('<id>/add_comment_profile',views.add_comment_profile,name="add_comment_profile"),
    path('<id2>/<id>/add_comment_userprofile',views.add_comment_userprofile,name="add_comment_userprofile"),
    path('allusers',views.allusers,name="allusers"),
    path('<id>/user_profile',views.user_profile,name="user_profile"),
    path('<id>/follow_user',views.follow_user,name="follow_user"),
    path('<id>/unfollow_user',views.unfollow_user,name="unfollow_user")
]
