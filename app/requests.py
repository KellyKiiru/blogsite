import urllib.request,json
import json
from app.models import Quote

def request_quote():
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        data = url.read()
        get_json = json.loads(data)
        
        if get_json['author'] and get_json['quote']:
            author =get_json['author']
            quote =get_json['quote']
            
            new_quote=Quote(author,quote)
            
            return new_quote
        else:
            return None