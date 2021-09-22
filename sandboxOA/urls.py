"""sandboxOA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.static import serve
from sandboxOA.settings import MEDIA_ROOT
from django.urls import path
from django.contrib import admin
from system.views_user import IndexView, LoginView, LogoutView
from dailyreport import views
from django.urls import reverse
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TemplateView.as_view(template_name='index.html')),
    path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('myreport/', views.MyReportView.as_view(), name='myreport'),
    path('myreport/create', views.ReportCreateView.as_view(), name='myreport-create'),
    path('myreport/detail', views.ReportDetailView.as_view(), name='myreport-detail'),

]
