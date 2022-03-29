from django.contrib import admin
from django.urls import path
import backend.settings as settings
from django.views.generic.base import TemplateView, RedirectView
from django.conf.urls.static import static
from django.conf.urls import url, include


urlpatterns = [
    path("admin/", admin.site.urls),
]


if settings.ENVIROMENT == "DESARROLLO":
    urlpatterns = urlpatterns + [
        url(
            r"^assets/(?P<path>.*)$",
            RedirectView.as_view(
                url=settings.STATIC_URL + "dist/assets/%(path)s", permanent=True
            ),
            name="cloud-static",
        ),
    ]
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
