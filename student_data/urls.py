from django.contrib import admin
from django.urls import path
from . import views
from . import models



urlpatterns = [
    path("login/", views.login_page , name = "login" ),
    path("logout/", views.logout_page , name = "logout" ),
    path("register/", views.register_page , name = "register" ),
    
    path("",views.index,name="home"),
    
    path("studentdata",views.get_student ,name = 'student data'),
    path("studentmarks/<student_id>", views.student_marks, name = 'student marks'),
    
]
