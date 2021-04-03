import re

def replace_func(url):
  url = url.replace('.','\\\.')
  url = url.replace('/', '\\\/')
  return url

def create_config():
  config = open('turboapps.json', 'a')
  config.write('''{
  "turboapps_desktop": {
    "known_applications_scopes": [
      "https://yandex.ru/games/"
    ],
    "apps_metadata": {''')
  urls = open("urls.txt")
  urls = [url.rstrip() for url in urls]
  urls_len = len(urls)
  i = 0
  while i < urls_len-1:
    config.write('''
      "%s": {
        "checkout_url": "%s"
      },''' % (urls[i], replace_func(urls[i])))
    i += 1
  config.write('''
      "%s": {
        "checkout_url": "%s"
      }
    }
  }
}''' % (urls[urls_len-1], replace_func(urls[urls_len-1])))

create_config()