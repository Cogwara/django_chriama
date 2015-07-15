from django.conf.urls import include, url
from django.contrib import admin
from django.templatetags.static import static
from django_chriama import settings

urlpatterns = [
    url(r'^$', 'django_chriama.views.home', name='home'),
    url(r'^product/', include('chriama.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
