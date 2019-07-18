"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path,include
from app1.views import create_detail_view,list_Employee_views,Reg_view,class_based_view,update_emp_view,EmpDetailView,EmpListview,EmpCreateView,\
EmpUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_detail_view),
    path('emp_details/',list_Employee_views),
    path('reg/', Reg_view),
    re_path("empBCBV/(?P<pk>[0-9]+)", update_emp_view),
    path(r'empBCBV/',class_based_view.as_view()),
    re_path('EmpDetailView/(?P<pk>[0-9]+)',EmpDetailView.as_view()),
    re_path('EmpListView/',EmpListview.as_view()),
    re_path(r'^EmpCreateView/',EmpCreateView.as_view()),
    re_path(r'^EmpUpdateView/(?P<pk>[0-9]+)',EmpUpdateView.as_view()),

 ### Django_restframework API ###########
    path('rest/', include('snippets.urls')),

    ]

