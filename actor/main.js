const Apify = require('apify');
const { log } = Apify.utils;

Apify.main(async () => {
    const input = await Apify.getInput();
    const { 
        search, 
        searchType = 'place', 
        searchLimit = 10, 
        resultsType = 'posts', 
        resultsLimit = 100,
        proxy = {}
    } = input;

    // Validate required input
    if (!search) {
        throw new Error('Search keyword is required');
    }

    log.info(`Starting Instagram keyword search for: "${search}"`);
    log.info(`Search type: ${searchType}, Results type: ${resultsType}`);
    log.info(`Limits: search=${searchLimit}, results=${resultsLimit}`);

    // Prepare input for Instagram Search Scraper
    const instagramScraperInput = {
        search,
        searchType,
        searchLimit,
        resultsType,
        resultsLimit,
        ...proxy
    };

    try {
        // Call the Instagram Search Scraper actor
        const instagramScraper = await Apify.newClient();
        const run = await instagramScraper.actor('apify/instagram-search-scraper').call(instagramScraperInput);

        if (run.status !== 'SUCCEEDED') {
            throw new Error(`Instagram scraper failed with status: ${run.status}`);
        }

        log.info('Instagram scraper completed successfully!');

        // Get the dataset items
        const dataset = await instagramScraper.dataset(run.defaultDatasetId).listItems();
        
        log.info(`Retrieved ${dataset.items.length} items`);

        // Process and enhance the data
        const processedItems = dataset.items.map((item, index) => ({
            ...item,
            _metadata: {
                searchKeyword: search,
                searchType,
                resultsType,
                itemIndex: index,
                scrapedAt: new Date().toISOString(),
                originalActor: 'apify/instagram-search-scraper'
            }
        }));

        // Save results to dataset
        await Apify.pushData(processedItems);

        // Save summary metadata
        const summary = {
            searchKeyword: search,
            searchType,
            resultsType,
            searchLimit,
            resultsLimit,
            totalItems: processedItems.length,
            scrapedAt: new Date().toISOString(),
            originalRunId: run.id,
            status: 'SUCCEEDED'
        };

        await Apify.setValue('SUMMARY', summary);
        
        log.info('✅ Instagram keyword scraping completed successfully!');
        log.info(`📊 Total items scraped: ${processedItems.length}`);

    } catch (error) {
        log.error('❌ Error during Instagram keyword scraping:', error);
        
        // Save error information
        await Apify.setValue('ERROR', {
            message: error.message,
            searchKeyword: search,
            searchType,
            resultsType,
            errorAt: new Date().toISOString(),
            status: 'FAILED'
        });
        
        throw error;
    }
});
