from django.shortcuts import render, redirect
from .forms import ClientCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('main-home')
    else:
        form = ClientCreationForm()
    return render(request, 'users/register.html', {'form': form})
