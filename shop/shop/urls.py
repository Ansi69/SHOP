from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static
from shop import settings
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('faq', views.faq, name='faq'),
    path('registration', views.registration, name='registration'),
    path('logout', views.logout, name='logout'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('cart/', include('carts.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)