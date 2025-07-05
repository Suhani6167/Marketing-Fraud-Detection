import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

# Load sales data to get valid order_ids
df_sales = pd.read_csv('data/sales_data.csv')

# Select 20 random orders to refund
refunded_orders = df_sales.sample(n=20, random_state=42)

# Create refund data
refunds = []
reasons = ['Defective', 'Customer Error', 'Fraud Suspicion']

for i, row in refunded_orders.iterrows():
    # Convert order_date from string to datetime object
    order_date_obj = datetime.strptime(row['order_date'], '%Y-%m-%d').date()

    refund = {
        'refund_id': 2000 + i,
        'order_id': row['order_id'],
        'refund_amount': round(random.uniform(50, row['sales_amount']), 2),
        'refund_date': fake.date_between(start_date=order_date_obj, end_date=datetime.today().date()),
        'reason': random.choice(reasons)
    }
    refunds.append(refund)

# Save to CSV
df_refunds = pd.DataFrame(refunds)
df_refunds.to_csv('data/refunds.csv', index=False)

print("✅ refunds.csv generated successfully!")
print(df_refunds.head())