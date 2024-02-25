import functools
from collections import OrderedDict
import requests


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco_cache:
                deco_cache[cache_key]['usage'] += 1
                deco_cache.move_to_end(cache_key, last=True)
                return deco_cache[cache_key]['data']
            result = f(*args, **kwargs)
            deco_cache[cache_key] = {'data': result, 'usage': 1}
            if len(deco_cache) > max_limit:
                min_freq_data = min(deco_cache, key=lambda x: deco_cache[x]['usage'])
                del deco_cache[min_freq_data]
            return result
        deco_cache = OrderedDict()
        return deco
    return internal


@cache(max_limit=200)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content