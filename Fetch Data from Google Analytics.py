from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Setup the Google Analytics Reporting API
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'YOUR_CREDENTIALS_FILE.json'
VIEW_ID = 'YOUR_VIEW_ID'

# Initialize credentials and service
credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Create request body to pull data
body = {
  'reportRequests': [{
    'viewId': VIEW_ID,
    'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
    'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:goalCompletionsAll'}],
    'dimensions': [{'name': 'ga:campaign'}]
  }]
}

# Fetch the report
response = analytics.reports().batchGet(body=body).execute()

# Parse and store the results
report = response['reports'][0]
rows = report['data']['rows']
data = []
for row in rows:
    campaign = row['dimensions'][0]
    sessions = row['metrics'][0]['values'][0]
    goal_completions = row['metrics'][0]['values'][1]
    data.append([campaign, int(sessions), int(goal_completions)])

df_ga = pd.DataFrame(data, columns=['Campaign', 'Sessions', 'Goal Completions'])
print(df_ga)
