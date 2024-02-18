# shortener/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import URL
from .utils import generate_short_url

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        url, created = URL.objects.get_or_create(long_url=long_url)
        if created:
            url.short_url = generate_short_url(long_url)
            url.save()
        return JsonResponse({'short_url': url.short_url})
    return JsonResponse({'error': 'Invalid request method'})
