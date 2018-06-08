import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class MyFileApkPipeline(FilesPipeline):


    def file_path(self, request, response=None, info=None):
        apk_guid = request.url.split('/')[-1].split('?')[0]
        print(apk_guid)
        return 'full/%s' % (apk_guid)

    def get_media_requests(self, item, info):
        for file_urls in item['file_urls']:
            print("yaphetshan")
            yield scrapy.Request(file_urls)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no apk")
        print("123"+"file_paths")
        item['file_urls'] = file_paths
        return item

