import re
from re import match
from requests import head
import logging


class Validator:
    def __init__(self):
        self.req = None
        self._github_url_regex = r'^(http(s?):\/\/)?(www\.)?github\.com\/([A-Za-z0-9\-]{1,})+\/?$'
        # self._github_url_regex = re.sub(r'^(http(s?):\/\/)?(www\.)?github\.com\/([A-Za-z0-9\-]{1,})+\/?$', '', str(self._github_url_regex))
 
        
    def url_status_code(self, url):
        try:
            if not ('http' in url):
                print('&&&^%^%^%',url)
                url = 'https://' + url
            self.req = head(url, verify=False,timeout=5)
            print('@@@@@@@',self.req.status_code)
            if self.req.status_code == 200:
                # logging.info('HTTP status code : 200')
                # logging.info('Successful')
                print("@##@$#Succsecc Http Status Code ", self.req.status_code)
                return True
            return False
        except Exception:
            # logging.error('######Error at Validator.url_status_code ' , e) 
            raise Exception('Invalid status code')
            
        
    def url_validator(self, url):
        if bool(match(self._github_url_regex, url) and self.url_status_code(url)):
            logging.info('Authentication Completed Successfully')
            return True
        logging.error('Error at Validator.url_validator' ) 
        return False
       
         
        