# TimeCovers
Hobby project to learn how to scrape images from the web, classify them, and create new images. 

Started by adapting a tutorial to scrape Time magazine covers using scrapy (https://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/).  
Then continued to examine the decadal average images using this tutorial (https://www.pyimagesearch.com/2015/10/19/analyzing-91-years-of-time-magazine-covers-for-visual-trends/).
Finally I applied a couple simple unsupervised clustering tools (k-means and gaussian mixture models) to see if similar covers clusters could be extracted and if they related to the decadal average image trends.

Scraper code here: [coverspider](/timecoverspider/timecoverspider/spiders/coverspider.py). I reccommend going through the tutorial to get this working. Also I had to modify the scraper since the website had changed.

Averaging and clustering code here: [Analyze_covers](    Analyze_covers.ipynb). 

