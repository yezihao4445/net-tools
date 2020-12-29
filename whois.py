'''
需要开放端口 53 DNS 、 43 Whois 、80 HTTP RDAP NIR 
'''
from ipwhois import IPWhois
from pprint import pprint
import crypt


class Whois():
    def __init__(self):
        self.key = crypt.mksalt(crypt.METHOD_SHA512)

    def find(self,ip):
        obj = IPWhois(ip)
        whois_results = obj.lookup_rdap(depth=1)
        whois_hash = crypt.crypt(str(whois_results),self.key)

        return whois_results,whois_hash

if __name__ == "__main__":
    whois_results,whois_hash = Whois().find("220.181.38.148")
    pprint(whois_results)