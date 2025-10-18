# Instagram Keyword Scraper with Apify

A Python application that scrapes Instagram posts based on keyword searches using Apify's [Instagram Search Scraper](https://apify.com/apify/instagram-search-scraper). This tool allows you to discover and extract posts from Instagram's keyword search feature (explore/search/keyword).

## Features

- 🔍 **Keyword Search**: Search Instagram using specific keywords (e.g., "koh phangan best coffee")
- 📊 **Multiple Search Types**: Support for place, profile, and hashtag searches
- 📁 **Multiple Export Formats**: Save results as JSON or CSV
- ⚙️ **Configurable**: Customize search limits and result types
- 🔒 **Secure**: Uses environment variables for API token management
- 📈 **Detailed Reporting**: Comprehensive summary of scraped data

## Prerequisites

- Python 3.7 or higher
- Apify account (free tier available at [apify.com](https://apify.com))
- Apify API token

## Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd lost-scarping
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit .env and add your Apify API token
   nano .env
   ```

4. **Get your Apify API token**
   - Sign up at [apify.com](https://apify.com) (free tier available)
   - Go to [Integrations > API tokens](https://console.apify.com/account/integrations)
   - Copy your API token and paste it in the `.env` file

## Usage

### Basic Usage

```python
from instagram_scraper import InstagramKeywordScraper

# Initialize the scraper
scraper = InstagramKeywordScraper()

# Scrape posts for a keyword
result = scraper.scrape_keyword("koh phangan best coffee")

# Save results
scraper.save_to_json(result)
scraper.save_to_csv(result)
```

### Advanced Configuration

```python
# Custom search configuration
search_config = {
    "search_type": "place",      # "place", "profile", or "hashtag"
    "search_limit": 10,          # Number of search results to process
    "results_type": "posts",     # "posts" or "profiles"
    "results_limit": 50          # Max results per search result
}

# Optional: Use residential proxies for better reliability
proxy_config = {
    "proxy": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}

# Scrape with custom configuration
result = scraper.scrape_keyword(
    "koh phangan best coffee",
    **search_config,
    proxy_config=proxy_config
)
```

### Command Line Usage

Run the script directly to scrape "koh phangan best coffee":

```bash
python instagram_scraper.py
```

## Configuration Options

### Search Types

- **`place`**: Search for places related to the keyword (recommended for location-based searches)
- **`profile`**: Search for user profiles related to the keyword
- **`hashtag`**: Search for hashtags related to the keyword

### Search Parameters

| Parameter | Description | Default | Options |
|-----------|-------------|---------|---------|
| `search` | The keyword to search for | Required | Any string |
| `search_type` | Type of search to perform | "place" | "place", "profile", "hashtag" |
| `search_limit` | Number of search results to process | 10 | 1-50 |
| `results_type` | Type of results to fetch | "posts" | "posts", "profiles" |
| `results_limit` | Max results per search result | 100 | 1-1000 |

### Proxy Configuration

For better reliability and to avoid rate limiting, you can use residential proxies:

```python
proxy_config = {
    "proxy": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}
```

## Output Format

### JSON Output

The scraper saves data in the following JSON structure:

```json
{
  "metadata": {
    "keyword": "koh phangan best coffee",
    "search_type": "place",
    "results_type": "posts",
    "total_items": 45,
    "scraped_at": "2024-01-15T10:30:00",
    "apify_run_id": "abc123..."
  },
  "data": [
    {
      "id": "post_id_123",
      "shortCode": "ABC123",
      "caption": "Amazing coffee in Koh Phangan...",
      "ownerUsername": "coffee_lover",
      "displayUrl": "https://...",
      "timestamp": "2024-01-15T08:00:00",
      "likesCount": 150,
      "commentsCount": 12,
      // ... more fields
    }
  ]
}
```

### CSV Output

The CSV file contains flattened data from all posts, making it easy to analyze in spreadsheet applications.

## File Structure

```
lost-scarping/
├── instagram_scraper.py    # Main scraper implementation
├── requirements.txt        # Python dependencies
├── env.example            # Environment variables template
├── .gitignore            # Git ignore file
├── README.md             # This documentation
├── DEPLOY_ACTOR.md       # Guide for deploying as Apify actor
├── apify_web_ui_guide.md # Guide for using Apify web UI
├── examples.py           # Usage examples
├── setup.py              # Setup script
├── actor/                # Apify actor files
│   ├── main.js           # Actor main code
│   ├── package.json      # Node.js dependencies
│   ├── input.json        # Example input
│   ├── README.md         # Actor documentation
│   └── .gitignore        # Actor gitignore
└── output/               # Generated output files
    ├── instagram_*.json  # JSON export files
    └── instagram_*.csv   # CSV export files
```

## Examples

### Example 1: Coffee Shops in Koh Phangan

```python
scraper = InstagramKeywordScraper()
result = scraper.scrape_keyword(
    "koh phangan best coffee",
    search_type="place",
    search_limit=5,
    results_limit=20
)
```

### Example 2: Travel Influencers

```python
result = scraper.scrape_keyword(
    "travel blogger",
    search_type="profile",
    search_limit=10,
    results_type="profiles"
)
```

### Example 3: Food Hashtags

```python
result = scraper.scrape_keyword(
    "thai food",
    search_type="hashtag",
    search_limit=3,
    results_limit=50
)
```

## Legal and Ethical Considerations

⚠️ **Important**: This tool is designed to scrape publicly available data from Instagram. Please ensure your usage complies with:

- Instagram's Terms of Service
- Applicable data protection regulations (GDPR, CCPA, etc.)
- Local laws regarding web scraping
- Respect for user privacy

The scraper only accesses publicly available information and does not require Instagram login credentials.

## Troubleshooting

### Common Issues

1. **"Apify API token is required"**
   - Make sure you've created a `.env` file with your API token
   - Verify the token is correct in your Apify console

2. **"Scraper run failed"**
   - Check your internet connection
   - Verify your Apify account has sufficient credits
   - Try using residential proxies for better reliability

3. **"No data to save"**
   - The keyword might not have returned any results
   - Try different search types (place vs profile vs hashtag)
   - Increase search_limit or results_limit

4. **Rate limiting**
   - Add delays between requests
   - Use residential proxies
   - Reduce search_limit and results_limit

### Getting Help

- Check the [Apify Instagram Search Scraper documentation](https://apify.com/apify/instagram-search-scraper)
- Review [Apify's Python client documentation](https://docs.apify.com/platform/sdks/python)
- Contact Apify support for API-related issues

## License

This project is for educational and research purposes. Please use responsibly and in compliance with Instagram's Terms of Service and applicable laws.

## Deployment Options

### Option 1: Python Script (Local)
Use the Python script for local development and one-off scraping:
```bash
python instagram_scraper.py
```

### Option 2: Apify Web UI (No Code)
Use Apify's web interface directly:
- Go to [Instagram Search Scraper](https://apify.com/apify/instagram-search-scraper)
- Configure and run in the browser
- See [apify_web_ui_guide.md](apify_web_ui_guide.md) for details

### Option 3: Custom Apify Actor (Recommended)
Deploy as your own reusable actor:
```bash
cd actor
apify push
```
- See [DEPLOY_ACTOR.md](DEPLOY_ACTOR.md) for complete deployment guide
- Create your own actor with enhanced features
- Schedule runs and share with others

## Contributing

Feel free to submit issues and enhancement requests!
