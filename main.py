#!/usr/bin/env python

import argparse
import urlparse
import whois
import requests
import time
import dns.resolver


class URLObject(object):
	def __init__(self, url):
		raw_url = url
		self.subdomain = url.split('/')[2]
		raw_url = urlparse.urlparse(self.subdomain).netloc.split(".")
		self.domain = raw_url[-2] + '.' + raw_url[-1]
		
	def get_domain(self):
		return self.domain 

	def get_subdomain(self):
		return self.subdomain 	

	def whois_info(self):
		self.whois_info = whois.whois(self.domain)
		return self.whois_info

	def dns_info(self):
		self.ip = dns.resolver.query(self.subdomain)[0]
		return self.ip
		
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file", type=str, help="File containing URLs")

	args = parser.parse_args()

	filename = args.file
	url_file = open(filename) 

	for line in url_file.readlines():
		raw_url = line.strip('\n\r')
		url = URLObject(raw_url)
		print url.get_domain() + " : " + str(url.dns_info())
		#whois = Whois(raw_url)

if __name__ == '__main__':
	main()