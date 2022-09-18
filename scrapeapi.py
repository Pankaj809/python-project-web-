from importlib.resources import contents
import requests as req
api_key = "7a4d1cc942c2920dff174722e92ba8a6"
web_url = "https://invozone.com/blog/data-and-web-scraping-for-dummies/"
param = {'access_key': api_key,
            'url' : web_url
}
resp = req.get('http://api.scrapestack.com/scrape', param)
website_data = resp.content
print(website_data)