"""
Yandex Pay-Per-Result Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result?fpr=9n7kx3
Input schema: https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema?fpr=9n7kx3

This script demonstrates how to scrape Yandex search results using the
pay-per-result pricing model - you are only charged for results returned.
Captures organic results, ads, knowledge graph, inline images, and videos.

Also available: pay-per-event variant at https://apify.com/johnvc/Scrape-Yandex?fpr=9n7kx3

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "text": "best python web scraping libraries",
    "yandex_domain": "yandex.com",
    "lang": "en",
    "max_pages": 2,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/yandex-scrape-yandex-search-results-at-scale---per-result").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
