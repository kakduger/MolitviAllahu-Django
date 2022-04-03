from mimetypes import init
from django.contrib import admin
from django.urls import path
from welcomeup.views import aboutPage, initPage, players
from nbaplayers.views import allplayersPage, CurrPlayer

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initPage),
    path('about/', aboutPage, name = "about_Nikolai"),
    path('players/', allplayersPage, name = "AllPlayers"),
    path('current player/', CurrPlayer, name = "Current Player" )
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


