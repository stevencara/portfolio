from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import sys
from portfolio import views

print("DEBUG:", settings.DEBUG, "DEFAULT_FILE_STORAGE:", getattr(settings, 'DEFAULT_FILE_STORAGE', 'Not Set'), file=sys.stderr)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("blog/", include("blog.urls"))
]

# Solo en modo local (DEBUG=True) servir media desde el sistema de archivos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
