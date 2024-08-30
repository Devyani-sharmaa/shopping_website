from django.urls import path
from ad import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("indexxx", views.indexxx),
    path("manageseller",views.seller),
    
    ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)