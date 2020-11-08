from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Application Views
    path('',               include('home.urls')),
    path('championships/',  include('championships.urls')),
    path('accounts/',       include('accounts.urls')),
    path('drivers/',        include('drivers.urls')),
    path('events/',         include('events.urls')),
    path('cars/',           include('cars.urls')),
    path('galleries/',      include('gallery.urls')),
    
    # Django Views
    path('admin/',          admin.site.urls),
    path('accounts/',       include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
## django.contrib.auth.urls ##

urlpatterns = [
    accounts/login/                     [name='login']
    accounts/logout/                    [name='logout']
    accounts/password_change/           [name='password_change']
    accounts/password_change/done/      [name='password_change_done']
    accounts/password_reset/            [name='password_reset']
    accounts/password_reset/done/       [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/    [name='password_reset_confirm']
    accounts/reset/done/                [name='password_reset_complete']
]
"""