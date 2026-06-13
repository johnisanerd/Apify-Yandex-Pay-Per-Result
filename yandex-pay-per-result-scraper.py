"""
Example: call the Yandex Search API (Pay Per Result) Apify Actor from Python.

Get a free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.

The Actor is billed per result returned: each selected result type present on a
page is one paid dataset item, so you pay only for the types you turn on. The
example fetches a single page and only a couple of result types so the first run
is inexpensive; raise max_pages or enable more types when you want deeper coverage.

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

# Inputs are kept small so the first run is inexpensive: one page, and only two
# result types enabled (organic + knowledge graph). Each enabled type that
# appears is one paid item, so enable only what you need.
# Параметры небольшие, чтобы первый запуск был дешёвым: одна страница и только
# два типа результатов (органика + граф знаний). Каждый включённый тип, который
# присутствует, оплачивается как один элемент.
run_input = {
    "text": "machine learning tutorial",
    # A la carte result types. Organic is on by default; the others are opt-in.
    "include_organic_results": True,
    "include_ads": False,
    "include_knowledge_graph": True,
    "include_inline_images": False,
    "include_inline_videos": False,
    "yandex_domain": "yandex.com",
    "lang": "en",
    "lr": "84",
    "sort_mode": "relevance",   # "relevance" (default) or "date" (newest first)
    "period": "all",            # time window: all | day | last_two_weeks | month
    "max_pages": 1,
}

# Russian-market example. Swap it in to search the Russian index in Russian,
# localized to Moscow (lr=213), newest-first within the last two weeks.
# Пример для российского рынка: русский индекс, локализация по Москве (lr=213),
# сортировка по дате за последние две недели.
# run_input = {
#     "text": "машинное обучение учебник",
#     "yandex_domain": "yandex.ru",
#     "lang": "ru",
#     "lr": "213",
#     "sort_mode": "date",
#     "period": "last_two_weeks",
#     "max_pages": 1,
# }

print(f"Searching Yandex for: {run_input['text']}")
run = client.actor("johnvc/yandex-scrape-yandex-search-results-at-scale---per-result").call(run_input=run_input)

if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

# Each selected result type present on a page is returned as its own dataset
# item, tagged with "item_type" (organic, ads, knowledge_graph, inline_images,
# inline_videos) and a "result_count". Map each type to the array holding its rows.
ARRAY_KEY = {
    "organic": "organic_results",
    "ads": "ads_results",
    "knowledge_graph": "knowledge_graph",
    "inline_images": "inline_images",
    "inline_videos": "inline_videos",
}

for item in client.dataset(run.default_dataset_id).iterate_items():
    item_type = item.get("item_type", "organic")
    rows = item.get(ARRAY_KEY.get(item_type, "organic_results"), []) or []
    print(
        f"\n[{item_type}] page {item.get('page_number', '?')}: "
        f"{item.get('result_count', len(rows))} result(s)\n"
    )

    for row in rows:
        # organic/ads/images/videos expose title + link; knowledge graph uses title + description.
        title = row.get("title", "")
        detail = row.get("link") or row.get("description", "")
        snippet = (row.get("snippet") or "").replace("\n", " ").strip()
        position = row.get("position")
        print(f"{position if position else '-'}. {title}")
        if detail:
            print(f"   {detail}")
        if snippet:
            print(f"   {snippet[:160]}...")
        print()
