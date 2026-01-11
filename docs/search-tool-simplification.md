# Search Tool Simplification

## Overview

Simplified Google search functionality by removing dedicated search tools and enabling direct Google search URL crawling via the `crawl_url` tool.

## Changes Made

### 1. Updated `crawl_url` Tool Description

**File:** `crawl4ai_mcp/server.py` (line 348)

Added Google search URL usage instructions to the docstring:

```python
"""Extract web page content with JavaScript support. Use wait_for_js=true for SPAs.
For Google search, use URLs like: https://www.google.com/search?q=query (web),
add &tbm=nws (news), &tbm=vid (videos), &tbm=isch (images)."""
```

### 2. Removed `search_google` MCP Tool

**File:** `crawl4ai_mcp/server.py` (line 1475)

Removed the `@mcp.tool()` decorator from `search_google` function. The function remains available internally but is no longer exposed as an MCP tool.

**Original tool parameters:**
- `query` (required)
- `num_results`
- `search_genre` (academic, news, technical, commercial, social)
- `language`
- `region`
- `recent_days`

### 3. Removed `search_and_crawl` MCP Tool

**File:** `crawl4ai_mcp/server.py` (line 1530)

Removed the `@mcp.tool()` decorator from `search_and_crawl` function. The function remains available internally but is no longer exposed as an MCP tool.

**Original tool parameters:**
- `search_query` (required)
- `crawl_top_results`
- `search_genre`
- `recent_days`

## Google Search URL Reference

LLMs can now perform Google searches using `crawl_url` with these URL patterns:

| Search Type | URL Pattern |
|-------------|-------------|
| Web Search | `https://www.google.com/search?q=your+query` |
| News | `https://www.google.com/search?q=your+query&tbm=nws` |
| Videos | `https://www.google.com/search?q=your+query&tbm=vid` |
| Images | `https://www.google.com/search?q=your+query&tbm=isch` |

### Additional URL Parameters

- `&tbs=qdr:d` - Past 24 hours
- `&tbs=qdr:w` - Past week
- `&tbs=qdr:m` - Past month
- `&hl=en` - Language (en, ja, etc.)
- `&gl=us` - Region/country

### Example Usage

```
# News search for "Iran protest"
crawl_url("https://www.google.com/search?q=Iran+protest&tbm=nws")

# Recent news (past week)
crawl_url("https://www.google.com/search?q=climate+change&tbm=nws&tbs=qdr:w")

# Web search in Japanese
crawl_url("https://www.google.com/search?q=東京+天気&hl=ja&gl=jp")
```

## Benefits

1. **Reduced complexity** - Fewer tools for LLMs to understand
2. **Lower token usage** - Simpler tool descriptions
3. **More flexible** - Direct URL control allows any Google search parameters
4. **Transparent** - LLMs see exactly what URL is being crawled

## Additional Fixes

### 4. Updated `__init__.py` Tool Selection Guides

**File:** `crawl4ai_mcp/__init__.py`

Updated all tool selection guides to replace search tool references with `crawl_url`:

- `TOOL_SELECTION_GUIDE` (lines 91-116): Replaced `search_google`, `search_and_crawl`, `batch_search_google` with `crawl_url`. Added comments explaining Google search URL patterns.
- Removed `search_genres` and `available_search_types` entries.
- `WORKFLOW_GUIDE` (lines 142-161): Replaced search tools with `crawl_url` and `deep_crawl_site`.
- `COMPLEXITY_GUIDE` (lines 163-169): Removed all search tool references.

### 5. Updated `get_tool_selection_guide()` in server.py

**File:** `crawl4ai_mcp/server.py` (line 2038)

Changed:
```python
"search": ["search_google", "batch_search_google", "search_and_crawl", "get_search_genres"],
```

To:
```python
"google_search": "Use crawl_url with Google search URLs: https://www.google.com/search?q=query (web), &tbm=nws (news), &tbm=vid (videos), &tbm=isch (images)",
```

## Internal Functions Retained

The following functions remain in the codebase for potential internal use but are not exposed as MCP tools:

- `search_google()` - Google search with genre filtering
- `search_and_crawl()` - Combined search and crawl
- `batch_search_google()` - Multiple searches (was never exposed)
- `get_search_genres()` - List available genres (was never exposed)
