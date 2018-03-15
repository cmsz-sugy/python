import requests
import  json
def http2(url,data_pa,focus_data):
    wbdata = requests.get(url).text
    data = json.loads(wbdata)
    news = data[data_pa][focus_data]
    return news

def http1(url1,data_pa):
    wbdata = requests.get(url1).text
    data = json.loads(wbdata)
    news = data[data_pa]
    return news