# import the necessary packages
from timecoverspider.items import MagazineCover
import datetime
import scrapy
 
class CoverSpider(scrapy.Spider):
	name = "cover-spider"
	start_urls = ["https://www.timecoverstore.com/decade"]
	
	def parse(self, response):
		# loop over all cover link elements listed as product-item
		# then request to grab the cover data and image
		for href in response.css('div.product-item a::attr(href)').extract():
			yield response.follow(href,self.parse_covers)
			
		# extract the 'Next' link from the pagination, load it, and
		# parse it
		next = response.css('li.next-page a::attr(href)').extract_first()
		if next is not None:
			yield response.follow(next, callback=self.parse)

	def parse_covers(self, response):
		# grab the URL of the cover image
		img = response.css("div.cover a::attr(href)")
		imageURL = img.extract_first()
 
		# grab the title and publication date of the current issue
		title = response.css("div.cover a::attr(title)").extract_first()[11:]
		day_year = response.css('div.short-description-date::text').extract_first()[-8:]
		month = response.css('div.short-description-date::text').extract_first()[:-9]
	
		# parse the date
		date = "{} {}".format(month, day_year).replace(",", "")
		d = datetime.datetime.strptime(date, "%B %d %Y")
		pub = "{}-{}-{}".format(d.year, str(d.month).zfill(2), str(d.day).zfill(2))
 
		# yield the result
		yield MagazineCover(title=title, pubDate=pub, file_urls=[imageURL])
