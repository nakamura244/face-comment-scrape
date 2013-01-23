# Scrapy settings for ameblo_face project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ameblo_face_bot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['ameblo_face.spiders']
NEWSPIDER_MODULE = 'ameblo_face.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ameblo_face (+http://www.yourdomain.com)'

USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'


COOKIES_ENABLED = False
#CLOSESPIDER_ITEMCOUNT = 1
#This setting is also affected by the RANDOMIZE_DOWNLOAD_DELAY setting (which is enabled by default). By default, 
#Scrapy doesnt wait a fixed amount of time between requests, but uses a random interval between 0.5 and 1.5 * DOWNLOAD_DELAY.
DOWNLOAD_DELAY = 0.25    # 250 ms of delay



