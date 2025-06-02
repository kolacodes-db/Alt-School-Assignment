import pandas as pd
import os

def clean_top_customers_csv(input_path, output_path):
    """
    Cleans the top_customers.csv file:
    - Converts customer names to title case
    - Formats total amount spent as ₦ currency

    Args:
        input_path (str): Path to input CSV
        output_path (str): Path to save cleaned CSV
    """
    # Load the CSV
    df = pd.read_csv(input_path)

    # Convert customer names to title case
    df['customer_name'] = df['customer_name'].str.title()

    # Format the total_amount_spent column as ₦ currency
    df['total_amount_spent'] = df['total_amount_spent'].apply(lambda x: f"₦{x:,.2f}")

    # Save to output path
    df.to_csv(output_path, index=False)
    print(f"✅ File cleaned and saved to '{output_path}'")

# Main execution
if __name__ == "__main__":
    input_file = os.path.join("results", "top_customers.csv")
    output_file = os.path.join("results", "top_customers_cleaned.csv")

    clean_top_customers_csv(input_file, output_file)
