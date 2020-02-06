from check_url import UrlRequest
import json


url_file_path = 'urls.json'
http_resp_code_sucess = range(200,399)
http_resp_code_errors = range(400,599)
http_response_code_ignored_errors=[401,417]

class Main():
    
    def run(self):
        stock = []
        urls_dict = json.load(open(url_file_path, 'r'))
        for url_group in urls_dict['url_monit']:
            for url_address in urls_dict['url_monit'][url_group]:
                http_resp_code = UrlRequest(url_address).check()
                
                if http_resp_code in http_resp_code_sucess:
                    url_status = 1
                elif http_resp_code in http_resp_code_errors and http_resp_code not in http_response_code_ignored_errors:
                    url_status = 0
                
                prepare_data = {
                    "url_group": url_group,
                    "url_address": url_address,
                    "http_resp_code": http_resp_code,
                    "url_status": url_status 
                }
                
                stock.append(prepare_data)
                print(prepare_data)

if __name__ == '__main__':
    Main().run()