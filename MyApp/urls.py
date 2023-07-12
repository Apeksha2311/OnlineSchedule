from django.urls import path

from .import views


urlpatterns = [
    path('' , views.home_view.as_view() , name="home"),
    path('register/' , views.register_view.as_view() , name='register'),
    path('signout/' , views.signout_view , name="signout"),
    
    

    
    path('instructor/', views.instructor, name='instructor'),
    
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('add-course/', views.add_course, name='add_course'),
    path('assign-lecture/', views.assign_lecture, name='assign_lecture'),
    path('add-instructor/', views.add_instructor, name='add_instructor'),
    ]