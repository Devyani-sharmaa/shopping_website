from django.urls import path
from hi import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("home", views.myhome), 
    path("product-sidebar",views.productsidebar,name='y'),
    path("product-info",views.productinfo),
    path("about",views.about),
    path("cart",views.cart,name='z'),
    path("index",views.index,name="index"),
    path('user-profile',views.user_profile),
    path("become-vendor",views.become_vendor),
    path("checkout",views.checkout),
    path("compaire",views.compaire),
    path("contact-us",views.contact_us),
    #path("add_to_cart",views.add_to_cart),
    path("create-account",views.create_account),
    path("order",views.order),
    path("faq",views.faq),
    path("login", views.loginpage, name = "loginpage"),
    path("signup", views.signuppage, name = "signuppage"),
    path("lets-logout", views.logutnow, name = "logout"),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)