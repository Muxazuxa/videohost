from .forms import *
from django.shortcuts import redirect, render


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('profile/login')
    else:
        form = RegistrationForm()
        args = {'form': form}
    return render(request, 'profile/register.html', args)


def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile/profile.html', args)


