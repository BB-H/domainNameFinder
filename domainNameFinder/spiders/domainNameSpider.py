# -*- coding: utf-8 -*-
import scrapy


class DomainnamespiderSpider(scrapy.Spider):
    
	allChars = [chr(i) for i in range(97,123)]
	allChars.extend(range(1,10))
	URL_TEMPLATE = r"http://www.xinnet.com/domain/domain_search_result_version2.jsp?prefix=%s&suffix=.com&domainSuffixType=null"
	name = "domainNameSpider"
	allowed_domains = ["xinnet.com",]
	start_urls = [
        #'http://www.xinnet.com/',
    ]
	
	def __init__(self):
		for i in self.allChars:
			char1 = str(i)
			for j in self.allChars:
				char2 = str(j)
				url =  self.URL_TEMPLATE %(char1+char2)
				self.start_urls.append(url)
				for k in self.allChars:
					char3 = str(k)
					url =  self.URL_TEMPLATE %(char1+char2+char3)
					self.start_urls.append(url)

	def parse(self, response):
		#for url in  self.start_urls:
		#	print url
		#print "Length: %s" %(len(self.start_urls))
		#print self.allChars
		pass
	
	
	
		