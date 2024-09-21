from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
from shop import settings
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('faq', views.faq, name='faq'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('category/<slug:category_slug>/', views.category, name='category'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)