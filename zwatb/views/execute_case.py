from django.http import HttpResponse
from django.views.generic import View

class executeCase(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")


