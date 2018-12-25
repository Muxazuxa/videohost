from .forms import *
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        videos = Home.objects.all().order_by('-uploaded')
        users = User.objects.exclude(id=request.user.id)
        args = {
            'form': form, 'videos': videos, 'users': users
                }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            video = form.save(commit = False)
            video.user = request.user
            video.save()
            name = form.save(commit=False)
            name.user = request.user
            name.save()
            form.save()
            form = HomeForm()
        args = {'form': form}
        return render(request, self.template_name, args)