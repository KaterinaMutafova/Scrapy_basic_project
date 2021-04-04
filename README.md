# Scrapy_basic_project

# Main Logic of scraping the page "https://www.parliament.bg/bg/MP"

# 1. Select all tags containing the basic info of each person and get 
# all the url link parts in one variable --> "all_the_links";

# 2. Go through every single url of "all_the_links" and concatenate them to the base url "https://www.parliament.bg";

# 3. Yield new request from every newly concatenated url link;

# 4. Select all the  required information from the  page;

#5. Create a dictionary with all the acquired data;

#6. Yield the data;

#7. Add a "FEED_EXPORT_ENCODING = 'utf-8'" format in the settings.py file to correct the format;

#8. Extract and save  the  obtained information in json file  with "scrapy crawl parliament -o parliament.json".







