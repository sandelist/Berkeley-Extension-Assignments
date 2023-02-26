# This programme list and count all of the images:

from urllib.request import urlopen, urljoin
import re

url = input('Please input a link to a webpage (eg: https://www.berkeley.edu):')

images_count = 0

page = urlopen(url).read().decode('utf-8')

img_ex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)

img_ex.findall(page)

print('This webpage has ' + str(len(img_ex.findall(page))) + ' images:')

for i in img_ex.findall(page):
    print(i)