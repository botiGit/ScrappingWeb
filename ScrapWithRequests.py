import requests
from bs4 import BeautifulSoup

base_url= 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
loc = 'Toledo'
page = 0

url = base_url + loc + "&start=" + str(page)

yelp_r =requests.get(url)
print(yelp_r.status_code)
yelp_soup =BeautifulSoup(yelp_r.text, 'html.parser')

print(yelp_soup.prettify())


#Si quisieramos buscar este elemento (normalmente es el elemento clave que queremos meter en un bucle for para imprimir)
#con el siguiente HTML code= <li class= "regular-search-result">
print(yelp_soup.find_all('li',{'class': 'regular-search-result'}))

for name in yelp_soup.find_all('a',{'class': 'biz-name  '}):
    print(name.text)

file_path = 'yelp-{loc}.txt'.format(loc=loc)

with open(file_path, "a") as textFile:
    businesses = yelp_soup.find_all('div',{'class': 'biz-listing-large'})
    for biz in businesses:
        title = biz.find_all('a', {'class':'biz-name'})[0].text
        phone = biz.find_all('span', {'class':'biz-phone'})[0].text

        page_line = "{title}\n{phone}\n\n".format(
            title=title,
            phone= phone
        )
        textFile.write(page_line)
        