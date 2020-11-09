from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@cache_page(60 * 15)
def index(request):
    print("call index")
    return JsonResponse({'result': 200})
