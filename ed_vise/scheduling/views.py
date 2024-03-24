"""
from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'calendar_app/event_list.html', {'events': events})
"""
from django.shortcuts import redirect, render
from google_auth_oauthlib.flow import Flow
from django.conf import settings
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime
from django.urls import reverse 

def google_login(request):
    flow = Flow.from_client_secrets_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        redirect_uri='http://localhost:8000/oauth2callback'
    )

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    request.session['state'] = state
    return redirect(authorization_url)

def oauth2callback(request):
    # Check if 'state' is in the session
    if 'state' not in request.session:
        # Handle the missing state (e.g., redirect to login or show an error)
        return redirect('google_login')  # Redirect to the index page of 'ed_vise' app

    state = request.session['state']

    flow = Flow.from_client_secrets_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        state=state,
        redirect_uri='http://localhost:8000/oauth2callback'
    )

    # Validate state parameter
    if state != request.GET.get('state'):
        # Handle mismatching state (e.g., redirect to login or show an error)
          return render(request, 'ed_vise/index.html')  # Redirect to a valid URL

    flow.fetch_token(authorization_response=request.get_full_path())

    credentials = flow.credentials
    request.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

    return render(request, 'ed_vise/index.html')


def list_events(request):
    creds_data = request.session.get('credentials')

    if not creds_data:
        return redirect('google_login')

    creds = Credentials(**creds_data)

    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            return redirect('google_login')

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    # Your logic to handle events goes here

    return render(request, 'scheduling:google_login')


