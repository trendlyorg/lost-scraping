# Deploy Instagram Keyword Scraper as Apify Actor

This guide shows you how to deploy the Instagram keyword scraper as a custom Apify actor.

## Prerequisites

- Apify account (free at [apify.com](https://apify.com))
- Node.js installed locally
- Apify CLI installed

## Step 1: Install Apify CLI

```bash
npm install -g @apify/cli
```

## Step 2: Login to Apify

```bash
apify login
```

Enter your Apify credentials when prompted.

## Step 3: Prepare the Actor

Navigate to the actor directory:

```bash
cd actor
npm install
```

## Step 4: Test Locally (Optional)

Test the actor locally before deploying:

```bash
# Run with default input
apify run

# Or run with custom input
echo '{"search": "bangkok restaurants", "searchType": "place"}' > input.json
apify run
```

## Step 5: Deploy to Apify

Deploy your actor to the Apify platform:

```bash
apify push
```

This will:
- Upload your actor code to Apify
- Create a new actor in your Apify console
- Make it available for use

## Step 6: Configure and Use

1. **Go to your Apify Console**
   - Visit [console.apify.com](https://console.apify.com)
   - Find your new actor in the "Actors" section

2. **Configure Input**
   - Click on your actor
   - Go to the "Input" tab
   - Enter your search parameters:
   ```json
   {
     "search": "koh phangan best coffee",
     "searchType": "place",
     "searchLimit": 10,
     "resultsType": "posts",
     "resultsLimit": 100
   }
   ```

3. **Run the Actor**
   - Click "Start" to begin scraping
   - Monitor progress in the "Run" tab
   - Wait for completion

4. **Download Results**
   - Go to the "Dataset" tab
   - Download results as JSON, CSV, or Excel
   - Check the "Key-value store" for summary information

## Step 7: Schedule Runs (Optional)

For regular scraping, you can schedule the actor:

1. Go to your actor's "Schedules" tab
2. Click "Add schedule"
3. Configure:
   - **Frequency**: How often to run (daily, weekly, etc.)
   - **Input**: Your search parameters
   - **Notifications**: Email alerts when runs complete

## Step 8: Share or Publish (Optional)

### Make Actor Public
1. Go to actor settings
2. Change visibility to "Public"
3. Add description and tags
4. Others can now find and use your actor

### Share Privately
1. Go to actor settings
2. Add collaborators by email
3. Set appropriate permissions

## Advanced Configuration

### Custom Input Schema
You can customize the input schema in the actor settings:

```json
{
  "type": "object",
  "properties": {
    "search": {
      "type": "string",
      "title": "Search Keyword",
      "description": "The keyword to search for on Instagram"
    },
    "searchType": {
      "type": "string",
      "title": "Search Type",
      "enum": ["place", "profile", "hashtag"],
      "default": "place"
    },
    "searchLimit": {
      "type": "number",
      "title": "Search Limit",
      "minimum": 1,
      "maximum": 50,
      "default": 10
    },
    "resultsType": {
      "type": "string",
      "title": "Results Type",
      "enum": ["posts", "profiles"],
      "default": "posts"
    },
    "resultsLimit": {
      "type": "number",
      "title": "Results Limit",
      "minimum": 1,
      "maximum": 1000,
      "default": 100
    }
  },
  "required": ["search"]
}
```

### Environment Variables
Set up environment variables for default configurations:

1. Go to actor settings
2. Navigate to "Environment variables"
3. Add variables like:
   - `DEFAULT_SEARCH_LIMIT`: 10
   - `DEFAULT_RESULTS_LIMIT`: 100
   - `USE_PROXY`: true

## Monitoring and Analytics

### View Run History
- Check the "Runs" tab for all execution history
- View logs, errors, and performance metrics
- Download results from completed runs

### Usage Analytics
- Monitor actor usage and costs
- Track performance over time
- Optimize based on usage patterns

## Troubleshooting

### Common Issues

**"Actor failed to start"**
- Check your code for syntax errors
- Verify all dependencies are included
- Review the logs for specific error messages

**"No results returned"**
- Verify the search keyword is valid
- Try different search types
- Check if Instagram Search Scraper is working

**"Rate limited"**
- Add delays between runs
- Use residential proxies
- Reduce search limits

### Debug Mode
Enable debug logging by adding to your input:

```json
{
  "search": "test keyword",
  "debug": true
}
```

## Cost Management

### Free Tier Limits
- Limited runs per month
- Basic proxy access
- Standard support

### Paid Plans
- More runs and storage
- Residential proxy access
- Priority support
- Advanced features

### Optimization Tips
- Use appropriate limits for your needs
- Schedule runs efficiently
- Monitor usage regularly
- Use proxies only when necessary

## Next Steps

1. **Test thoroughly** with different keywords and configurations
2. **Monitor performance** and optimize as needed
3. **Set up monitoring** and alerts for important runs
4. **Consider automation** for regular data collection
5. **Share or publish** if others might benefit

---

**Ready to deploy?** Run `apify push` in the actor directory to get started!
