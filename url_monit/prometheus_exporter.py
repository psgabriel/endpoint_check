from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY
from prometheus_client import Gauge, start_http_server

class PrometheusExporter():
    
    def __init__(self, url_data):
        self.url_data = url_data
        
    def publisher(self):
        for item in self.url_data:
            url_group = item['url_group']
            url_address = item['url_address']
            http_resp_code = item['http_resp_code']
            url_status = item['url_status']

            prometheus_metric_name = 'http_check'
            prometheus_metric_help = 'http_resp_code' + '_' + str(http_resp_code)
            g = GaugeMetricFamily(prometheus_metric_name, prometheus_metric_help, labels=[url_group])
            g.add_metric([url_address], value=url_status)
            yield g