
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hello/', views.hello),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('list/', views.table, name='singed'),
    path('clear_all/', views.clear_all, name='clear-all'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
