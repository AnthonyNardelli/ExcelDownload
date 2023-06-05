from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from excel_streaming.views import get_dummy_data

urlpatterns = [

    path('get_dummy_data/', get_dummy_data, name='stream_excel'),
    # templateview para la página de inicio
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

# Configuración para servir los archivos estáticos en el entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)