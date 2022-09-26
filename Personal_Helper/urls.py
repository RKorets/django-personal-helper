from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = [
                path(_('admin/'), admin.site.urls),
                path('captcha/', include('captcha.urls')),
                ] + i18n_patterns\
        (
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('accounts.urls')),
    path('', include('files.urls')),
    path('', include('contacts.urls')),
    path('', include('news.urls')),
    path('', include('notes.urls')),
    prefix_default_language=False
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = "contacts.views.page_not_found_view"
