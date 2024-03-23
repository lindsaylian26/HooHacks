from django.shortcuts import render, redirect
from .forms import AdviseeForm
from .models import Advisee

def register_advisee(request):
    if request.method == 'POST':
        form = AdviseeForm(request.POST)
        if form.is_valid():
            advisee = form.save(commit=False)
            advisee.user = request.user
            advisee.save()
            return redirect('advisee_profile', advisee_id=advisee.id)
    else:
        form = AdviseeForm()
    return render(request, 'advisees/register.html', {'form': form})

def advisee_profile(request, advisee_id):
    advisee = Advisee.objects.get(id=advisee_id)
    return render(request, 'advisees/profile.html', {'advisee': advisee})
