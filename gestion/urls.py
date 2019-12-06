from django.urls import path
from . import views
from django.urls import include #para usar urls de las app 

urlpatterns = [
    path('', views.home, name="home"),
    path('encuentranos/', views.encuentranos, name="encuentranos"),
    path('juegos/', views.juegos, name="juegos"),
    #url('list/', views.ClienteList.as_view(), name='plist'),
    #url('add/', views.add_cliente, name='padd'),
    #path("", view.home),
    path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name='cliente_detail'),
    
]

urlpatterns += [
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),#es tipo cliente/nombre/update y si no funciona es cliente/"id"/update
    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
    
]

    