# Instagram Keyword Scraper - Apify Web UI Guide

This guide shows you how to use Apify's web interface to scrape Instagram keyword searches without writing any code.

## Quick Start

### 1. Access the Instagram Search Scraper

1. Go to [Apify.com](https://apify.com) and sign up for a free account
2. Navigate to the [Instagram Search Scraper](https://apify.com/apify/instagram-search-scraper)
3. Click **"Try for free"** or **"Start"**

### 2. Configure Your Search

In the **Input** section, configure your search parameters:

#### Basic Configuration
```json
{
  "search": "koh phangan best coffee",
  "searchType": "place",
  "searchLimit": 10,
  "resultsType": "posts",
  "resultsLimit": 100
}
```

#### Parameter Explanations

| Parameter | Description | Options | Example |
|-----------|-------------|---------|---------|
| `search` | Your keyword search term | Any string | "koh phangan best coffee" |
| `searchType` | Type of search to perform | "place", "profile", "hashtag" | "place" |
| `searchLimit` | Number of search results to process | 1-50 | 10 |
| `resultsType` | Type of results to fetch | "posts", "profiles" | "posts" |
| `resultsLimit` | Max results per search result | 1-1000 | 100 |

### 3. Advanced Configuration (Optional)

#### For Better Reliability - Use Proxies
```json
{
  "search": "koh phangan best coffee",
  "searchType": "place",
  "searchLimit": 10,
  "resultsType": "posts",
  "resultsLimit": 100,
  "proxy": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

#### For Different Search Types

**Search for Places:**
```json
{
  "search": "koh phangan best coffee",
  "searchType": "place",
  "resultsType": "posts"
}
```

**Search for Profiles:**
```json
{
  "search": "travel blogger",
  "searchType": "profile",
  "resultsType": "profiles"
}
```

**Search for Hashtags:**
```json
{
  "search": "thai food",
  "searchType": "hashtag",
  "resultsType": "posts"
}
```

### 4. Run the Scraper

1. Click **"Save & Start"** to begin scraping
2. Monitor the progress in the **Run** tab
3. Wait for the status to show **"SUCCEEDED"**

### 5. Download Your Data

Once completed:

1. Go to the **Dataset** tab
2. Click **"Preview"** to see your data
3. Click **"Download"** and choose your format:
   - **JSON** - For programmatic use
   - **CSV** - For spreadsheet applications
   - **Excel** - For Microsoft Excel
   - **HTML** - For web viewing

## Common Use Cases

### 1. Coffee Shops in Koh Phangan
```json
{
  "search": "koh phangan best coffee",
  "searchType": "place",
  "searchLimit": 5,
  "resultsType": "posts",
  "resultsLimit": 20
}
```

### 2. Travel Influencers
```json
{
  "search": "travel blogger",
  "searchType": "profile",
  "searchLimit": 10,
  "resultsType": "profiles",
  "resultsLimit": 50
}
```

### 3. Food Hashtags
```json
{
  "search": "thai street food",
  "searchType": "hashtag",
  "searchLimit": 3,
  "resultsType": "posts",
  "resultsLimit": 50
}
```

### 4. Restaurant Reviews
```json
{
  "search": "bangkok restaurants",
  "searchType": "place",
  "searchLimit": 8,
  "resultsType": "posts",
  "resultsLimit": 30
}
```

## Understanding the Results

### Data Structure
Each result contains information like:
- **Post ID and short code**
- **Caption text**
- **Owner username**
- **Image/video URLs**
- **Likes and comments count**
- **Timestamp**
- **Location information** (if available)
- **Hashtags used**

### Sample Result
```json
{
  "id": "1234567890",
  "shortCode": "ABC123",
  "caption": "Amazing coffee in Koh Phangan! ☕️ #kohphangan #coffee #thailand",
  "ownerUsername": "coffee_lover",
  "displayUrl": "https://instagram.com/p/ABC123/media/",
  "timestamp": "2024-01-15T08:00:00.000Z",
  "likesCount": 150,
  "commentsCount": 12,
  "location": {
    "name": "Coffee Shop Name",
    "slug": "coffee-shop-name"
  }
}
```

## Tips for Better Results

### 1. Choose the Right Search Type
- **"place"** - Best for location-based searches (restaurants, shops, attractions)
- **"profile"** - Best for finding specific types of users (influencers, businesses)
- **"hashtag"** - Best for content discovery around specific topics

### 2. Optimize Your Keywords
- Use specific, descriptive terms
- Include location names for local searches
- Try variations of your keywords

### 3. Adjust Limits Based on Your Needs
- **Small searches** (10-50 results): `searchLimit: 3-5`, `resultsLimit: 10-20`
- **Medium searches** (50-200 results): `searchLimit: 5-10`, `resultsLimit: 20-50`
- **Large searches** (200+ results): `searchLimit: 10-20`, `resultsLimit: 50-100`

### 4. Use Proxies for Reliability
- Enable residential proxies for better success rates
- Especially important for large-scale scraping

## Troubleshooting

### Common Issues

**"No results found"**
- Try different search types (place vs profile vs hashtag)
- Use more specific or broader keywords
- Increase `searchLimit`

**"Scraper failed"**
- Check your internet connection
- Try using residential proxies
- Reduce `searchLimit` and `resultsLimit`

**"Rate limited"**
- Add delays between runs
- Use residential proxies
- Reduce scraping volume

### Getting Help
- Check the [Apify documentation](https://docs.apify.com/)
- Visit the [Instagram Search Scraper page](https://apify.com/apify/instagram-search-scraper)
- Contact Apify support for technical issues

## Legal and Ethical Considerations

⚠️ **Important**: 
- Only scrape publicly available data
- Respect Instagram's Terms of Service
- Follow applicable data protection laws
- Use data responsibly and ethically
- Don't overload Instagram's servers

## Cost Information

- **Free tier**: Limited runs per month
- **Paid plans**: More runs and better proxy access
- **Pay-per-use**: Pay only for what you use
- Check [Apify pricing](https://apify.com/pricing) for current rates

## Next Steps

1. **Start with a simple search** to test the tool
2. **Experiment with different parameters** to find what works best
3. **Use the data** for your research, analysis, or business needs
4. **Consider automation** if you need regular scraping (using the Python script)

---

**Ready to start?** Go to [Instagram Search Scraper on Apify](https://apify.com/apify/instagram-search-scraper) and try your first search!
