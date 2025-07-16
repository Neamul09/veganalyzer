import os
import pandas as pd
import re
from rich.console import Console
from rich.table import Table

# Set up console for terminal output
console = Console()

# Folder where xlsx files are saved
folder_path = "downloaded_excels"
output_csv = "daily_onion_prices.csv"

# Create CSV if not exists
if not os.path.exists(output_csv):
    with open(output_csv, "w", encoding="utf-8") as f:
        f.write("Date,Min Price,Max Price,Avg Price,City\n")

# Function to show result in terminal table
def show_onion_info(date, min_price, max_price, avg_price, city):
    table = Table(title="Onion Price Extracted")

    table.add_column("Date", justify="center")
    table.add_column("Min Price", justify="center")
    table.add_column("Max Price", justify="center")
    table.add_column("Avg Price", justify="center")
    table.add_column("City", justify="center")

    table.add_row(date, min_price, max_price, avg_price, city)
    console.print(table)

# Loop through all xlsx files
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)

        try:
            df = pd.read_excel(file_path, header=None)

            # Search for row containing "পিঁয়াজ (দেশী)"
            onion_row = df[df.astype(str).apply(
                lambda row: row.str.contains(r"পিঁয়াজ \(দেশী\)", regex=True).any(), axis=1)]

            if not onion_row.empty:
                onion_data = onion_row.iloc[0]
                min_price = float(str(onion_data[2]).strip())
                max_price = float(str(onion_data[3]).strip())
                avg_price = round((min_price + max_price) / 2, 2)

                # Extract date from filename using regex
                match = re.search(r"(\d{4}-\d{2}-\d{2})", filename)
                date_str = match.group(1) if match else "Unknown"

                # Save to CSV
                with open(output_csv, "a", encoding="utf-8") as f:
                    f.write(f"{date_str},{min_price},{max_price},{avg_price},Dhaka\n")

                # Print visual table in terminal
                show_onion_info(date_str, str(min_price), str(max_price), str(avg_price), "Dhaka")

            else:
                console.print(f"[yellow]No onion data found in file: {filename}[/yellow]")

        except Exception as e:
            console.print(f"[red]Failed to process {filename}: {e}[/red]")


for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)

        try:
            df = pd.read_excel(file_path, header=None)

            # Search for row containing "পিঁয়াজ (দেশী)"
            onion_row = df[df.astype(str).apply(
                lambda row: row.str.contains(r"পিঁয়াজ \(নতুন\) \(দেশী\)", regex=True).any(), axis=1)]

            if not onion_row.empty:
                onion_data = onion_row.iloc[0]
                min_price = float(str(onion_data[2]).strip())
                max_price = float(str(onion_data[3]).strip())
                avg_price = round((min_price + max_price) / 2, 2)

                # Extract date from filename using regex
                match = re.search(r"(\d{4}-\d{2}-\d{2})", filename)
                date_str = match.group(1) if match else "Unknown"

                # Save to CSV
                with open(output_csv, "a", encoding="utf-8") as f:
                    f.write(f"{date_str},{min_price},{max_price},{avg_price},Dhaka\n")

                # Print visual table in terminal
                show_onion_info(date_str, str(min_price), str(max_price), str(avg_price), "Dhaka")

            else:
                console.print(f"[yellow]No onion data found in file: {filename}[/yellow]")

        except Exception as e:
            console.print(f"[red]Failed to process {filename}: {e}[/red]")


