from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "pontos"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("createuser/", views.createuser, name="createuser"),
    path("addpontos/", views.addpontos, name="addpontos"),
    path("signout/", views.signout, name="signout"),
    path("hinario/", views.hinarioView, name="hinario"),
    path("hinario/<slug:slug_id>", views.pontosView, name="hino"),
    path("hinario/update-ponto/<int:ponto_id>", views.UpdateHino, name="update-hino")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)