"""
Module containing the CalendarAction.
This shows the events in the users Google Calendar
"""


import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.action import Action
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


class CalendarAction(Action):
    """
    Shows the agenda for today from GCal
    """
    def __init__(self):
        super().__init__('Calendar')

        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())


    def get_events_from_calendar_id(self, service, calendar_id):
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        tomorrow = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat() + 'Z'
        events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                                timeMax=tomorrow,
                                                  maxResults=100, singleEvents=True,
                                                  orderBy='startTime').execute()
        events = events_result.get('items', [])
        return [(event['start'].get('dateTime', event['start'].get('date')), event['summary']) for event in events]
    
    def convert_event_data_to_string(self, event_data):
        human_readble_time = datetime.datetime.fromisoformat(event_data[0]).time()
        return f'{event_data[1]} at {human_readble_time}'
    
    def call(self) -> str:
        """
        Makes an API call to Google Calendar and returns the list of meetings for today
        :return: str, containing the meetings
        """
        try:
            service = build('calendar', 'v3', credentials=self.creds)

            calendars = service.calendarList().list().execute()['items']
            calendar_ids = [calendar['id'] for calendar in calendars]

            all_events = sum([self.get_events_from_calendar_id(service, calendar_id) for calendar_id in calendar_ids], [])
            all_events = sorted(all_events, key=lambda x: x[0])

            if len(all_events) == 0:
                return 'No upcoming events found.'
            
            all_events = ['Events today:'] + [self.convert_event_data_to_string(event) for event in all_events]
            
            return '\n'.join(all_events)

        except HttpError as error:
            print(f'An error occurred: {error}')
            return 'An error occurred'

