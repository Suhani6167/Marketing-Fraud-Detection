import pandas as pd

# Load data
sales = pd.read_csv("../data/sales_data.csv")
refunds = pd.read_csv("../data/refunds.csv")

# Step 1: Total sales per customer
sales_summary = sales.groupby(['customer_id', 'customer_name'])['sales_amount'].sum().reset_index()
sales_summary.rename(columns={'sales_amount': 'total_sales'}, inplace=True)

# Step 2: Total refunds per customer
refunds_merged = refunds.merge(sales[['order_id', 'customer_id']], on='order_id', how='left')
refunds_summary = refunds_merged.groupby('customer_id')['refund_amount'].sum().reset_index()
refunds_summary.rename(columns={'refund_amount': 'total_refunds'}, inplace=True)

# Step 3: Merge sales and refunds
cltv = sales_summary.merge(refunds_summary, on='customer_id', how='left')
cltv['total_refunds'] = cltv['total_refunds'].fillna(0)
cltv['cltv'] = cltv['total_sales'] - cltv['total_refunds']

# Step 4: Optional - categorize customers
def categorize(value):
    if value >= 2000:
        return 'High'
    elif value >= 1000:
        return 'Medium'
    else:
        return 'Low'

cltv['customer_segment'] = cltv['cltv'].apply(categorize)

# Save output
cltv.to_csv("../data/cltv_output.csv", index=False)
print("✅ CLTV calculated and saved to cltv_output.csv")
print(cltv.head())
