from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import visualisations.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^visualisations/', include('visualisations.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG: # Explicit registration of django toolbar URLs
    pass
    #import debug_toolbar
    #urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]