#!-*- coding:utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy import log
from ameblo_face.service import *
from ameblo_face.db_model import *
import re
import urllib
#from ameblo_face.items import AmebloFaceItem


class DcmxEcSiteSpider(BaseSpider):
    name = "ameblo_face"
    allowed_domains = ["face.ameba.jp"]
    start_urls = [
                    "http://face.ameba.jp/"
                 ]



    def _download (self,img_url,filename):
        img = urllib.urlopen(img_url)
        localfile = open(filename, 'wb')
        localfile.write(img.read())
        img.close()
        localfile.close()
        return;

    def parse (self, response):
        response._encoding = "utf-8"
        hxs = HtmlXPathSelector(response)
        service = Service()
        lists = dict()
        for elem in hxs.select('//div[@id="main"]'):
            lists['name'] = elem.select('dl[@class="clr"]/dd[@class="name"]/p/text()').extract()[0]
            profile_img_url = elem.select('dl[@class="clr"]/dt/img/@src').extract()[0]
            profile_img_file = re.sub(r'http://stat.ameba.jp/blog/img/ameba/officialblog/face/', '', profile_img_url)
            self._download(profile_img_url,"/home/face-comment/face_comment_web/public/common/img/profile_photo/"+profile_img_file)
            lists['profile_img_file'] = profile_img_file
            img_url = elem.select('ul[@id="imgNavWrap"]/li[@id="blogImgWrap"]/p[@class="blogImg"]/img/@src').extract()[0]
            img_alt = elem.select('ul[@id="imgNavWrap"]/li[@id="blogImgWrap"]/p[@class="blogImg"]/img/@alt').extract()[0]
            img_link = elem.select('ul[@id="imgNavWrap"]/li[@id="blogImgWrap"]/p[@class="blogImg"]/span/a/@href').extract()[0]
            img_file = re.sub(r'http://stat.ameba.jp/user_images/', '', img_url)
            save_filename = re.sub(r'/', '_', img_file)
            lists['datetime'] = img_file[:8]
            self._download(img_url,"/home/face-comment/face_comment_web/public/common/img/photo/"+save_filename)
            lists['img_file']          = save_filename
            lists['img_name']          = img_alt
            lists['blog_entry_url']   = img_link
            lists['sex']               = 3
            lists['photo_other']       = ""
            lists['talent_other']      = ""
            lists['comment_count']     = 0

            ## タレントマスターの作成
            # 処理1：タレント名でTalent Tableを検索
            # 処理2：無ければinsert
            # 処理3：タレントIDをlistsにセット
            talent = service.get_talent_id(lists['name'])
            if not talent:
                insert = Talent(lists)
                session.add(insert)
                session.commit()
                talent = service.get_talent_id(lists['name'])
                lists['talent_id'] = talent.id
            else:
                lists['talent_id'] = talent.id

            ## 写真テーブルにデータをinsert　※新規の写真のみをinsert(updateはしない)
            ##   常に新しい順にデータがアップされているので
            ##   一度既存のデータが存在した場合は以降は既に取得済みのデータとして定義
            # 処理1：画像のファイル名でphoto Table を検索
            # 処理2：無ければinsert
            # 処理3：有れば以降にスクレイピングするデータは既存データとなるのでbreakして終了
            if not service.get_photo_id(lists['img_file']):
                insert = Photo(lists)
                session.add(insert)
                session.commit()
            else:
                break


            next_url = elem.select('ul[@id="imgNavWrap"]/li[@id="next"]/a/@href').extract()[0]
            request = Request('http://face.ameba.jp'+next_url, self.parse)
            yield request
 

