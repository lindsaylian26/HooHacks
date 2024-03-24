from django.shortcuts import render, redirect
from .forms import AdvisorForm
from .models import Advisor
from django.views.generic import ListView


def register_advisor(request):
    if request.method == 'POST':
        form = AdvisorForm(request.POST)
        if form.is_valid():
            advisor = form.save(commit=False)
            advisor.user = request.user
            advisor.save()
            return render(request, 'advisor/success_advisor.html')
    else:
        form = AdvisorForm()
    return render(request, 'advisors/register.html', {'form': form})

def advisor_profile(request, advisor_id):
    advisor = Advisor.objects.get(id=advisor_id)
    return render(request, 'advisors/profile.html', {'advisor': advisor})

class AdvisorList(ListView):
    model = Advisor
    template_name = 'advisors/advisor_list.html'