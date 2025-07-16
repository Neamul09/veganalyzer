import csv
from datetime import datetime

# Input and output filenames
input_file = 'daily_onion_prices.csv'
output_file = 'daily_onion_prices_sorted.csv'

with open(input_file, 'r', newline='') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Sort rows by date in the first column
rows.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
