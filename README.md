**English** | [Русский](README.ru.md)

# 🔍 Yandex Search API (Pay Per Result): Search Results in Clean JSON

> Pay only for the results you get. The developer-friendly way to use the Yandex Search API.

**Actor page:** [apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema?fpr=9n7kx3)

This edition of the Yandex Search API bills per result returned, so your cost ties directly to how much you collect. It queries Yandex, the dominant search engine across Russia and several Eastern European and Central Asian markets, and returns clean, structured JSON, one item per page. Each item carries the search parameters, result counts, and arrays for organic results, ads, knowledge graph, inline images, and inline videos. Supports regional domains, language and region targeting, and pagination.

> Prefer per-page pricing instead of per-result? See the [pay-per-page edition](https://apify.com/johnvc/Scrape-Yandex?fpr=9n7kx3).

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Yandex-Pay-Per-Result.git
   cd Apify-Yandex-Pay-Per-Result
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
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

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python yandex-pay-per-result-scraper.py
```

## Why Use This Yandex Search API?

**Pay only for results.** Pay-per-result pricing ties your cost directly to what you collect, which suits exploratory research, keyword testing, and workloads where result density varies between queries.

**An independent search index.** Yandex maintains its own web index with distinct rankings, regional content, and Cyrillic-language coverage not replicated elsewhere. For Russian-language research, Eastern European markets, or comparative SEO, it is a unique source.

**Multi-domain support.** Target `yandex.ru`, `yandex.com`, `yandex.com.tr`, `yandex.by`, `yandex.kz`, and `yandex.uz`, then combine with `lang` and `lr` for precise control over the regional index and language variant.

**Rich result types.** Beyond organic results, each page returns ads, knowledge graph entries, inline image blocks, and inline video carousels in one structured output.

**Predictable, pay-per-use pricing.** Billing is per result, with no subscription, and the `max_pages` cap keeps cost under your control.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can run Yandex searches for you on demand.

## Features

### Core Capabilities
- **Yandex search** across 6 supported regional domains
- **A la carte result types**: toggle organic, ads, knowledge graph, inline images, and inline videos independently; you pay only for the types you turn on
- **Language and region control** with `lang` and `lr`
- **Sort and recency filters**: `sort_mode` (relevance or date) and `period` (all, day, last_two_weeks, month)
- **Parallel multi-page pagination** with a configurable `max_pages` cap
- **Pay-per-result billing** tied to what you collect

### Data Quality
- **One item per result type per page**, tagged with `item_type` and `result_count`
- **`organic_results` array** with position, title, link, snippet, and displayed link
- **Result counts and metadata** echoed on every item
- **Separate arrays** for ads, knowledge graph, images, and videos
- **Consistent JSON** shape across every query

## Usage Examples

### Basic search
```json
{
  "text": "machine learning tutorial",
  "max_pages": 1
}
```

### Regional domain with language and region targeting
```json
{
  "text": "машинное обучение учебник",
  "yandex_domain": "yandex.ru",
  "lang": "ru",
  "lr": "213",
  "max_pages": 1
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `text` | `string` | Yes | - | Search query. Supports any operator Yandex supports, e.g. `site:wikipedia.org python`. |
| `include_organic_results` | `boolean` | No | `true` | Return organic results (`item_type` `organic`). |
| `include_ads` | `boolean` | No | `false` | Return paid ads when present (`item_type` `ads`). |
| `include_knowledge_graph` | `boolean` | No | `false` | Return the knowledge graph card when present (`item_type` `knowledge_graph`). |
| `include_inline_images` | `boolean` | No | `false` | Return the inline image strip (`item_type` `inline_images`). |
| `include_inline_videos` | `boolean` | No | `false` | Return the inline video carousel (`item_type` `inline_videos`). |
| `yandex_domain` | `string` | No | `yandex.com` | Yandex domain, e.g. `yandex.ru`, `yandex.com.tr` (6 supported). |
| `lang` | `string` | No | (domain default) | Language code, e.g. `en`, `ru`. Comma-separated for multi-language. |
| `lr` | `string` | No | (domain default) | Country or region ID, e.g. `84` (USA), `213` (Moscow), `225` (Russia). |
| `max_pages` | `integer` | No | `2` | Maximum pages to fetch; `0` = unlimited. Applies to every selected result type. |
| `sort_mode` | `string` | No | `relevance` | Result ordering: `relevance` or `date` (newest first). |
| `period` | `string` | No | `all` | Recency window: `all`, `day`, `last_two_weeks`, `month`. |
| `output_file` | `string` | No | - | Optional filename to save results. |

## Output Format

Each selected result type present on a page is returned as its own dataset item, tagged with `item_type` (`organic`, `ads`, `knowledge_graph`, `inline_images`, or `inline_videos`) and a `result_count`; each item is billed as one result. A representative `organic` item for `machine learning tutorial` is shown below (the `organic_results` array is trimmed to a single result here).

```json
{
  "item_type": "organic",
  "result_count": 10,
  "text": "machine learning tutorial",
  "yandex_domain": "yandex.com",
  "lang": "en",
  "lr": "84",
  "max_pages": 1,
  "search_timestamp": "2026-05-29T11:51:33",
  "total_results_found": 10,
  "pages_processed": 1,
  "page_number": 1,
  "search_domain_description": "United States",
  "search_language_description": "English",
  "results_per_page": 10,
  "organic_results": [
    {
      "position": 2,
      "title": "Machine Learning Tutorial - GeeksforGeeks",
      "link": "https://www.geeksforgeeks.org/machine-learning/machine-learning/",
      "snippet": "Machine Learning is mainly divided into three core types: Supervised Learning: Trains models on labeled data to predict or classify new, unseen data.",
      "displayed_link": "geeksforgeeks.org > machine-learning > machine"
    }
  ],
  "ads_results": [],
  "knowledge_graph": [],
  "inline_images": [],
  "inline_videos": []
}
```

Each page item echoes the search parameters and result counts, lists every organic listing in `organic_results` (with position, title, link, snippet, and displayed link; video and news results may also include `duration` and `date`), and returns separate `ads_results`, `knowledge_graph`, `inline_images`, and `inline_videos` arrays.

---

## Use as an MCP tool

You can load the Yandex Search API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Yandex Search API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Yandex Search API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Yandex Search API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/yandex-scrape-yandex-search-results-at-scale---per-result`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result`, using OAuth when prompted.
5. Ask Claude to run the Yandex Search API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Yandex Search API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Yandex Search API to power SEO research, market intelligence, and multilingual content analysis with reliable, structured results.*

## Featured Tasks

Ready-to-run examples on the Apify Store.

- [Export Yandex Search Results to CSV](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/examples/export-yandex-search-results-to-csv?fpr=9n7kx3)

Last Updated: 2026.09.02
