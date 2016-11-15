from flask import Flask, url_for, request, jsonify
import requests as rq
import collections
import simplejson
from operator import itemgetter, attrgetter
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Jons giphy search api tool'

@app.route('/search/<gif>', methods = ['GET'])
def api_search(gif):
    urlinput = rq.get("http://api.giphy.com/v1/gifs/search?q="+gif+"&api_key=dc6zaTOxFJmzC&limit=1&offset=0&limit=6&fmt=json")
    urlresponse = urlinput.json()



    results = []
    for response_data in urlresponse['data']:
      url = response_data['url']
      gif_id = response_data['id']
      results.append({ 'data': [ { 'gif_id': gif_id, 'url': url } ] })
      if len(results) == 5:
        break
    if len(results) < 5:
      results = []
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
