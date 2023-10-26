"""
URL configuration for student_report_card project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from student_data import views
from student_data import models

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("home",views.index,name="home"),
    
    path("studentdata",views.get_student ,name = 'student data'),
    path("studentmarks/<student_id>", views.student_marks, name = 'student marks'),
    # path("login/", include('student_data.urls') , name = "login" ),
    # path("logout/", include('student_data.urls') , name = "logout" ),
    # path("register/", include('student_data.urls') , name = "register" ),
    # path("",include('student_data.urls'),name="home"),
    # path("home",include('student_data.urls'),name="home"),
    # path("studentdata", include('student_data.urls'), name = 'student data'),

    path("login/", views.login_page , name = "login" ),
    path("logout/", views.logout_page , name = "logout" ),
    path("register/", views.register_page , name = "register" ),
    
    
    
    
]
