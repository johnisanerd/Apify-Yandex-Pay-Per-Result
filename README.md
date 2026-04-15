# 🔍 Yandex Pay-Per-Result Scraper: Scrape Yandex Search Results with Python

> **The most efficient, reliable, and developer-friendly Yandex search scraper - pay only for results returned**

**Actor page:** [apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema?fpr=9n7kx3)

Scrape Yandex search results with Python using the [Yandex Pay-Per-Result scraper on Apify](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result?fpr=9n7kx3). Returns structured JSON with organic results, ads, knowledge graph entries, inline images, and inline videos - with pay-per-result pricing so you are only charged for the search results actually returned.

> Also available: [pay-per-event variant](https://apify.com/johnvc/Scrape-Yandex?fpr=9n7kx3) - better suited for high-volume runs where you expect consistent result counts per page.

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Yandex-Pay-Per-Result.git
   cd Apify-Yandex-Pay-Per-Result
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you don't have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python yandex-pay-per-result-scraper.py
   ```

### Alternative: Set API Key Directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python yandex-pay-per-result-scraper.py
```

## 🌟 Why Use This Yandex Pay-Per-Result Scraper?

The [Yandex Pay-Per-Result scraper on Apify](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result?fpr=9n7kx3) delivers structured search result data from Yandex - the dominant search engine across Russia and several Eastern European and Central Asian markets, with its own ranking signals, regional index, and result types distinct from Western search engines.

**Only Pay for What You Get**: Pay-per-result pricing ties your cost directly to the number of search results returned. Queries that surface fewer results cost less - making this model ideal for exploratory research, keyword testing, and workloads where result density varies significantly between queries.

**Access the Yandex Index**: Yandex maintains an independent web index with distinct rankings, regional content, and Cyrillic-language coverage not replicated in other search engines. For research involving Russian-language content, Eastern European markets, or comparative SEO analysis, Yandex data is irreplaceable.

**Multi-Domain Support**: Use the `yandex_domain` parameter to target `yandex.ru`, `yandex.com`, `yandex.com.tr`, or other regional Yandex domains. Combined with the `lang` and `lr` parameters, this gives precise control over which regional index and language variant you query.

**Rich Result Types**: Beyond organic results, the scraper captures ads, knowledge graph entries, inline image blocks, and inline video carousels - the full range of result types Yandex surfaces for a given query, all in a single structured output.

**Configurable Pagination**: Set `max_pages` to collect a shallow sample or a deep dataset. The default of 2 pages covers most research use cases, while higher values support large-scale SEO audits and content gap analysis.

**Production-Ready JSON Output**: All result types are returned with consistent field structures. Load directly into an SEO analysis pipeline, a competitive intelligence dashboard, or a multilingual content research workflow without additional parsing.

## 🎯 Common Use Cases for Yandex Search Data

**Russian-Language SEO Research**: Analyze rankings, featured snippets, and result types on Yandex for Russian-language keywords to inform content and SEO strategies targeting Russian-speaking audiences.

**Eastern European Market Intelligence**: Monitor how brands, products, and topics rank on Yandex across Russia, Kazakhstan, Belarus, and other markets where Yandex has strong search share.

**Multilingual Content Research**: Identify content gaps, trending topics, and authoritative sources in Cyrillic-language niches for content planning and localization projects.

**Competitive SERP Analysis**: Track competitor rankings, ad presence, and knowledge graph appearances on Yandex for target keywords over time.

**Academic and Linguistic Research**: Build datasets of Yandex search results for computational linguistics, information retrieval, or regional internet studies research.

**Ad Intelligence**: Collect Yandex ad copy and landing page data for competitive advertising research in Russian-language markets.

## ⚡ Features

### Core Capabilities
- **Yandex Search Index**: Queries Yandex's full search index with support for all major regional domains
- **Pay-Per-Result Pricing**: Charged only for search results actually returned, not pages processed
- **Multi-Domain Support**: Target `yandex.ru`, `yandex.com`, `yandex.com.tr`, and other regional domains
- **Language and Region Control**: Use `lang` and `lr` to target specific language variants and regional indexes
- **Configurable Pagination**: Set `max_pages` to control collection depth
- **Rich Result Types**: Captures organic results, ads, knowledge graph, inline images, and inline videos

### Data Quality
- **Consistent JSON Schema**: All result types share structured, predictable field names
- **Full Result Coverage**: Organic results, ads, knowledge graph, images, and videos in one output
- **Position Tracking**: Result position included for every organic listing
- **Per-Result Billing**: Charged per result returned, not per page, for accurate cost control

## 📖 Usage Examples

### Basic Search: Scrape Yandex for Any Keyword

```json
{
  "text": "python web scraping",
  "max_pages": 1
}
```

### Advanced Search: Regional Yandex Domain with Language Targeting

Retrieve Russian-language results from yandex.ru with 3 pages of results.

```json
{
  "text": "веб скрапинг на python",
  "yandex_domain": "yandex.ru",
  "lang": "ru",
  "lr": "213",
  "max_pages": 3
}
```

## 🔍 Input Parameters

Full input schema reference: [apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema?fpr=9n7kx3)

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `text` | `str` | YES | - | Search query |
| `yandex_domain` | `str` | no | `"yandex.com"` | Yandex domain (e.g. `"yandex.ru"`, `"yandex.com.tr"`) |
| `lang` | `str` | no | - | Language code (e.g. `"en"`, `"ru"`) |
| `lr` | `str` | no | - | Region/location code (e.g. `"213"` for Moscow) |
| `max_pages` | `int` | no | `2` | Maximum pages to scrape |
| `output_file` | `str` | no | - | Optional output filename |

## 📊 Output Format

Each run returns a dataset of structured JSON objects. Sample output:

```json
{
  "query": "best python web scraping libraries",
  "yandex_domain": "yandex.com",
  "lang": "en",
  "max_pages": 2,
  "pages_processed": 2,
  "organic_results": [
    {
      "position": 1,
      "title": "Top Python Web Scraping Libraries in 2025",
      "link": "https://realpython.com/python-web-scraping-libraries",
      "displayed_link": "realpython.com",
      "snippet": "A comprehensive comparison of the most popular Python scraping libraries including Scrapy, BeautifulSoup, Playwright, and httpx..."
    },
    {
      "position": 2,
      "title": "Beautiful Soup vs Scrapy: Which Should You Use?",
      "link": "https://towardsdatascience.com/example",
      "displayed_link": "towardsdatascience.com",
      "snippet": "Both libraries are excellent choices depending on your use case. Here is a breakdown of when to use each..."
    }
  ],
  "ads": [],
  "knowledge_graph": null,
  "inline_images": [],
  "inline_videos": [],
  "search_metadata": {
    "total_results_found": 94,
    "pages_processed": 2
  }
}
```

---

[**Made with love**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your data collection with the most reliable and efficient scraper on the market.*

Last Updated: 2026.04.15
