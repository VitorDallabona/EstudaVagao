'''ARQUIVO PARA DEFINIR AS ROTAS DA APLICAÇÃO '''

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django_app.views import *

# ORGANIZANDO ROTAS
urlpatterns = [
    path('', LoginView.as_view(), name='login'), # pagina inicial / login
    path('register/', cadastro, name='register'), #pagina de registro
    #path('home/', name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #define que possui elementos estaticos no view
