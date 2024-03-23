from django.shortcuts import render, redirect
from .forms import AdvisorForm
from .models import Advisor

def register_advisor(request):
    if request.method == 'POST':
        form = AdvisorForm(request.POST)
        if form.is_valid():
            advisor = form.save(commit=False)
            advisor.user = request.user
            advisor.save()
            return redirect('advisor_profile', advisor_id=advisor.id)
    else:
        form = AdvisorForm()
    return render(request, 'advisors/register.html', {'form': form})

def advisor_profile(request, advisor_id):
    advisor = Advisor.objects.get(id=advisor_id)
    return render(request, 'advisors/profile.html', {'advisor': advisor})
