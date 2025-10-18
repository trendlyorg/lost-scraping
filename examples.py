#!/usr/bin/env python3
"""
Example usage patterns for Instagram Keyword Scraper

This file demonstrates different ways to use the InstagramKeywordScraper
for various scraping scenarios.
"""

from instagram_scraper import InstagramKeywordScraper
import time


def example_place_search():
    """Example: Search for places related to a keyword."""
    print("🏝️ Example 1: Place Search - 'koh phangan best coffee'")
    print("-" * 50)
    
    scraper = InstagramKeywordScraper()
    
    result = scraper.scrape_keyword(
        keyword="koh phangan best coffee",
        search_type="place",
        search_limit=3,
        results_type="posts",
        results_limit=15
    )
    
    scraper.print_summary(result)
    scraper.save_to_json(result, "koh_phangan_coffee_places.json")
    scraper.save_to_csv(result, "koh_phangan_coffee_places.csv")
    
    return result


def example_profile_search():
    """Example: Search for profiles related to a keyword."""
    print("\n👤 Example 2: Profile Search - 'travel blogger'")
    print("-" * 50)
    
    scraper = InstagramKeywordScraper()
    
    result = scraper.scrape_keyword(
        keyword="travel blogger",
        search_type="profile",
        search_limit=5,
        results_type="profiles",
        results_limit=10
    )
    
    scraper.print_summary(result)
    scraper.save_to_json(result, "travel_blogger_profiles.json")
    
    return result


def example_hashtag_search():
    """Example: Search for hashtags related to a keyword."""
    print("\n#️⃣ Example 3: Hashtag Search - 'thai food'")
    print("-" * 50)
    
    scraper = InstagramKeywordScraper()
    
    result = scraper.scrape_keyword(
        keyword="thai food",
        search_type="hashtag",
        search_limit=2,
        results_type="posts",
        results_limit=25
    )
    
    scraper.print_summary(result)
    scraper.save_to_json(result, "thai_food_hashtags.json")
    scraper.save_to_csv(result, "thai_food_hashtags.csv")
    
    return result


def example_with_proxy():
    """Example: Using residential proxies for better reliability."""
    print("\n🌐 Example 4: With Residential Proxies")
    print("-" * 50)
    
    scraper = InstagramKeywordScraper()
    
    # Configure residential proxies
    proxy_config = {
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"]
        }
    }
    
    result = scraper.scrape_keyword(
        keyword="bangkok street food",
        search_type="place",
        search_limit=3,
        results_type="posts",
        results_limit=20,
        proxy_config=proxy_config
    )
    
    scraper.print_summary(result)
    scraper.save_to_json(result, "bangkok_street_food_proxy.json")
    
    return result


def example_batch_search():
    """Example: Batch search for multiple keywords."""
    print("\n📦 Example 5: Batch Search - Multiple Keywords")
    print("-" * 50)
    
    keywords = [
        "koh samui beach",
        "phuket restaurants",
        "chiang mai temples"
    ]
    
    scraper = InstagramKeywordScraper()
    all_results = []
    
    for i, keyword in enumerate(keywords, 1):
        print(f"\n🔍 Processing {i}/{len(keywords)}: {keyword}")
        
        try:
            result = scraper.scrape_keyword(
                keyword=keyword,
                search_type="place",
                search_limit=2,
                results_type="posts",
                results_limit=10
            )
            
            all_results.append(result)
            
            # Save individual results
            filename = keyword.replace(' ', '_').lower()
            scraper.save_to_json(result, f"{filename}_batch.json")
            
            # Add delay between searches to be respectful
            if i < len(keywords):
                print("⏳ Waiting 30 seconds before next search...")
                time.sleep(30)
                
        except Exception as e:
            print(f"❌ Error searching for '{keyword}': {str(e)}")
            continue
    
    print(f"\n✅ Batch search completed! Processed {len(all_results)} keywords successfully.")
    return all_results


def main():
    """Run all examples."""
    print("🚀 Instagram Keyword Scraper - Examples")
    print("=" * 60)
    
    try:
        # Run individual examples
        example_place_search()
        time.sleep(10)  # Delay between examples
        
        example_profile_search()
        time.sleep(10)
        
        example_hashtag_search()
        time.sleep(10)
        
        # Uncomment to run proxy example (requires Apify credits)
        # example_with_proxy()
        # time.sleep(10)
        
        # Uncomment to run batch example
        # example_batch_search()
        
        print("\n🎉 All examples completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
