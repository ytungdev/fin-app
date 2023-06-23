from django.http import JsonResponse
import utils


def test(request):
    result = []
    return JsonResponse({'result':result})