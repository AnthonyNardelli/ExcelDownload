from django.core.paginator import Paginator
from django.http import JsonResponse
from excel_streaming.models import DummyData

def get_dummy_data(request):
    page_number = request.GET.get('page', 1)  # Obtén el número de página de la solicitud
    page_size = request.GET.get('page_size', 100)  # Tamaño de la página
    
    # Obtén los datos de DummyData con paginación
    paginator = Paginator(DummyData.objects.all().order_by('pk'), page_size)
    page = paginator.get_page(page_number)
    
    # Serializa los datos de la página actual a formato JSON
    data = [{'data': obj.data} for obj in page]
    
    return JsonResponse(data, safe=False)
