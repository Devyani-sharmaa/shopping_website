from django.urls import path
from ds import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("indexx", views.indexx),
    path("mailbox",views.mailbox),
    path("chart",views.chart),
    path("basic-chart",views.chart),
    path("data-table",views.data_table),
    path("layouts",views.layouts),
    path("login",views.login),
    path("forget-password",views.forget_password),
    path("add_product",views.add_product),
    path("delte-record/<int:x>",views.deletefata),
    path("order_detail",views.order_detail),

    ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)