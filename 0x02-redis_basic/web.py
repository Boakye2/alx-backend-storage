#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it """
import requests
import redis
import time

redis_client = redis.Redis()

def get_page(url):
    # check if the cached content is available
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')
    
    # cache the content for 10 seconds
    count_key = f"count:{url}"
    redis_client.incr(count_key)
    redis_client.expire(count_key, 10)
    
    # get the HTML content from the URL
    response = requests.get(url)
    content = response.content.decode('utf-8')
    
    # cache the HTML content for 10 seconds
    redis_client.set(url, content, ex=10)
    
    return content



if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/10000/url/https://www.example.com"
    content = get_page(url)
    print(content)
    
