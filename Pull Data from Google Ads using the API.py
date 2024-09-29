from google.ads.google_ads.client import GoogleAdsClient

# Initialize Google Ads API client
client = GoogleAdsClient.load_from_storage(path="google_ads.yaml")

# Define the query to fetch data
query = '''
SELECT
  campaign.id,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros
FROM
  campaign
WHERE
  segments.date DURING LAST_30_DAYS
'''

# Fetch the data
ga_service = client.get_service("GoogleAdsService")
response = ga_service.search_stream(customer_id="YOUR_CUSTOMER_ID", query=query)

# Parse and store the results in a DataFrame
import pandas as pd

data = []
for batch in response:
    for row in batch.results:
        data.append({
            "Campaign ID": row.campaign.id,
            "Campaign Name": row.campaign.name,
            "Impressions": row.metrics.impressions,
            "Clicks": row.metrics.clicks,
            "Conversions": row.metrics.conversions,
            "Cost (Micros)": row.metrics.cost_micros / 1e6  # Convert micros to standard currency
        })

df = pd.DataFrame(data)
print(df)
