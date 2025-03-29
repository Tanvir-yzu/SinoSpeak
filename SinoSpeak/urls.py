
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('i18n/', include('django.conf.urls.i18n')),  # Language switcher
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "SinoSpeak Admin"
admin.site.site_title = "SinoSpeak Portal"
admin.site.index_title = "Welcome to SinoSpeak Portal"