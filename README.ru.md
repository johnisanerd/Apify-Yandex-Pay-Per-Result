[English](README.md) | **Русский**

# 🔍 Yandex Search API (оплата за результат): выдача в чистом JSON

> Платите только за полученные результаты. Удобный для разработчиков способ работать с Yandex Search API.

**Страница актора:** [apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result?fpr=9n7kx3)
**Схема ввода:** [apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema](https://apify.com/johnvc/yandex-scrape-yandex-search-results-at-scale---per-result/input-schema?fpr=9n7kx3)

Эта редакция Yandex Search API тарифицируется за каждый возвращённый результат, поэтому стоимость напрямую зависит от объёма собранных данных. Она выполняет запросы к Яндексу - ведущему поисковику в России и ряде рынков Восточной Европы и Центральной Азии - и возвращает чистый структурированный JSON, по одному элементу на страницу. Каждый элемент содержит параметры поиска, счётчики результатов и массивы для органики, рекламы, графа знаний, изображений и видео. Поддерживаются региональные домены, таргетинг по языку и региону и пагинация.

> Предпочитаете оплату за страницу вместо оплаты за результат? Смотрите [редакцию с оплатой за страницу](https://apify.com/johnvc/Scrape-Yandex?fpr=9n7kx3).

## Видеообзор

[![Смотреть обзор](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Быстрый старт

### Требования
- Python 3.11 или новее
- Аккаунт Apify и ключ API ([получить бесплатный ключ](https://apify.com?fpr=9n7kx3))

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Yandex-Pay-Per-Result.git
   cd Apify-Yandex-Pay-Per-Result
   ```

2. **Установите зависимости через UV**
   ```bash
   # Установите UV, если его нет:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Установите зависимости проекта:
   uv sync
   ```

3. **Настройте ключ API**
   ```bash
   cp .env.example .env
   # Откройте .env и добавьте свой ключ API Apify
   # Получите бесплатный ключ: https://apify.com?fpr=9n7kx3
   ```

4. **Запустите пример**
   ```bash
   uv run python yandex-pay-per-result-scraper.py
   ```

### Альтернатива: задать ключ напрямую
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python yandex-pay-per-result-scraper.py
```

## Почему стоит использовать этот Yandex Search API?

**Платите только за результаты.** Оплата за результат напрямую связывает стоимость с объёмом собранных данных, что удобно для разведочных исследований, тестирования ключевых слов и задач, где плотность результатов меняется от запроса к запросу.

**Независимый поисковый индекс.** Яндекс ведёт собственный веб-индекс с уникальным ранжированием, региональным контентом и охватом кириллических языков, которого нет в других системах. Для русскоязычных исследований, рынков Восточной Европы или сравнительного SEO это уникальный источник.

**Поддержка нескольких доменов.** Используйте `yandex.ru`, `yandex.com`, `yandex.com.tr`, `yandex.by`, `yandex.kz` и `yandex.uz`, сочетая их с `lang` и `lr` для точного контроля региона и языка.

**Богатые типы результатов.** Помимо органики каждая страница возвращает рекламу, карточки графа знаний, блоки изображений и карусели видео в одном структурированном выводе.

**Предсказуемая оплата по факту использования.** Тарификация за результат, без подписки, а лимит `max_pages` держит расходы под контролем.

**Простая автоматизация.** Вызывайте из Python в несколько строк или подключите как инструмент MCP, чтобы ассистенты Claude и Cursor выполняли поиск в Яндексе по вашему запросу.

## Возможности

### Основные возможности
- **Поиск в Яндексе** по 6 поддерживаемым региональным доменам
- **Типы результатов по выбору**: включайте органику, рекламу, граф знаний, изображения и видео по отдельности; вы платите только за включённые типы
- **Контроль языка и региона** через `lang` и `lr`
- **Фильтры сортировки и периода**: `sort_mode` (relevance или date) и `period` (all, day, last_two_weeks, month)
- **Параллельная постраничная навигация** с настраиваемым лимитом `max_pages`
- **Оплата за результат**, привязанная к объёму собранных данных

### Качество данных
- **Один элемент на тип результата на странице**, с полями `item_type` и `result_count`
- **Массив `organic_results`**: позиция, заголовок, ссылка, описание и отображаемая ссылка
- **Счётчики результатов и метаданные** в каждом элементе
- **Отдельные массивы** для рекламы, графа знаний, изображений и видео
- **Единообразный JSON** для каждого запроса

## Примеры использования

### Базовый поиск
```json
{
  "text": "machine learning tutorial",
  "max_pages": 1
}
```

### Региональный домен с таргетингом по языку и региону
```json
{
  "text": "машинное обучение учебник",
  "yandex_domain": "yandex.ru",
  "lang": "ru",
  "lr": "213",
  "max_pages": 1
}
```

## Входные параметры

| Параметр | Тип | Обязательный | По умолчанию | Описание |
|-----------|------|----------|---------|-------------|
| `text` | `string` | Да | - | Поисковый запрос. Поддерживает любые операторы Яндекса, например `site:wikipedia.org python`. |
| `include_organic_results` | `boolean` | Нет | `true` | Возвращать органическую выдачу (`item_type` `organic`). |
| `include_ads` | `boolean` | Нет | `false` | Возвращать рекламу, если присутствует (`item_type` `ads`). |
| `include_knowledge_graph` | `boolean` | Нет | `false` | Возвращать карточку графа знаний (`item_type` `knowledge_graph`). |
| `include_inline_images` | `boolean` | Нет | `false` | Возвращать блок изображений (`item_type` `inline_images`). |
| `include_inline_videos` | `boolean` | Нет | `false` | Возвращать блок видео (`item_type` `inline_videos`). |
| `yandex_domain` | `string` | Нет | `yandex.com` | Домен Яндекса, например `yandex.ru`, `yandex.com.tr` (поддерживается 6). |
| `lang` | `string` | Нет | (по домену) | Код языка, например `en`, `ru`. Через запятую для нескольких языков. |
| `lr` | `string` | Нет | (по домену) | Идентификатор страны или региона, например `84` (США), `213` (Москва), `225` (Россия). |
| `max_pages` | `integer` | Нет | `2` | Максимум страниц; `0` = без лимита. Применяется ко всем выбранным типам. |
| `sort_mode` | `string` | Нет | `relevance` | Сортировка: `relevance` или `date` (сначала новые). |
| `period` | `string` | Нет | `all` | Период: `all`, `day`, `last_two_weeks`, `month`. |
| `output_file` | `string` | Нет | - | Имя файла для сохранения результатов. |

## Формат вывода

Каждый выбранный тип результатов, присутствующий на странице, возвращается отдельным элементом с полем `item_type` (`organic`, `ads`, `knowledge_graph`, `inline_images`, `inline_videos`) и `result_count`; каждый элемент оплачивается как один результат. Ниже показан элемент `organic` для `machine learning tutorial` (массив `organic_results` сокращён до одного результата).

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

Каждый элемент страницы повторяет параметры поиска и счётчики результатов, перечисляет всю органику в `organic_results` (позиция, заголовок, ссылка, описание и отображаемая ссылка; для видео и новостей могут добавляться `duration` и `date`) и возвращает отдельные массивы `ads_results`, `knowledge_graph`, `inline_images` и `inline_videos`.

---

## Использование как инструмент MCP

Вы можете подключить Yandex Search API как инструмент MCP, чтобы ассистенты вызывали его за вас. URL сервера MCP предзагружает только этот актор:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result
```

Авторизуйтесь через OAuth в браузере, когда будет предложено, или с помощью токена API Apify (тот же `APIFY_API_TOKEN`, что и в примере на Python). Получите токен на https://console.apify.com/settings/integrations и бесплатный аккаунт Apify на https://apify.com?fpr=9n7kx3 .

## Установка в Claude Cowork Desktop

![Установка в Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork - это режим автоматизации в десктоп-приложении. Чтобы дать ему Yandex Search API как инструмент, добавьте сервер Apify MCP как коннектор.

1. Откройте приложение Claude и перейдите в **Settings → Connectors** (или **Settings → Developer → Edit Config**, чтобы редактировать `claude_desktop_config.json` напрямую).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Добавьте сервер Apify MCP, предзагруженный только этим актором:

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

3. Перезапустите приложение. При первом вызове инструмента в Cowork пройдите OAuth в браузере или добавьте токен API Apify в настройках коннектора, чтобы пропустить OAuth.
4. В чате Cowork убедитесь, что инструмент доступен, и попросите запустить Yandex Search API.

Скачайте приложение и начните бесплатный период: https://claude.ai/referral/uIlpa7nPLg
Подробнее: https://docs.apify.com/platform/integrations/claude-desktop

## Установка в Claude Code

![Установка в Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code - это инструмент командной строки. Добавьте сервер MCP актора одной командой:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result"
```

Чтобы использовать токен вместо OAuth в браузере:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Затем проверьте через `claude mcp list` или выполните `/mcp` в сессии. Попросите Claude Code вызвать Yandex Search API.

Попробуйте Claude Code бесплатно: https://claude.ai/referral/uIlpa7nPLg
Документация MCP: https://code.claude.com/docs/en/mcp

## Установка в Claude (веб-сайт)

![Установка в Claude (веб-сайт)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

На claude.ai вы добавляете Apify как коннектор, затем включаете инструмент именно этого актора.

1. Перейдите в **Settings → Connectors → Browse connectors** и найдите **Apify MCP server**. Установите его (включите или обновите при необходимости).
2. При подключении авторизуйтесь токеном API Apify и включите инструмент `johnvc/yandex-scrape-yandex-search-results-at-scale---per-result`.
3. В любом чате откройте **+ → Connectors** и включите **Apify**.
4. Или выберите **Add custom connector** и вставьте полный URL MCP `https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result`, пройдя OAuth при запросе.
5. Попросите Claude запустить Yandex Search API.

Откройте Claude в браузере: https://claude.ai

## Установка в Cursor

![Установка в Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor читает серверы MCP из файла проекта `.cursor/mcp.json`.

1. В вашем проекте создайте `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result"
    }
  }
}
```

2. Если предпочитаете токен вместо OAuth, добавьте заголовок:

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

3. Откройте **Cursor → Settings → MCP** и убедитесь, что сервер **apify** подключён (зелёная точка).
4. В Composer или Chat попросите Cursor вызвать Yandex Search API.

Впервые в Cursor? Скачайте: https://cursor.com/referral?code=XQP4VBLI3NNX

## Установка в ChatGPT

![Установка в ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT подключается к серверу Apify MCP через режим разработчика (доступен в планах ChatGPT Pro, Plus, Business, Enterprise и Education).

1. Нажмите на иконку профиля, затем перейдите в **Settings > Apps**. Если нет кнопки **Create app**, откройте **Advanced settings** и включите **Developer mode**.
2. Нажмите **Create app** и заполните форму:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/yandex-scrape-yandex-search-results-at-scale---per-result`
   - **Authentication:** OAuth
3. Нажмите **Create** и авторизуйте подключение к Apify.
4. Чтобы использовать приложение в диалоге, нажмите **+** в чате, выберите **Developer mode** и затем **Apify**.

Подробнее: https://docs.apify.com/platform/integrations/mcp

---

[**Сделано с заботой**](https://apify.com/johnvc?fpr=9n7kx3)

*Используйте Yandex Search API для SEO-исследований, рыночной аналитики и многоязычного анализа контента с надёжными структурированными результатами.*

Last Updated: 2026.06.13
