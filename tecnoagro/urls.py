from django.urls import path
from . import views
from .views import consulta_usuario
from .views import UserRegisterView

urlpatterns= [
	path('', views.home, name='home'),
	path('contacto/', views.consultar, name='consultar'),
	path('somos/', views.somos, name='somos'),
	path('aplicaciones/', views.aplicaciones, name='aplicaciones'),
	#path('registro/', views.registro, name='registro'),
	path('descargas/', views.descargas, name='descargas'),
	path('consulta/', consulta_usuario, name='consulta'),
	path('registro/', UserRegisterView.as_view(), name='registro'),
	path('login/', UserRegisterView.as_view(), name='login')
]