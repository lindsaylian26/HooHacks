from django.shortcuts import render, redirect
from .forms import AdviseeForm
from .models import Advisee
from django.http import HttpResponse


def register_advisee(request):
    if request.method == 'POST':
        form = AdviseeForm(request.POST)
        if form.is_valid():
            # Check if the user already has an advisee entry
            if Advisee.objects.filter(user=request.user).exists():
                # Handle the case where the user already has an advisee, e.g., show an error message
                return HttpResponse("You already have an advisee entry.", status=400)
            else:
                advisee = form.save(commit=False)
                advisee.user = request.user
                advisee.save()
                return render(request, 'advisee/advisee_success.html')
    else:
        form = AdviseeForm()
    return render(request, 'advisees/register.html', {'form': form})

def advisee_profile(request, advisee_id):
    advisee = Advisee.objects.get(id=advisee_id)
    return render(request, 'advisees/profile.html', {'advisee': advisee})