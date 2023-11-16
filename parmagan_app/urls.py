from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from  . import views
app_name = 'parmagan_app'

urlpatterns = [
    path('', views.index, name='index'),


    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)