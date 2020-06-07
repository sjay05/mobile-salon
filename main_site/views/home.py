from django.shortcuts import render, redirect
from django.views import View

class IndexView(View):
    template_name = 'home_page.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['user'] = request.user

        return render(request, self.template_name, self.context)