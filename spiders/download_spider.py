import scrapy
from scrapyapk.items import ScrapyapkItem

class DonwloadSpider(scrapy.Spider):
	name="file_download"
    #allowed_domains=['matplotlib.org']
	handle_httpstatus_list = [301]
	start_urls=['https://www.apkmonk.com/download-app/com.viber.voip/5_com.viber.voip_2018-06-03.apk']
	def parse(self, response):
		href = 'http://apk.apkmonk.com/apks-3/com.viber.voip_2018-06-03.apk?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=IFVYHACUO60QSGWW9L9Z%2F20180608%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180608T115024Z&X-Amz-Expires=2400&X-Amz-SignedHeaders=host&X-Amz-Signature=816249432d2fa48950fe2300380de210c95eabfa9e0a17f3c4155e6cd05e4763'
		file = ScrapyapkItem()
		file['file_urls']=[href]
		return file