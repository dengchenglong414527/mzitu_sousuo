from scrapy import cmdline

# 两种方法  二选一即可
cmdline.execute(['scrapy','crawl','wg'])
#cmdline.execute('scrapy crawl dugu'.split(' '))