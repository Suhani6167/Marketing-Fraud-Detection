from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)

# Define products and campaign codes
products = ['Phone', 'Laptop', 'Tablet', 'Headphones', 'Monitor']
campaigns = ['CMP001', 'CMP002', 'CMP003', 'None']

# Generate 200 fake sales records
sales_data = []

for i in range(200):
    order = {
        'order_id': 1000 + i,
        'customer_id': random.randint(1, 50),
        'customer_name': fake.name(),
        'product_name': random.choice(products),
        'sales_amount': round(random.uniform(100, 3000), 2),
        'campaign_code': random.choice(campaigns),
        'order_date': fake.date_between(start_date='-6M', end_date='today')
    }
    sales_data.append(order)

# Create DataFrame and save to CSV
df_sales = pd.DataFrame(sales_data)
df_sales.to_csv('data/sales_data.csv', index=False)

print("✅ sales_data.csv generated successfully!")
print(df_sales.head())
