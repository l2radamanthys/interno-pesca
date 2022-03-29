from django.contrib import admin
from django.urls import path
import backend.settings as settings
from django.views.generic.base import TemplateView, RedirectView
from django.conf.urls.static import static
from django.urls import re_path as url
from django.conf.urls import include
from interno.views.statics_pages import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("torneo/<pk>", detalle_torneo, name="detalle-torneo"),
    path("", home_page, name="home"),
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
