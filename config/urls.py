from django.contrib import admin
from django.urls import path , include ,re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('shop.urls')),
    path('account/',include('accounts.urls')),
    path('cart/',include('cart.urls')),
    path('orders/',include('orders.urls')),
    path('dashboard/',include('dashboard.urls')),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)