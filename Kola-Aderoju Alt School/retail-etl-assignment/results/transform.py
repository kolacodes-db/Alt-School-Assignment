import pandas as pd

# Step 1: Create the list of dictionaries
csv_data = [
    {
        "customer_id": 8,
        "customer_name": "Chinedu Okafor",
        "total_amount_spent": 2201700.0
    },
    {
        "customer_id": 2,
        "customer_name": "John Obi",
        "total_amount_spent": 1335000.0
    },
    {
        "customer_id": 1,
        "customer_name": "Fatima Usman",
        "total_amount_spent": 1127500.0
    },
    {
        "customer_id": 6,
        "customer_name": "Tunde Bakare",
        "total_amount_spent": 830300.0
    },
    {
        "customer_id": 5,
        "customer_name": "Amina Bello",
        "total_amount_spent": 588400.0
    }
]

# Step 2: Convert to DataFrame
df = pd.DataFrame(csv_data)

# Step 3: Format the amount as ₦ currency
df['total_amount_spent'] = df['total_amount_spent'].apply(lambda x: f"₦{x:,.2f}")

# Step 4: Save to CSV
output_path = "C:\Kola-Aderoju Alt School\retail-etl-assignment\results"
df.to_csv(output_path, index=False)

return ("'Done! CSV file saved to '{output_path}'")
print(df)
