import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Configuration
output_dir = "downloaded_excels"
os.makedirs(output_dir, exist_ok=True)

api_url = "https://tcb.gov.bd/api/datatable/daily_rmp_view.php"
params = {
    "domain_id": "6383",
    "lang": "bn",
    "subdomain": "tcb.portal.gov.bd",
    "content_type": "daily_rmp"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

# API pagination config
page_size = 20
total_records = 993  # Based on your JSON
pages = range(0, total_records, page_size)

# Download function
def download_file(file_url, output_path):
    r = requests.get(file_url)
    if r.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(r.content)
        print(f"✅ Downloaded: {os.path.basename(output_path)}")
    else:
        print(f"❌ Failed to download: {file_url}")

# Loop through pages
for start in tqdm(pages, desc="Fetching Pages"):
    payload = {
        "sEcho": 2,
        "iColumns": 5,
        "sColumns": ",,,",
        "iDisplayStart": start,
        "iDisplayLength": page_size,
    }

    # Add column metadata for the request (important!)
    for i in range(5):
        payload[f"mDataProp_{i}"] = i
        payload[f"sSearch_{i}"] = ""
        payload[f"bRegex_{i}"] = "false"
        payload[f"bSearchable_{i}"] = "true"

    response = requests.post(api_url, params=params, data=payload, headers=headers)
    response.raise_for_status()
    data = response.json().get("data", [])

    for row in data:
        html_cell = row[-1]  # Last column contains the download link
        soup = BeautifulSoup(html_cell, "html.parser")
        link_tag = soup.find("a")

        if link_tag and link_tag.get("href"):
            partial_url = link_tag["href"].replace("//", "https://")
            file_name = os.path.basename(partial_url)
            full_path = os.path.join(output_dir, file_name)

            # Avoid re-downloading
            if not os.path.exists(full_path):
                download_file(partial_url, full_path)
