
from django.shortcuts import redirect, render
from google_auth_oauthlib.flow import Flow
from django.conf import settings
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime
from advisees.forms import AdviseeForm

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

    # Retrieve user profile information
    service = build('oauth2', 'v2', credentials=credentials)
    profile = service.userinfo().get().execute()
    username = profile.get('name', 'Unknown')

    # Pass the username to the form initialization
    form = AdviseeForm(initial={'name': username})

    return render(request, 'ed_vise/index.html', {'form': form})


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

     # Get user's email from Gmail API
    user_email = service.users().getProfile(userId='me').execute()['emailAddress']

    # Pass email as initial data to the AdviseeForm
    form = AdviseeForm(initial={'name': user_email})

    return render(request, 'your_template.html', {'form': form})


def gmail_data(request):
    # Check if credentials are available in the session
    if 'credentials' not in request.session:
        return redirect('google_login')  # Redirect to login if credentials are not available

    # Get credentials from session
    credentials_data = request.session['credentials']
    credentials = Credentials(**credentials_data)

    # Build Gmail service
    service = build('gmail', 'v1', credentials=credentials)

    # Example: Fetching email labels
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    # Pass fetched labels data to the form
    form = AdviseeForm(label_choices=[(label['id'], label['name']) for label in labels])

    return render(request, 'gmail_data.html', {'form': form})

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }