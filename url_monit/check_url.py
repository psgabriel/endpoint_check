import requests

class UrlRequest():
    
    def __init__(self, address):
        self.address = address
        
    def check(self):
        r = requests.head(self.address)
        return r.status_code