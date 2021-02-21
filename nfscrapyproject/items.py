# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NfscrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DenimItem(scrapy.Item):
    url = scrapy.Field()
    cut = scrapy.Field()
    weight = scrapy.Field()
    brand = scrapy.Field()
    name = scrapy.Field()
    retail_price = scrapy.Field()
    sale_price = scrapy.Field()
    description_paragraph = scrapy.Field()
    description_bullet = scrapy.Field()
    picture_urls = scrapy.Field()
    tag_size = scrapy.Field()
    pre_waist_inch = scrapy.Field()
    pre_front_rise_inch = scrapy.Field()
    pre_back_rise_inch = scrapy.Field()
    pre_upper_thigh_inch = scrapy.Field()
    pre_knee_inch = scrapy.Field()
    pre_leg_opening_inch = scrapy.Field()
    pre_inseam_inch = scrapy.Field()
    post_waist_inch = scrapy.Field()
    post_front_rise_inch = scrapy.Field()
    post_back_rise_inch = scrapy.Field()
    post_upper_thigh_inch = scrapy.Field()
    post_knee_inch = scrapy.Field()
    post_leg_opening_inch = scrapy.Field()
    post_inseam_inch = scrapy.Field()
    date_scrape = scrapy.Field()
    user_enter = scrapy.Field()

class DenimSizeItem(scrapy.Item):
    denim_name = scrapy.Field()
    brand = scrapy.Field()
    cut = scrapy.Field()
    wash = scrapy.Field()
    tag_size = scrapy.Field()
    pre_waist_inch = scrapy.Field()
    pre_front_rise_inch = scrapy.Field()
    pre_back_rise_inch = scrapy.Field()
    pre_upper_thigh_inch = scrapy.Field()
    pre_knee_inch = scrapy.Field()
    pre_leg_opening_inch = scrapy.Field()
    pre_inseam_inch = scrapy.Field()
    post_waist_inch = scrapy.Field()
    post_front_rise_inch = scrapy.Field()
    post_back_rise_inch = scrapy.Field()
    post_upper_thigh_inch = scrapy.Field()
    post_knee_inch = scrapy.Field()
    post_leg_opening_inch = scrapy.Field()
    post_inseam_inch = scrapy.Field()
    date_scrape = scrapy.Field()
    user_enter = scrapy.Field()
    url = scrapy.Field()

class DenimSalePrice(scrapy.Item):
    denim_name = scrapy.Field()
    brand = scrapy.Field()
    cut = scrapy.Field()
    retail_price = scrapy.Field()
    sale_price = scrapy.Field()
    date_scrape = scrapy.Field()
    user_enter = scrapy.Field()
    url = scrapy.Field()
