from django.urls import path
from . import views


urlpatterns = [
    # path("", views.index, name = "index" ), # aici definim lista de endpoint-uri ale aplicatiei
    path("", views.HomeCadou.as_view(), name = 'home'),
    path("cadouri/<int:pk>/", views.DetaliiCadou.as_view(), name = "detalii_cadou" ), # cadou by Id
    path("cadouri/", views.ListaCadou.as_view(), name = "lista_cadou" ), # toate cadourile
    path("cadouri/<str:input_type>/", views.ListaCategorieCadou.as_view(), name = "lista_categorie_cadou"),
    path("cos/adauga/<int:cadou_id>/", views.AdaugaInCos.as_view(), name = "adauga_in_cos"),
    path("cos/sterge/<int:pk>/", views.StergeCos.as_view(), name = "sterge_cos"),
    path("cos/update/<int:pk>/", views.UpdateCos.as_view(), name = "update_cos"),
    path("cos/<int:pk>/", views.DetaliiCos.as_view(), name = "detalii_cos"),
    path('contact/', views.contact, name = "contact"),
    # path('home/', views.home, name = "home"),
    path('login/', views.login_user, name = "login"),
    path('logout/', views.logout_user, name = "logout"),


]