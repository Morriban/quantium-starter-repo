import csv

import csv

# Input and output filenames
input_file = 'daily_sales_data_0.csv'
input_file_2 = 'daily_sales_data_1.csv'
input_file_3 = 'daily_sales_data_2.csv'
output_file = 'output.csv'


# Helper function to convert price string to float
def parse_price(price_str):
    return float(price_str.replace('$', ''))

output_rows = []
# Read data from the input file and process it
with open(input_file, mode='r', newline='') as infile:
    reader = csv.DictReader(infile)
    #output_rows = []

    for row in reader:
        if row['product'].strip().lower() == 'pink morsel':
            price = parse_price(row['price'])
            quantity = int(row['quantity'])
            sales = price * quantity
            output_rows.append({
                'sales': f"${sales:.2f}",
                'date': row['date'],
                'region': row['region']
            })

with open(input_file_2, mode='r', newline='') as infile:
    reader = csv.DictReader(infile)
    #output_rows = []

    for row in reader:
        if row['product'].strip().lower() == 'pink morsel':
            price = parse_price(row['price'])
            quantity = int(row['quantity'])
            sales = price * quantity
            output_rows.append({
                'sales': f"${sales:.2f}",
                'date': row['date'],
                'region': row['region']
            })

with open(input_file_3, mode='r', newline='') as infile:
    reader = csv.DictReader(infile)
    #output_rows = []

    for row in reader:
        if row['product'].strip().lower() == 'pink morsel':
            price = parse_price(row['price'])
            quantity = int(row['quantity'])
            sales = price * quantity
            output_rows.append({
                'sales': f"${sales:.2f}",
                'date': row['date'],
                'region': row['region']
            })

# Write the processed data to the output file
with open(output_file, mode='w', newline='') as outfile:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(output_rows)

print(f"Processed data written to {output_file}")