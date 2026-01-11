"""
Crawl4AI MCP Server - Unofficial Implementation

An unofficial Model Context Protocol server that wraps the excellent crawl4ai
library to provide advanced web crawling capabilities through MCP interface.

Original crawl4ai: https://github.com/unclecode/crawl4ai by unclecode
This MCP wrapper: https://github.com/walksoda/crawl-mcp by walksoda

This is NOT an official crawl4ai project.
"""

__version__ = "0.1.2"
__author__ = "walksoda"
__email__ = "walksoda@users.noreply.github.com"
__original_lib__ = "crawl4ai"
__original_author__ = "unclecode"
__original_url__ = "https://github.com/unclecode/crawl4ai"
__license__ = "MIT"
__status__ = "Unofficial Third-party Implementation"

# Comprehensive Tool Selection Guide for AI Agents
# This guide helps AI systems choose the most appropriate tool for different tasks
TOOL_SELECTION_GUIDE = {
    # === SINGLE CONTENT EXTRACTION ===
    "single_url_content": "crawl_url",
    "general_webpage_content": "crawl_url", 
    "article_extraction": "crawl_url",
    "single_page_analysis": "crawl_url",
    "content_from_one_url": "crawl_url",
    
    # === MULTI-PAGE WEBSITE ANALYSIS ===
    "multiple_pages_same_site": "deep_crawl_site",
    "site_mapping": "deep_crawl_site",
    "documentation_crawling": "deep_crawl_site", 
    "blog_section_analysis": "deep_crawl_site",
    "product_catalog_extraction": "deep_crawl_site",
    "website_structure_analysis": "deep_crawl_site",
    
    # === TARGETED DATA EXTRACTION ===
    "specific_data_extraction": "intelligent_extract",
    "product_information": "intelligent_extract",
    "pricing_data": "intelligent_extract",
    "company_details": "intelligent_extract",
    "financial_metrics": "intelligent_extract",
    "technical_specifications": "intelligent_extract",
    "ai_powered_extraction": "intelligent_extract",
    
    # === PATTERN-BASED ENTITY EXTRACTION ===
    "contact_info_patterns": "extract_entities",
    "email_extraction": "extract_entities",
    "phone_number_extraction": "extract_entities",
    "url_collection": "extract_entities",
    "date_extraction": "extract_entities",
    "social_media_links": "extract_entities",
    "lead_generation": "extract_entities",
    "regex_pattern_matching": "extract_entities",
    
    # === STRUCTURED DATA EXTRACTION ===
    "structured_data_extraction": "extract_structured_data",
    "css_selector_extraction": "extract_structured_data",
    "form_data_extraction": "extract_structured_data",
    "table_data_extraction": "extract_structured_data",
    "schema_based_extraction": "extract_structured_data",
    
    # === DOCUMENT PROCESSING ===
    "document_conversion": "process_file",
    "pdf_processing": "process_file",
    "office_document_processing": "process_file",
    "file_to_markdown": "process_file",
    "archive_extraction": "process_file",
    "research_paper_processing": "process_file",
    
    # === VIDEO CONTENT PROCESSING ===
    "video_to_text": "extract_youtube_transcript",
    "youtube_transcript": "extract_youtube_transcript",
    "video_content_analysis": "extract_youtube_transcript",
    "accessibility_transcription": "extract_youtube_transcript",
    "video_summarization": "extract_youtube_transcript",
    
    # === BATCH VIDEO PROCESSING ===
    "multiple_youtube_videos": "batch_extract_youtube_transcripts",
    "bulk_video_transcription": "batch_extract_youtube_transcripts",
    "video_playlist_processing": "batch_extract_youtube_transcripts",
    
    # === YOUTUBE VIDEO INFORMATION ===
    "youtube_video_info": "get_youtube_video_info",
    "video_metadata": "get_youtube_video_info",
    "transcript_availability": "get_youtube_video_info",
    
    # === SEARCH OPERATIONS (use crawl_url with Google search URLs) ===
    # For Google search, use crawl_url with URLs like:
    # - Web: https://www.google.com/search?q=query
    # - News: https://www.google.com/search?q=query&tbm=nws
    # - Videos: https://www.google.com/search?q=query&tbm=vid
    # - Images: https://www.google.com/search?q=query&tbm=isch
    # Time filters: &tbs=qdr:d (24h), &tbs=qdr:w (week), &tbs=qdr:m (month)
    "search_only": "crawl_url",
    "google_search_results": "crawl_url",
    "research_queries": "crawl_url",
    "fact_checking": "crawl_url",
    "genre_specific_search": "crawl_url",
    "academic_search": "crawl_url",

    # === SEARCH + CONTENT EXTRACTION ===
    "search_plus_content": "crawl_url",
    "comprehensive_research": "crawl_url",
    "competitive_analysis": "crawl_url",
    "market_research": "crawl_url",
    "content_aggregation": "crawl_url",
    "search_and_analyze": "crawl_url",

    # === BATCH SEARCH OPERATIONS ===
    "multiple_search_queries": "crawl_url",
    "bulk_search_analysis": "crawl_url",
    "comparative_search": "crawl_url",
    
    # === BATCH CONTENT PROCESSING ===
    "multiple_urls_processing": "batch_crawl",
    "bulk_content_extraction": "batch_crawl",
    "list_of_websites": "batch_crawl",
    "concurrent_crawling": "batch_crawl",
    
    # === ENHANCED CRAWLING ===
    "fallback_crawling": "crawl_url_with_fallback",
    "robust_content_extraction": "crawl_url_with_fallback",
    "difficult_websites": "crawl_url_with_fallback",
    "multi_strategy_crawling": "crawl_url_with_fallback",
    
    # === CONFIGURATION & METADATA ===
    "llm_configuration": "get_llm_config_info",
    "available_models": "get_llm_config_info",
    "system_capabilities": "get_llm_config_info",
    
    "file_format_support": "get_supported_file_formats",
    "document_capabilities": "get_supported_file_formats",
    
    "youtube_setup_info": "get_youtube_api_setup_guide",
    "youtube_capabilities": "get_youtube_api_setup_guide",
}

