# Instagram Keyword Scraper Actor

A custom Apify actor that scrapes Instagram posts based on keyword searches using Apify's Instagram Search Scraper.

## Features

- 🔍 **Keyword Search**: Search Instagram using specific keywords
- 📊 **Multiple Search Types**: Support for place, profile, and hashtag searches
- 🔄 **Enhanced Data**: Adds metadata to scraped results
- 📈 **Summary Reports**: Provides detailed summary of scraping results
- ⚙️ **Configurable**: Customize search limits and result types
- 🔒 **Error Handling**: Comprehensive error reporting and logging

## Input Schema

```json
{
  "search": "koh phangan best coffee",     // Required: Search keyword
  "searchType": "place",                   // Optional: "place", "profile", "hashtag" (default: "place")
  "searchLimit": 10,                       // Optional: Number of search results to process (default: 10)
  "resultsType": "posts",                  // Optional: "posts" or "profiles" (default: "posts")
  "resultsLimit": 100,                     // Optional: Max results per search result (default: 100)
  "proxy": {                               // Optional: Proxy configuration
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

## Output

### Dataset Items
Each item in the dataset contains the original Instagram data plus enhanced metadata:

```json
{
  "id": "post_id_123",
  "shortCode": "ABC123",
  "caption": "Amazing coffee in Koh Phangan! ☕️",
  "ownerUsername": "coffee_lover",
  "displayUrl": "https://instagram.com/p/ABC123/media/",
  "timestamp": "2024-01-15T08:00:00.000Z",
  "likesCount": 150,
  "commentsCount": 12,
  "_metadata": {
    "searchKeyword": "koh phangan best coffee",
    "searchType": "place",
    "resultsType": "posts",
    "itemIndex": 0,
    "scrapedAt": "2024-01-15T10:30:00.000Z",
    "originalActor": "apify/instagram-search-scraper"
  }
}
```

### Summary (Key-Value Store)
The actor saves a summary in the key-value store:

```json
{
  "searchKeyword": "koh phangan best coffee",
  "searchType": "place",
  "resultsType": "posts",
  "searchLimit": 10,
  "resultsLimit": 100,
  "totalItems": 45,
  "scrapedAt": "2024-01-15T10:30:00.000Z",
  "originalRunId": "abc123...",
  "status": "SUCCEEDED"
}
```

## Usage Examples

### Basic Place Search
```json
{
  "search": "koh phangan best coffee",
  "searchType": "place",
  "resultsType": "posts"
}
```

### Profile Search
```json
{
  "search": "travel blogger",
  "searchType": "profile",
  "resultsType": "profiles",
  "searchLimit": 5,
  "resultsLimit": 20
}
```

### Hashtag Search with Proxies
```json
{
  "search": "thai food",
  "searchType": "hashtag",
  "resultsType": "posts",
  "searchLimit": 3,
  "resultsLimit": 50,
  "proxy": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

## Building and Deploying

### 1. Prepare the Actor
```bash
cd actor
npm install
```

### 2. Test Locally
```bash
# Set your input in input.json
echo '{"search": "koh phangan best coffee"}' > input.json

# Run locally
apify run
```

### 3. Deploy to Apify
```bash
# Login to Apify
apify login

# Deploy the actor
apify push
```

### 4. Use in Apify Console
1. Go to your actor in the Apify console
2. Configure input parameters
3. Click "Start" to run
4. Download results from the dataset

## Configuration Options

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `search` | string | Yes | - | The keyword to search for |
| `searchType` | string | No | "place" | Type of search: "place", "profile", "hashtag" |
| `searchLimit` | number | No | 10 | Number of search results to process (1-50) |
| `resultsType` | string | No | "posts" | Type of results: "posts", "profiles" |
| `resultsLimit` | number | No | 100 | Max results per search result (1-1000) |
| `proxy` | object | No | {} | Proxy configuration for better reliability |

## Error Handling

The actor includes comprehensive error handling:

- **Input validation**: Checks for required parameters
- **Scraper monitoring**: Monitors the Instagram scraper status
- **Error reporting**: Saves error details to key-value store
- **Logging**: Detailed logs for debugging

## Legal and Ethical Considerations

⚠️ **Important**: This actor is designed to scrape publicly available data from Instagram. Please ensure your usage complies with:

- Instagram's Terms of Service
- Applicable data protection regulations
- Local laws regarding web scraping
- Respect for user privacy

## Dependencies

- `apify`: Apify SDK for actor development
- `apify/instagram-search-scraper`: The underlying Instagram scraper

## Support

For issues or questions:
- Check the [Apify documentation](https://docs.apify.com/)
- Review the [Instagram Search Scraper](https://apify.com/apify/instagram-search-scraper) documentation
- Contact Apify support for technical issues
