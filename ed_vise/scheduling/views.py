"""
from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'calendar_app/event_list.html', {'events': events})
"""


from google_auth_oauthlib.flow import Flow
from django.shortcuts import redirect

def google_login(request):
    flow = Flow.from_client_secrets_file(
        'client_secrets.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        redirect_uri='http://localhost:8000/oauth2callback'
    )

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    request.session['state'] = state
    return redirect(authorization_url)
