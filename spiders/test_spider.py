import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
	

    def start_requests(self):
        urls = [
            'https://www.apkmonk.com/download-app/com.viber.voip/5_com.viber.voip_2018-06-03.apk/'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.apk' % page
        print(response.body)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
