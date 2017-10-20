"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout
from mysite.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   url(r'^$', main),
   url(r'^editetask/(\d+)', taskedite),
   url(r'^task_list/(.*)/(.*)/(.*)/(.*)/(.*)/(.*)/(.*)', tasklist),
   url(r'^admin/', admin.site.urls),
   url(r'^editetask/(\d+)/', taskedite),
   url(r'^editetask/', taskedite),
   url(r'^imgview/(\d+)', imgview),


 #   url(r'^order/(\d+)/(\d+)/',order),
    url(r'^login/$', login2),
    url(r'^accounts/login/$', login2),
    url(r'^logout/$', logout,{'next_page': '/'}),]+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
