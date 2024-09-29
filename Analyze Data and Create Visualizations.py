# Merge Google Ads and Google Analytics Data
merged_df = pd.merge(df, df_ga, how='left', left_on='Campaign Name', right_on='Campaign')

# Calculate key performance metrics
merged_df['CTR'] = (merged_df['Clicks'] / merged_df['Impressions']) * 100
merged_df['CPA'] = merged_df['Cost (Micros)'] / merged_df['Conversions']
merged_df['Conversion Rate'] = (merged_df['Conversions'] / merged_df['Clicks']) * 100

# Example: Calculate ROI for each campaign
merged_df['ROI'] = (merged_df['Goal Completions'] / merged_df['Cost (Micros)']) * 1000

print(merged_df)

# Visualization with Plotly
import plotly.express as px

fig = px.bar(merged_df, x='Campaign Name', y='Conversions', title='Conversions by Campaign')
fig.show()
