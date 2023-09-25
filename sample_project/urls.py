
"""sample_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from upload_data.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploaddata/',UploadFiles,name='UploadFiles'),
    # path('showallfiles/',Show_All_Files,name="Show_All_Files"),
    path('deletefile/<id>/',delete_files,name='delete_files'),
    path('login/',LogIn_page,name="LogIn_page"),
    path('logout/',logout_page,"logout_page"),
    path('registration/',Registration,name="Registration"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()