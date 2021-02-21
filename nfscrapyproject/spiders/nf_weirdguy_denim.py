import scrapy
import re
import pytz
import logging
import pandas as pd
from scrapy_splash import SplashRequest
from datetime import datetime
from nfscrapyproject.items import DenimItem


class NfWeirdguyDenimSpider(scrapy.Spider):
    name = 'weirdguy_denim'
    allowed_domains = ['www.tateandyoko.com']
    start_urls = [
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=1',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=2',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=3',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=4',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=5',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=6',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=7',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=8',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=9',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=10',
            'http://www.tateandyoko.com/collections/naked-and-famous-weird-guy?page=11',
    ]

    def parse(self, response):
        urls = response.xpath('//h2[@class="product-item__title"]/a/@href').extract()
        for url in urls:
            yield SplashRequest(response.urljoin(url), callback=self.parse_jean_product_pages, args={'wait': 5})
            #yield response.follow(url, callback=self.parse_jean_product_pages)
    
    def parse_jean_product_pages(self, response):
        item = DenimItem()
        item['url'] = response.url
        item['brand'] = response.xpath('//h2[@class="product-meta__vendor"]/text()').extract()[0].replace('\xa0', ' ')
        title = response.xpath('//h1[@class="product-meta__title"]/text()').extract()[0]
        title = title.split('-',1)
        #item['cut'] = title[0].strip().replace('\xa0', ' ')
        item['cut'] = "Weird Guy" 
        item['name'] = title[1].strip().replace('\xa0', ' ')

        sale_price = response.xpath('//span[@class="product-meta__price product-meta__price--new"]').extract()
        if not sale_price:
            retail_price = response.xpath('//span[@class="product-meta__price"]/text()').extract()
            if retail_price:
                item['retail_price'] = retail_price[0].split(' ',1)[0].replace('$','').replace('\xa0', ' ')
        else:
            item['sale_price'] = response.xpath('//span[@class="product-meta__price product-meta__price--new"]/text()').extract()[0].split(' ',1)[0].replace('$','').replace('\xa0', ' ')
            item['retail_price'] = response.xpath('//span[@class="product-meta__price product-meta__price--old"]/text()').extract()[0].split(' ',1)[0].replace('$','').replace('\xa0', ' ')
        desc_paragraphs = response.xpath('//div[@class="product__description rte"]//*/text()').extract()
        desc_paragraphs = ' '.join(desc_paragraphs)
        item['description_paragraph'] = desc_paragraphs.replace('\xa0', ' ')
        #item['description_paragraph'] = response.xpath('//div[@class="product__description rte"]/p/text()').extract()[0].replace('\xa0', ' ')
        denim_description_bullet_pt = response.xpath('//div[@class="product__description rte"]/ul/li/text()').extract()
        if '\n' in denim_description_bullet_pt: 
            denim_description_bullet_pt.remove('\n')
        item['description_bullet'] = [w.replace('\xa0', ' ') for w in denim_description_bullet_pt]
        item['weight'] = [] 
        if item['description_bullet'] != []:
            m = re.search(r"([-+]?\d*\.?\d+)oz", item['description_bullet'][0])
            if m:
                item['weight'] = m.group(1)
        if item['description_paragraph'] and not item['weight']:
            m = re.search(r"([-+]?\d*\.?\d+)oz", item['description_paragraph'])
            if m:
                item['weight'] = m.group(1)
        
        item['picture_urls'] = response.xpath('//div[@class="product__thumbnails"]/a/@href').extract()
        item['date_scrape'] = datetime.now(pytz.utc) 
        item['user_enter'] = 'NFDenimBot'
        tables = response.xpath('//table[@class="ks-table"]')
        #table = tables[0]
        #rows = table.xpath('//tr[position()>1]')
        #check = rows.xpath('(//tr)[1]').extract()
        #print(check)

        num_size_table = len(response.xpath('//table[@class="ks-table"]'))
        i = 1
        for table in response.xpath('//table[@class="ks-table"]'):
            header = table.xpath('//tr/td[position()=1]/text()').extract()
            item['tag_size'] = table.xpath('//tr[position()=1]/td[position()>1]/text()').extract()
            rows = table.xpath('//tr[position()>1]')
            waist_size_inch = rows[0].xpath('./td[@class="ks-table-cell"]/text()').extract()
            front_rise_inch = rows[1].xpath('./td[@class="ks-table-cell"]/text()').extract()
            back_rise_inch = rows[2].xpath('./td[@class="ks-table-cell"]/text()').extract()
            upper_thigh_inch = rows[3].xpath('./td[@class="ks-table-cell"]/text()').extract()
            knee_inch = rows[4].xpath('./td[@class="ks-table-cell"]/text()').extract()
            leg_opening_inch = rows[5].xpath('./td[@class="ks-table-cell"]/text()').extract()
            #logging.debug("DEBUG FUCK FUCK")
            #print(front_rise_inch)
            if num_size_table == 2 and i == 1 :
                item['pre_waist_inch'] = [w.replace('\n', '').replace(' ', '') for w in waist_size_inch]
                item['pre_front_rise_inch'] = [w.replace('\n', '').replace(' ', '') for w in front_rise_inch]
                item['pre_back_rise_inch'] = [w.replace('\n', '').replace(' ', '') for w in back_rise_inch]
                item['pre_upper_thigh_inch'] = [w.replace('\n', '').replace(' ', '') for w in upper_thigh_inch]
                item['pre_knee_inch'] = [w.replace('\n', '').replace(' ', '') for w in knee_inch]
                item['pre_leg_opening_inch'] = [w.replace('\n', '').replace(' ', '') for w in leg_opening_inch]
            if num_size_table == 2 and i == 2 :
                item['post_waist_inch'] = [w.replace('\n', '').replace(' ', '') for w in waist_size_inch]
                item['post_front_rise_inch'] = [w.replace('\n', '').replace(' ', '') for w in front_rise_inch]
                item['post_back_rise_inch'] = [w.replace('\n', '').replace(' ', '') for w in back_rise_inch]
                item['post_upper_thigh_inch'] = [w.replace('\n', '').replace(' ', '') for w in upper_thigh_inch]
                item['post_knee_inch'] = [w.replace('\n', '').replace(' ', '') for w in knee_inch]
                item['post_leg_opening_inch'] = [w.replace('\n', '').replace(' ', '') for w in leg_opening_inch]
            if num_size_table == 1:
                item['post_waist_inch'] = [w.replace('\n', '').replace(' ', '') for w in waist_size_inch]
                item['post_front_rise_inch'] = [w.replace('\n', '').replace(' ', '') for w in front_rise_inch]
                item['post_back_rise_inch'] = [w.replace('\n', '').replace(' ', '') for w in back_rise_inch]
                item['post_upper_thigh_inch'] = [w.replace('\n', '').replace(' ', '') for w in upper_thigh_inch]
                item['post_knee_inch'] = [w.replace('\n', '').replace(' ', '') for w in knee_inch]
                item['post_leg_opening_inch'] = [w.replace('\n', '').replace(' ', '') for w in leg_opening_inch]
            i = i + 1
            #check = data.xpath('//td/text()')
            #data = [row for row in data if len(row)==len(header)]
            #data = pd.DataFrame(data, columns=header)
        yield item
