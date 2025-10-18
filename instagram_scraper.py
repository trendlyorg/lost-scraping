#!/usr/bin/env python3
"""
Instagram Keyword Scraper using Apify

This script scrapes Instagram posts based on keyword searches using Apify's
Instagram Search Scraper. It can search for posts related to specific keywords
like "koh phangan best coffee" and export the results to JSON/CSV format.
"""

import os
import json
import csv
import time
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path

from apify_client import ApifyClient
from dotenv import load_dotenv
import pandas as pd


class InstagramKeywordScraper:
    """Instagram keyword scraper using Apify's Instagram Search Scraper."""
    
    def __init__(self, api_token: Optional[str] = None):
        """
        Initialize the scraper with Apify API token.
        
        Args:
            api_token: Apify API token. If None, will try to load from .env file.
        """
        if api_token is None:
            load_dotenv()
            api_token = os.getenv('APIFY_API_TOKEN')
            
        if not api_token:
            raise ValueError("Apify API token is required. Set APIFY_API_TOKEN in .env file or pass as parameter.")
            
        self.client = ApifyClient(api_token)
        self.actor_id = "apify/instagram-search-scraper"
        
    def scrape_keyword(self, 
                      keyword: str, 
                      search_type: str = "place",
                      search_limit: int = 10,
                      results_type: str = "posts",
                      results_limit: int = 100,
                      proxy_config: Optional[Dict] = None) -> Dict:
        """
        Scrape Instagram posts for a specific keyword.
        
        Args:
            keyword: The search keyword (e.g., "koh phangan best coffee")
            search_type: Type of search - "place", "profile", or "hashtag"
            search_limit: Number of search results to process
            results_type: Type of results to fetch - "posts" or "profiles"
            results_limit: Maximum number of results to retrieve per search result
            proxy_config: Optional proxy configuration
            
        Returns:
            Dictionary containing scraped data and metadata
        """
        print(f"🔍 Starting Instagram keyword search for: '{keyword}'")
        print(f"📊 Search type: {search_type}, Results type: {results_type}")
        print(f"📈 Limits: search={search_limit}, results={results_limit}")
        
        # Prepare input configuration
        run_input = {
            "search": keyword,
            "searchType": search_type,
            "searchLimit": search_limit,
            "resultsType": results_type,
            "resultsLimit": results_limit,
        }
        
        # Add proxy configuration if provided
        if proxy_config:
            run_input.update(proxy_config)
            
        try:
            # Start the scraper run
            print("🚀 Starting Apify scraper...")
            run = self.client.actor(self.actor_id).call(run_input=run_input)
            
            if run['status'] != 'SUCCEEDED':
                raise Exception(f"Scraper run failed with status: {run['status']}")
                
            print("✅ Scraper completed successfully!")
            
            # Get the dataset items
            print("📥 Retrieving scraped data...")
            dataset_items = list(self.client.dataset(run['defaultDatasetId']).iterate_items())
            
            print(f"📊 Retrieved {len(dataset_items)} items")
            
            # Prepare result data
            result = {
                "metadata": {
                    "keyword": keyword,
                    "search_type": search_type,
                    "results_type": results_type,
                    "search_limit": search_limit,
                    "results_limit": results_limit,
                    "total_items": len(dataset_items),
                    "scraped_at": datetime.now().isoformat(),
                    "apify_run_id": run['id']
                },
                "data": dataset_items
            }
            
            return result
            
        except Exception as e:
            print(f"❌ Error during scraping: {str(e)}")
            raise
    
    def save_to_json(self, data: Dict, filename: Optional[str] = None) -> str:
        """
        Save scraped data to JSON file.
        
        Args:
            data: The scraped data dictionary
            filename: Optional custom filename. If None, auto-generates based on keyword and timestamp.
            
        Returns:
            Path to the saved JSON file
        """
        if filename is None:
            keyword = data['metadata']['keyword'].replace(' ', '_')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"instagram_{keyword}_{timestamp}.json"
            
        # Ensure output directory exists
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"💾 Data saved to JSON: {filepath}")
        return str(filepath)
    
    def save_to_csv(self, data: Dict, filename: Optional[str] = None) -> str:
        """
        Save scraped data to CSV file.
        
        Args:
            data: The scraped data dictionary
            filename: Optional custom filename. If None, auto-generates based on keyword and timestamp.
            
        Returns:
            Path to the saved CSV file
        """
        if not data['data']:
            print("⚠️ No data to save to CSV")
            return ""
            
        if filename is None:
            keyword = data['metadata']['keyword'].replace(' ', '_')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"instagram_{keyword}_{timestamp}.csv"
            
        # Ensure output directory exists
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        filepath = output_dir / filename
        
        # Convert to DataFrame and save
        df = pd.json_normalize(data['data'])
        df.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"💾 Data saved to CSV: {filepath}")
        return str(filepath)
    
    def print_summary(self, data: Dict):
        """Print a summary of the scraped data."""
        metadata = data['metadata']
        items = data['data']
        
        print("\n" + "="*50)
        print("📊 SCRAPING SUMMARY")
        print("="*50)
        print(f"🔍 Keyword: {metadata['keyword']}")
        print(f"📋 Search Type: {metadata['search_type']}")
        print(f"📋 Results Type: {metadata['results_type']}")
        print(f"📈 Total Items: {metadata['total_items']}")
        print(f"⏰ Scraped At: {metadata['scraped_at']}")
        
        if items:
            print(f"\n📝 Sample Data Fields:")
            sample_item = items[0]
            for key in list(sample_item.keys())[:10]:  # Show first 10 fields
                print(f"   - {key}")
            if len(sample_item.keys()) > 10:
                print(f"   ... and {len(sample_item.keys()) - 10} more fields")
        print("="*50)


def main():
    """Main function to demonstrate the scraper usage."""
    try:
        # Initialize scraper
        scraper = InstagramKeywordScraper()
        
        # Example: Scrape posts for "koh phangan best coffee"
        keyword = "koh phangan best coffee"
        
        # Configure search parameters
        search_config = {
            "search_type": "place",  # Search for places
            "search_limit": 5,       # Process 5 search results
            "results_type": "posts", # Get posts
            "results_limit": 20      # Max 20 posts per search result
        }
        
        # Optional: Add proxy configuration for better reliability
        # proxy_config = {
        #     "proxy": {
        #         "useApifyProxy": True,
        #         "apifyProxyGroups": ["RESIDENTIAL"]
        #     }
        # }
        
        # Scrape the data
        result = scraper.scrape_keyword(keyword, **search_config)
        
        # Print summary
        scraper.print_summary(result)
        
        # Save to files
        json_file = scraper.save_to_json(result)
        csv_file = scraper.save_to_csv(result)
        
        print(f"\n✅ Scraping completed successfully!")
        print(f"📁 Files saved:")
        print(f"   - JSON: {json_file}")
        print(f"   - CSV: {csv_file}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
