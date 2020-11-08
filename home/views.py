from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = "home/index.html"

    def get(self, request):
        return render(request, self.template_name)


class AboutView(View):
    template_name = "home/about.html"

    def get(self, request):
        return render(request, self.template_name)