# Workflow-based tool selection guide
WORKFLOW_GUIDE = {
    # === RESEARCH WORKFLOWS ===
    "market_research_workflow": ["crawl_url", "deep_crawl_site", "intelligent_extract"],
    "competitive_analysis_workflow": ["crawl_url", "deep_crawl_site", "intelligent_extract"],
    "academic_research_workflow": ["crawl_url", "process_file", "extract_youtube_transcript"],
    "lead_generation_workflow": ["crawl_url", "extract_entities", "intelligent_extract"],

    # === CONTENT ANALYSIS WORKFLOWS ===
    "website_audit_workflow": ["crawl_url", "deep_crawl_site", "extract_entities"],
    "document_analysis_workflow": ["process_file", "intelligent_extract", "extract_entities"],
    "video_content_workflow": ["extract_youtube_transcript", "intelligent_extract"],
    "bulk_processing_workflow": ["batch_crawl", "batch_extract_youtube_transcripts"],

    # === DATA EXTRACTION WORKFLOWS ===
    "contact_discovery_workflow": ["crawl_url", "extract_entities", "intelligent_extract"],
    "pricing_analysis_workflow": ["crawl_url", "intelligent_extract"],
    "product_research_workflow": ["crawl_url", "deep_crawl_site", "intelligent_extract"],
    "documentation_extraction_workflow": ["deep_crawl_site", "process_file", "intelligent_extract"],
}

# Task complexity mapping
COMPLEXITY_GUIDE = {
    "simple_single_task": ["crawl_url", "extract_entities", "process_file"],
    "moderate_multi_step": ["intelligent_extract", "deep_crawl_site", "crawl_url"],
    "complex_bulk_operations": ["batch_crawl", "batch_extract_youtube_transcripts"],
    "advanced_workflows": ["crawl_url_with_fallback", "extract_structured_data"],
}