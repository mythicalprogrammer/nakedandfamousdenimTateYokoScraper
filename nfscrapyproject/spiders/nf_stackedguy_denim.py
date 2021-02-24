import scrapy
import logging
from .basespiders.TateAndYokoBaseSpider import TateAndYokoBaseSpider

class NfEasyguyDenimSpider(TateAndYokoBaseSpider):
    name = 'stackedguy_denim'
    start_urls = [
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=1',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=2',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=3',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=4',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=5',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=6',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=7',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=8',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=9',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=10',
            'http://www.tateandyoko.com/collections/naked-and-famous-stacked-guy?page=11',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def parse(self, response):
        return super().parse_denim(response)
    
