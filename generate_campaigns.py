import pandas as pd

# Create a list of marketing campaigns
campaigns = [
    {
        'campaign_code': 'CMP001',
        'campaign_name': 'New Year Bonanza',
        'start_date': '2025-01-01',
        'end_date': '2025-01-15',
        'ad_spend': 10000
    },
    {
        'campaign_code': 'CMP002',
        'campaign_name': 'Summer Sale Splash',
        'start_date': '2025-03-15',
        'end_date': '2025-03-31',
        'ad_spend': 8000
    },
    {
        'campaign_code': 'CMP003',
        'campaign_name': 'Mega Festive Promo',
        'start_date': '2025-04-10',
        'end_date': '2025-04-25',
        'ad_spend': 12000
    }
]

# Create DataFrame and save to CSV
df_campaigns = pd.DataFrame(campaigns)
df_campaigns.to_csv('data/campaigns.csv', index=False)

print("✅ campaigns.csv generated successfully!")
print(df_campaigns)
