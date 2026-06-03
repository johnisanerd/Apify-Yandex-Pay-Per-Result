"""
Example: call the Yandex Search API (Pay Per Result) Apify Actor from Python.

Get a free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.

The Actor is billed per result returned, and each page is one paid item. The
example fetches a single page so the first run is inexpensive; raise max_pages
when you want deeper coverage.

Also available: a pay-per-page edition at https://apify.com/johnvc/Scrape-Yandex?fpr=9n7kx3
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

# Inputs are kept small so the first run is inexpensive: one page of results.
# Параметры небольшие, чтобы первый запуск был дешёвым: одна страница результатов.
run_input = {
    "text": "machine learning tutorial",
    "yandex_domain": "yandex.com",
    "lang": "en",
    "lr": "84",
    "max_pages": 1,
}

# Russian-market example. Swap it in to search the Russian index in Russian,
# localized to Moscow (lr=213). | Пример для российского рынка: поиск в русском
# индексе на русском языке с локализацией по Москве (lr=213).
# run_input = {
#     "text": "машинное обучение учебник",
#     "yandex_domain": "yandex.ru",
#     "lang": "ru",
#     "lr": "213",
#     "max_pages": 1,
# }

print(f"Searching Yandex for: {run_input['text']}")
run = client.actor("johnvc/yandex-scrape-yandex-search-results-at-scale---per-result").call(run_input=run_input)

if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

# One dataset item is returned per page; each page holds organic_results plus
# ads, knowledge graph, inline images, and inline videos.
for page in client.dataset(run.default_dataset_id).iterate_items():
    organic = page.get("organic_results", [])
    print(
        f"\nPage {page.get('page_number', '?')}: "
        f"{len(organic)} organic results (total found: {page.get('total_results_found', 'n/a')})\n"
    )

    for result in organic:
        title = result.get("title", "")
        displayed = result.get("displayed_link", "")
        link = result.get("link", "")
        snippet = (result.get("snippet") or "").replace("\n", " ").strip()

        print(f"{result.get('position', '?')}. {title}")
        print(f"   {displayed}")
        print(f"   {link}")
        if snippet:
            print(f"   {snippet[:160]}...")
        print()

    extras = {
        "ads": len(page.get("ads_results", [])),
        "knowledge_graph": len(page.get("knowledge_graph", [])),
        "inline_images": len(page.get("inline_images", [])),
        "inline_videos": len(page.get("inline_videos", [])),
    }
    print(f"Other blocks on this page: {extras}")
