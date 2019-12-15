import json
import requests


def response_ndjson_iteration(url):
    with requests.get(url=url, stream=True) as response:
        for resp_json in response.iter_lines():
            yield json.loads(resp_json)
